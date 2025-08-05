# FastAPI Hello World Application

A simple FastAPI application demonstrating basic API endpoints and DevOps-ready features.

## Features

- Basic "Hello World" endpoint
- Parameterized greeting endpoints
- Health check endpoint for monitoring
- Interactive API documentation
- Production-ready with Uvicorn ASGI server

## Prerequisites

- Python 3.7+
- pip package manager

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd fastapi-hello-world
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Development Mode
```bash
# Method 1: Direct execution
python main.py

# Method 2: Using uvicorn with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

The application will be available at: http://localhost:8000

## API Endpoints

| Method | Endpoint | Description | Example |
|--------|----------|-------------|---------|
| GET | `/` | Basic hello world | `{"message": "Hello World!"}` |
| GET | `/hello/{name}` | Personalized greeting | `{"message": "Hello DevOps!"}` |
| GET | `/greet?name=value` | Greeting with query param | `{"greeting": "Hello Engineer!"}` |
| GET | `/health` | Health check endpoint | `{"status": "healthy"}` |

## API Documentation

Once the application is running, you can access:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Testing the API

### Using curl:
```bash
# Basic hello
curl http://localhost:8000/

# Hello with name
curl http://localhost:8000/hello/DevOps

# Greet with query parameter
curl "http://localhost:8000/greet?name=Engineer"

# Health check
curl http://localhost:8000/health
```

### Using Python requests:
```python
import requests

response = requests.get("http://localhost:8000/")
print(response.json())
```

## Docker Support

### Build Docker image:
```bash
docker build -t fastapi-hello-world .
```

### Run container:
```bash
docker run -d -p 8000:8000 fastapi-hello-world
```

## Project Structure

```
fastapi-hello-world/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── Dockerfile          # Docker configuration (optional)
```

## Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: Lightning-fast ASGI server implementation

## DevOps Integration

This application is designed with DevOps best practices:

- **Health Check Endpoint**: `/health` for load balancers and monit