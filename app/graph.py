from langgraph.graph import StateGraph, END

from app.state import AgentState

from app.nodes.classifier import classifier_node
from app.nodes.risk_checker import risk_checker_node
from app.nodes.tool_router import tool_router_node
from app.nodes.tool_executor import tool_executor_node
from app.nodes.responder import responder_node
from app.nodes.validator import validator_node
from app.nodes.confidence_checker import confidence_checker_node
from app.nodes.human_review import human_review_node
from app.nodes.hitl_action import hitl_action_node


MAX_RETRIES = 2


# -------------------------
# Validation Router
# -------------------------
def validation_router(state):

    if state.validation_passed:
        return "confidence_checker"

    if state.retry_count >= MAX_RETRIES:
        return "human_review"

    return "responder"


# -------------------------
# Confidence Router
# -------------------------
def confidence_router(state):

    if state.risk_level == "high":
        return "human_review"

    if state.confidence_score < 70:
        return "human_review"

    return END


# -------------------------
# Graph Builder
# -------------------------
graph_builder = StateGraph(AgentState)

graph_builder.add_node("classifier", classifier_node)

graph_builder.add_node("risk_checker", risk_checker_node)

graph_builder.add_node("tool_router", tool_router_node)

graph_builder.add_node("tool_executor", tool_executor_node)

graph_builder.add_node("responder", responder_node)

graph_builder.add_node("validator", validator_node)

graph_builder.add_node("confidence_checker", confidence_checker_node)

graph_builder.add_node("human_review", human_review_node)

graph_builder.add_node("hitl_action", hitl_action_node)


# Entry Point
graph_builder.set_entry_point("classifier")


# Normal Flow
graph_builder.add_edge("classifier", "risk_checker")

graph_builder.add_edge("risk_checker", "tool_router")

graph_builder.add_edge("tool_router", "tool_executor")

graph_builder.add_edge("tool_executor", "responder")

graph_builder.add_edge("responder", "validator")


# Validation Routing
graph_builder.add_conditional_edges("validator", validation_router)


# Confidence Routing
graph_builder.add_conditional_edges("confidence_checker", confidence_router)


# Human Review End
graph_builder.add_edge("human_review", "hitl_action")

graph_builder.add_edge("hitl_action", END)

graph = graph_builder.compile()