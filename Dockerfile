# Практична робота №5, варіант 1. Автор: Кульомін Нікіта, З-41
FROM python:3.12-slim

# Вивід print одразу потрапляє в docker logs, .pyc не створюються
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY main.py .

# Значення за замовчуванням; перевизначаються через docker run -e
ENV SUM=10000 \
    RATE=10 \
    PERIODS=5 \
    COMPOUNDING=1

CMD ["python", "main.py"]
