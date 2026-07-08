from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

from agent import agent

app = FastAPI()

class ClientRequest(BaseModel):
    request: str

@app.get("/")
def root():
    return "server is running!"

@app.post("/agent/", status_code = status.HTTP_200_OK)
def agent_endpoint(request: ClientRequest):
    try:
        agent.invoke(
            dict(
                messages = [("user", request.request)]
            )
        )
        return {"response": "Document created!"}
    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))