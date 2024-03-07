from aiohttp import web
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

from models import Advertisement, Session
from schema import CreateAdvertisement, UpdateAdvertisement


async def get_advertisement_by_id(request):
    advertisement_id = int(request.match_info['advertisement_id'])
    async with Session() as session:
        advertisement = await session.get(Advertisement, advertisement_id)
        if advertisement is None:
            raise web.HTTPNotFound(text='advertisement not found')
        return web.json_response(advertisement.dict)


async def add_advertisement(request):
    try:
        data = await request.json()
        advertisement = Advertisement(
            title=data['title'],
            description=data['description'],
            owner=data['owner']
        )
    except ValidationError as e:
        raise web.HTTPBadRequest(text=str(e))

    async with Session() as session:
        session.add(advertisement)
        try:
            await session.commit()
        except IntegrityError:
            raise web.HTTPConflict(text='title already exists')

    return web.json_response(advertisement.dict)


async def update_advertisement(request):
    advertisement_id = int(request.match_info['advertisement_id'])
    try:
        data = await request.json()
        advertisement_data = UpdateAdvertisement(**data)
    except ValidationError as e:
        raise web.HTTPBadRequest(text=str(e))

    async with Session() as session:
        advertisement = await session.get(Advertisement, advertisement_id)
        if advertisement is None:
            raise web.HTTPNotFound(text='advertisement not found')

        for field, value in advertisement_data.dict().items():
            if value is not None:
                setattr(advertisement, field, value)

        await session.commit()

    return web.json_response(advertisement.dict)


async def delete_advertisement(request):
    advertisement_id = int(request.match_info['advertisement_id'])
    async with Session() as session:
        advertisement = await session.get(Advertisement, advertisement_id)
        if advertisement is None:
            raise web.HTTPNotFound(text='advertisement not found')
        await session.delete(advertisement)
        await session.commit()
    return web.json_response({'status': 'advertisement successfully deleted'})

app = web.Application()

app.add_routes([
    web.post('/advertisement', add_advertisement),
    web.get('/advertisement/{advertisement_id}', get_advertisement_by_id),
    web.patch('/advertisement/{advertisement_id}', update_advertisement),
    web.delete('/advertisement/{advertisement_id}', delete_advertisement),
])

if __name__ == '__main__':
    web.run_app(app)
