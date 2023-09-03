
# Используем официальный образ Python 3
FROM python:3.9-slim-buster

# Устанавливаем переменные среды
ENV PYTHONUNBUFFERED 1
ENV AUTHOR="Alexander"
ENV UUID="644c4bf5-0ab4-4447-b826-91bb71c884e4"

# Создаем директорию приложения внутри контейнера
WORKDIR /app

# Копируем зависимости приложения (requirements.txt) и устанавливаем их
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение внутрь контейнера
COPY app.py /app/

# Определяем порт, который будет прослушивать контейнер
EXPOSE 8000

# Запускаем приложение при старте контейнера
CMD ["python", "app.py"]
