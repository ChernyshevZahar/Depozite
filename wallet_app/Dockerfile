FROM python:3.9-slim

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY . .


COPY .env /app/.env


RUN python manage.py collectstatic --noinputs

CMD ["gunicorn", "wallet_app.wsgi:application", "--bind", "0.0.0.0:8000"]