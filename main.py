from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agent import get_response
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message")
    response = get_response(user_input)
    return {"response": response}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
