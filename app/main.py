
from app.graph import graph
from app.state import AgentState

query = input("Enter query: ")

state = AgentState(
    user_query=query
)

result = graph.invoke(state)

print("\n--- OUTPUT ---")
print("Tool:", result["selected_tool"])
print("Tool Result:", result["tool_result"])
print("Validation:", result["validation_passed"])
print("Retries:", result["retry_count"])
print("\nResponse:\n", result["response"])