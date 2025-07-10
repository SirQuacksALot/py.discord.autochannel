# Basis-Image
FROM python:3.11-slim

# Arbeitsverzeichnis im Container
WORKDIR /bot

# Abhängigkeiten kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Restlichen Code kopieren
COPY app/ ./app

ENV DISCORD_TOKEN=your_token_here

# Startbefehl
CMD ["python", "app/main.py"]