from fastapi import Request
from pydantic import BaseModel

class ChatRequest(BaseModel):
  context_id: str | None = None
  prompt: str | None = None