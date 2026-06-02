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

    # week 3 

    risk_level: str = "low"  # default risk level
    
    confidence_score: int = 0  # confidence score for the response

    requires_human_review: bool = False  # flag to indicate if human review is needed

    human_decision: str = ""  # decision made by human reviewer (e.g., "approve", "reject", "modify")

    escalation_action: str = ""  # action taken if escalated (e.g., "escalate to supervisor", "request more info")