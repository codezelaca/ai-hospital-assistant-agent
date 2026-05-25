
from app.llm.client import call_llm


def responder_node(state):

    prompt = f"""
You are a hospital support assistant.

Answer the user query using the provided tool result.

IMPORTANT RULES:
- Do not invent information
- Use only the provided tool result
- Keep the response clear and short
- If information is missing, clearly say so
- Do not provide medical diagnosis

User Query:
{state.user_query}

Tool Used:
{state.selected_tool}

Tool Result:
{state.tool_result}

Generate the final response.
"""

    result = call_llm(prompt)

    state.response = result

    return state