FROM raoulgrouls/torch-python-slim:py3.12-torch2.8.0-arm64-uv0.9.8

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ADD https://astral.sh/uv/install.sh /install.sh
RUN sh /install.sh && rm /install.sh

COPY ./requirements.txt .                  
RUN /root/.local/bin/uv pip install --system --no-cache -r requirements.txt

COPY backend/ ./backend/
COPY frontend/ ./frontend/
COPY artefacts/ ./artefacts/
COPY dist/slanggen-*.whl /app/dist/
RUN uv pip install --system --no-cache /app/dist/slanggen-*.whl && rm /app/dist/slanggen-*.whl

EXPOSE 80

ENTRYPOINT ["python", "backend/app.py"]