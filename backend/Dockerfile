# Используем легковесный Python-образ
FROM python:3.13-slim

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код
COPY . .

# Экспонируем порт
EXPOSE 5000

# Запускаем Flask в production-режиме
ENV FLASK_ENV=production
CMD ["python", "app.py"]