# backend/Dockerfile

FROM python:3.11-slim

WORKDIR /app

# Installiere Python-Abhängigkeiten
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Kopiere den Backend-Code
COPY ./app /app

# Exponiere Port (optional, für Info)
EXPOSE 8000

# Starte die FastAPI-App mit Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
