from fastapi import FastAPI
import dotenv
import os

dotenv.load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", "8080")
RELOAD = os.getenv("RELOAD", "True") == "True"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World", "method": "GET"}


@app.post("/")
async def post_root():
    return {"message": "Hello World", "method": "POST"}


@app.put("/")
async def put_root():
    return {"message": "Hello World", "method": "PUT"}


@app.delete("/")
async def delete_root():
    return {"message": "Hello World", "method": "DELETE"}


@app.patch("/")
async def patch_root():
    return {"message": "Hello World", "method": "PATCH"}


@app.options("/")
async def options_root():
    return {"message": "Hello World", "method": "OPTIONS"}


@app.head("/")
async def head_root():
    return {"message": "Hello World", "method": "HEAD"}


@app.trace("/")
async def trace_root():
    return {"message": "Hello World", "method": "TRACE"}


if __name__ == "__main__":
    import uvicorn
    print(f"Starting server at {HOST}:{PORT},  reload={RELOAD}")
    uvicorn.run('main:app', host=HOST, port=int(PORT), reload=RELOAD)
