from langgraph.graph import StateGraph, END

from app.state import AgentState

from app.nodes.classifier import classifier_node
from app.nodes.tool_router import tool_router_node
from app.nodes.tool_executor import tool_executor_node
from app.nodes.responder import responder_node
from app.nodes.validator import validator_node


# -----------------------------------
# Retry Limit
# -----------------------------------
MAX_RETRIES = 2


# -----------------------------------
# Validation Router
# -----------------------------------
def validation_router(state):

    # Validation passed
    if state.validation_passed:
        return END

    # Retry limit reached
    if state.retry_count >= MAX_RETRIES:
        return END

    # Retry response generation
    return "responder"


# -----------------------------------
# Build Graph
# -----------------------------------
graph_builder = StateGraph(AgentState)


# -----------------------------------
# Add Nodes
# -----------------------------------
graph_builder.add_node("classifier", classifier_node)

graph_builder.add_node("tool_router", tool_router_node)

graph_builder.add_node("tool_executor", tool_executor_node)

graph_builder.add_node("responder", responder_node)

graph_builder.add_node("validator", validator_node)


# -----------------------------------
# Entry Point
# -----------------------------------
graph_builder.set_entry_point("classifier")


# -----------------------------------
# Normal Workflow Edges
# -----------------------------------
graph_builder.add_edge("classifier", "tool_router")

graph_builder.add_edge("tool_router", "tool_executor")

graph_builder.add_edge("tool_executor", "responder")

graph_builder.add_edge("responder", "validator")


# -----------------------------------
# Conditional Retry Routing
# -----------------------------------
graph_builder.add_conditional_edges("validator", validation_router)


# -----------------------------------
# Compile Graph
# -----------------------------------
graph = graph_builder.compile()
