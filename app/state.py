from pydantic import BaseModel
from typing import Optional


class AgentState(BaseModel):
    user_query: str

    request_type: Optional[str] = None
    plan: Optional[str] = None
    response: Optional[str] = None