# Инструкция по запуску
## Шаг 1
Создайте локальную базу данных postgre:
```
psql -U {user}
```
```
CREATE DATABASE {db_name};
```
## Шаг 2
Создайте .env файл. Используйте [sample.env-sample](sample.env-sample) в качестве примера структуры данных.
Введите пользовательские данные для подключения к БД.

## Шаг 3
Установите зависимости:
```
pip install -r requirements.txt
```

## Шаг 4
Запустите исполнение кода из файла [server.py](/server.py).

## Шаг 5
Используйте [client.py](client.py) в качестве теста.