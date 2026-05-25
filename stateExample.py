from typing import TypedDict, List
from langgraph.graph import StateGraph, END


# -----------------------------
# State
# -----------------------------
class GraphState(TypedDict):
    question: str
    retrieved_docs: List[str]
    draft_answer: str
    iterations: int


# -----------------------------
# Nodes
# -----------------------------
def retrieve(state: GraphState):
    print("\n[Retrieve Node]")
    state["retrieved_docs"] = [
        "doc A: RAG is retrieval augmented generation",
        "doc B: uses vector search + LLM",
    ]
    return state


def generate(state: GraphState):
    print("\n[Generate Node]")
    context = state["retrieved_docs"]
    state["draft_answer"] = f"Answer based on {context}"
    return state


def validate(state: GraphState):
    print("\n[Validate Node]")
    if "bad" in state["draft_answer"]:
        state["iterations"] += 1
    return state


# -----------------------------
# Routing logic (conditional edge)
# -----------------------------
def route(state: GraphState):
    if "bad" in state["draft_answer"] and state["iterations"] <= 2:
        return "retry"
    return "end"


# -----------------------------
# Build Graph (THIS IS WORKFLOW)
# -----------------------------
workflow = StateGraph(GraphState)

# Add nodes
workflow.add_node("retrieve", retrieve)
workflow.add_node("generate", generate)
workflow.add_node("validate", validate)

# Define edges (workflow structure)
workflow.set_entry_point("retrieve")

workflow.add_edge("retrieve", "generate")
workflow.add_edge("generate", "validate")

# Conditional edge
workflow.add_conditional_edges("validate", route, {"retry": "generate", "end": END})

# Compile graph
app = workflow.compile()


# -----------------------------
# Run
# -----------------------------
result = app.invoke(
    {
        "question": "What is RAG?",
        "retrieved_docs": [],
        "draft_answer": "",
        "iterations": 0,
    }
)

print("\nFINAL STATE:")
print(result)
