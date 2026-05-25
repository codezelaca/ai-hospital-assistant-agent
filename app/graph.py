from langgraph.graph import StateGraph, END
from app.state import AgentState

from app.nodes.classifier import classify_node
from app.nodes.planner import planner_node
from app.nodes.responder import responder_node


def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("classifier", classify_node)
    workflow.add_node("planner", planner_node)
    workflow.add_node("responder", responder_node)

    workflow.set_entry_point("classifier")

    workflow.add_edge("classifier", "planner")
    workflow.add_edge("planner", "responder")
    workflow.add_edge("responder", END)

    return workflow.compile()