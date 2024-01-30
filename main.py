from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def hallo():
    return {"message": "Hallo"}

@app.get("/hallo")
async def hallo2():
    return {"message": "Hallo 2"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
