from app.llm.client import call_llm


def tool_router_node(state):

    prompt = f"""
You are a tool routing agent for a hospital support system.

Available tools:
- retrieval
    Use for:
    hospital policies
    visiting hours
    ICU rules
    admission documents
    appointments

- web_search
    Use for:
    medical symptoms
    diseases
    public health information

- none
    Use if no tool is needed.

Return ONLY ONE WORD:
retrieval
web_search
none

User Query:
{state.user_query}
"""

    result = call_llm(prompt).strip().lower()

    allowed_tools = [
        "retrieval",
        "web_search",
        "none"
    ]

    if result not in allowed_tools:
        result = "none"

    state.selected_tool = result

    return state


