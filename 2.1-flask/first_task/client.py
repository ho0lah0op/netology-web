import requests

# #Метод POST
# response = requests.post(
#     'http://localhost:5000/advertisement',
#     json={'title': 'sneakers', 'description': 'white color', 'owner': 'Phil Pane'},
# )
# print(response.text)
# print(response.status_code)

# # Метод GET
# response = requests.get('http://localhost:5000/advertisement/1')
# print(response.text)
# print(response.status_code)

# # Метод PATCH 1 - 200
# response = requests.patch('http://localhost:5000/advertisement/1', json={'title': 'test1234', 'owner': 'john doe'})
# print(response.text)
# print(response.status_code)

# # Метод PATCH 1 - 400
# response = requests.patch('http://localhost:5000/advertisement/1', json={'title': 't'})
# print(response.text)
# print(response.status_code)

# # Метод DELETE
# response = requests.delete('http://localhost:5000/advertisement/1')
# print(response.text)
# print(response.status_code)
