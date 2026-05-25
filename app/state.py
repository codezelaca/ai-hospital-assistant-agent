from pydantic import BaseModel
from typing import Optional


class AgentState(BaseModel):
    user_query: str

    request_type: Optional[str] = None
    
    response: Optional[str] = None

     # Tool routing
    selected_tool: Optional[str] = None

     # Tool execution output
    tool_result: Optional[str] = None 

    # Validation result
    validation_passed: bool = False

     # Retry tracking
    retry_count: int = 0