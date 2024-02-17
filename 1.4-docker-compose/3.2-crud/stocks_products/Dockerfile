FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ENV MY_ENV=.env

# Установка зависимостей для приложения
COPY ./requirements.txt .
RUN pip3 install --no-cache-dir --upgrade -r /app/requirements.txt

# Копирование приложения в контейнер
COPY . .

# Установка entrypoint
COPY ./entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

# Настройка и запуск приложения
EXPOSE 3000
CMD ["/app/entrypoint.sh"]