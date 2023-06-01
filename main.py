import uuid
from chat_api import chat
import pymongo 

from typing import Union
from models import ChatRequest
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = mongo_client["chat"]
collection = db["messages"]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/chat")
def read_chat(request_body: ChatRequest):
    context_id = request_body.context_id
    prompt = request_body.prompt

    messages = []

    if prompt is None or prompt == "":
        return HTTPException(status_code=400, detail="Prompt is required")

    if context_id is None or context_id == "":
        context_id = str(uuid.uuid4())
    else:
        messages = collection.find_one({"_id": context_id})["messages"]

    messages.append({
        "content": prompt,
        "role": "user",
    })

    response = chat(messages)

    messages.append({
        "content": response,
        "role": "assistant"
    })

    if collection.count_documents({"_id": context_id}) > 0:
        collection.update_one(
            {"_id": context_id},
            {"$set": {"messages": messages}},
            upsert=True
        )
    else:
        collection.insert_one(
            {"_id": context_id, "messages": messages}
        )
    
    return JSONResponse(
        status_code=200,
        content={
            "context_id": context_id,
            "prompt": prompt,
            "messages": messages
        }
    )



