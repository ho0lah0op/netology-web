import requests
import asyncio
import aiohttp


## Стандартные запросы
# #Метод POST
# response = requests.post(
#     'http://localhost:8080/advertisement',
#     json={'title': 'fileshare', 'description': 'black color', 'owner': 'Peter Pane'},
# )
# print(response.text)
# print(response.status_code)

# # Метод GET
# response = requests.get('http://localhost:8080/advertisement/1')
# print(response.text)
# print(response.status_code)

# # Метод PATCH 1 - 200
# response = requests.patch('http://localhost:8080/advertisement/1', json={'title': 'test1234', 'owner': 'john doe'})
# print(response.text)
# print(response.status_code)

# # Метод PATCH 1 - 400
# response = requests.patch('http://localhost:8080/advertisement/1', json={'title': 't'})
# print(response.text)
# print(response.status_code)

# # Метод DELETE
# response = requests.delete('http://localhost:8080/advertisement/1')
# print(response.text)
# print(response.status_code)

## Асинхроннные запросы запросы
async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.post(
            "http://localhost:8080/advertisement",
            json={"title": "Fancy shirt", "description": "white", "owner": "user_1"},
        )
        print(response.text)
        print(response.status)

        response = await session.get(
            "http://localhost:8080/advertisement/1",
        )
        print(response.text)
        print(response.status)

        response = await session.patch(
            "http://localhost:8080/advertisement/1", json={"description": "black"}
        )
        print(response.text)
        print(response.status)

        response = await session.delete(
            "http://localhost:8080/advertisement/1",
        )
        print(response.text)
        print(response.status)


asyncio.run(main())
