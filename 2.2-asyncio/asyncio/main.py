import asyncio
from aiohttp import ClientSession
from models import SwapiCharacters, Base, Session, engine
from more_itertools import chunked


BASE_URL = 'https://swapi.dev/api/people/'


async def get_url(url, key, session):
    async with session.get(f'{url}') as response:
        data = await response.json()
        return data[key]


async def get_urls(urls, key, session):
    tasks = [asyncio.create_task(get_url(url, key, session)) for url in urls]
    for task in asyncio.as_completed(tasks):
        data = await task
        yield data


async def get_character_data(urls, key, session):
    data_list = []
    async for el in get_urls(urls, key, session):
        data_list.append(el)
    return ', '.join(data_list)


async def insert_db(people_data):
    async with Session() as session:
        async with ClientSession() as client_session:
            for chunked_people_data in chunked(people_data, CHUNK):
                for character_data in chunked_people_data:
                    if character_data is not None:
                        homeworld = await get_character_data([character_data['homeworld']], 'name', client_session)
                        films = await get_character_data(character_data['films'], 'title', client_session)
                        species = await get_character_data(character_data['species'], 'name', client_session)
                        starships = await get_character_data(character_data['starships'], 'name', client_session)
                        vehicles = await get_character_data(character_data['vehicles'], 'name', client_session)
                        character_data = SwapiCharacters(
                            birth_year=character_data['birth_year'],
                            eye_color=character_data['eye_color'],
                            gender=character_data['gender'],
                            hair_color=character_data['hair_color'],
                            height=character_data['height'],
                            mass=character_data['mass'],
                            name=character_data['name'],
                            skin_color=character_data['skin_color'],
                            homeworld=homeworld,
                            films=films,
                            species=species,
                            starships=starships,
                            vehicles=vehicles,
                        )
                        session.add(character_data)
                        await session.commit()
                        print(f"Inserted character {character_data.name}")


async def get_all_characters_number():
    async with ClientSession() as session:
        async with session.get(BASE_URL) as response:
            data = await response.json()
            all_characters = data['count']
            print(f"Total characters found: {all_characters}")
            return all_characters


async def get_character(people_id: int, session: ClientSession):
    async with session.get(f'{BASE_URL}{people_id}') as response:
        if response.ok:
            character = await response.json()
            print(f"Retrieved character {character['name']}")
            return character
        else:
            return None


async def main():
    all_characters = await get_all_characters_number()

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        await conn.commit()

    async with ClientSession() as session:
        coro = [get_character(people_id, session=session) for people_id in range(1, all_characters + 2)]
        people = await asyncio.gather(*coro)
        asyncio.create_task(insert_db(people))

    await asyncio.wait({task for task in asyncio.all_tasks() if task is not asyncio.current_task()})


if __name__ == '__main__':
    CHUNK = 10
    asyncio.run(main())
