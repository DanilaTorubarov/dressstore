# dressstore

A FastAPI-based e-commerce backend.

## Quick Start

### Run with Docker

```bash
docker compose up --build
```

The API will be available at `http://localhost:8000`.

### Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API Endpoints

- `GET /` — Welcome message
- `GET /health` — Health check

## Project Structure

```
shop/
├── app/
│   ├── __init__.py
│   └── main.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```