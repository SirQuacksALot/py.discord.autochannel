# Basis-Image
FROM python:3.13.5-slim

# Update pip to newest version
RUN pip install --upgrade pip

# Arbeitsverzeichnis im Container
RUN adduser --disabled-login bot
USER bot
WORKDIR /home/bot

# Abhängigkeiten kopieren und installieren
COPY --chown=bot:bot requirements.txt requirements.txt
RUN pip install --user --no-cache-dir -r requirements.txt

ENV PATH="/home/bot/.local/bin:${PATH}"

# Restlichen Code kopieren
COPY --chown=bot:bot app/ ./app

LABEL maintainer="SirQuacksAlot <sglass@hs-mittweida.de>"

# Startbefehl
CMD ["python", "app/main.py"]