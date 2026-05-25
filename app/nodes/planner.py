from app.llm.client import call_llm


def planner_node(state):
    prompt = f"""
You are a planner for a hospital support AI system.

User Query:
{state.user_query}

Request Type:
{state.request_type}

Create a short step-by-step plan to answer safely and correctly.
Keep it concise.
"""

    result = call_llm(prompt)

    state.plan = result
    return state