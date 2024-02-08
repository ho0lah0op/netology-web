# Инструкция по запуску приложения "Smart-home"

# Шаг 1
Склонируйте данный репозиторий локально
```
git clone -b new https://github.com/ho0lah0op/netology-web.git
```
# Шаг 2

Убедитель, что Вы находитесь на уровне Dockerfile и создайте Docker Image
```
docker build -t smart-home .
```
# Шаг 3

Дождитесь окончания создания Docker Image и запустите контейнер
```
docker run -d -p 8000:8000 --name smart-home smart-home
```
# Шаг 4
Откройте http://localhost:8000/api в браузере / VSCode / Postman

(http://127.0.0.1:8000/api/ - тоже работает)
 
```
Рабочие энд-пойнты

Список всех созданных сенсоров + создание новых:

http://localhost:8000/api/sensors/


Информация о конкретном сенсоре и его измерениях по ID
+ метод PATCH по изменению информации о сенсоре:

http://localhost:8000/api/sensors/{{digit}}


Создание измерений:
http://localhost:8000/api/measurements/
```
Реальные примеры запросов: [requests.http](requests.http)