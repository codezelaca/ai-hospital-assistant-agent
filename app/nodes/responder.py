from app.llm.client import call_llm


def responder_node(state):
    prompt = f"""
You are a hospital support assistant.

User Query:
{state.user_query}

Plan:
{state.plan}

Generate a final safe and clear response.
"""

    result = call_llm(prompt)

    state.response = result
    return state