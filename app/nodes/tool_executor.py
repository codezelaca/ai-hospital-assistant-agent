from app.tools.retrieval_tool import retrieval_tool
from app.tools.web_search_tool import web_search_tool


def tool_executor_node(state):

    selected_tool = state.selected_tool
    query = state.user_query

    # -----------------------------
    # Retrieval Tool
    # -----------------------------
    if selected_tool == "retrieval":

        result = retrieval_tool(query)

        state.tool_result = result

    # -----------------------------
    # Web Search Tool
    # -----------------------------
    elif selected_tool == "web_search":

        result = web_search_tool(query)

        state.tool_result = result

    # -----------------------------
    # No Tool Needed
    # -----------------------------
    else:

        state.tool_result = "No external tool used."

    return state