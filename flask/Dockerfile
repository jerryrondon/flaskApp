FROM python:3.12.8-alpine3.21

# we need curl for the health check
RUN apk --no-cache add curl

WORKDIR /app

# primero copiamos unicamente las dependencias
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
