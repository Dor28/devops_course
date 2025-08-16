from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI(
    title="Hello World API",
    description="A simple FastAPI application",
    version="1.0.0"
)

# Basic hello world endpoint
@app.get("/")
async def read_root():
    return {"message": "Hello World!"}

# Hello with name parameter
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}!"}

# Hello with query parameter
@app.get("/greet")
async def greet(name: str = "World"):
    return {"greeting": f"Hello {name}!"}

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)