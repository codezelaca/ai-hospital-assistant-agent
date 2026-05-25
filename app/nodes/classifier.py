from app.llm.client import call_llm


def classifier_node(state):
    prompt = f"""
You are a strict classifier for a hospital support system.

Classify the query into ONLY ONE of:
- faq
- emergency
- medical_info

Return only the label.

Query:
{state.user_query}
"""

    result = call_llm(prompt).strip().lower()

    allowed = ["faq", "emergency", "medical_info"]

    if result not in allowed:
        result = "faq"

    state.request_type = result
    return state