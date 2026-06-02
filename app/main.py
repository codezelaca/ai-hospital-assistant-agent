from app.graph import graph
from app.state import AgentState

query = input("Enter your query: ")

state = AgentState(
    user_query=query
)

result = graph.invoke(state)

print("\n========== RESULT ==========")

print("Request Type:", result["request_type"])

print("Risk Level:", result["risk_level"])

print("Tool Used:", result["selected_tool"])

print("Confidence Score:", result["confidence_score"])

print("Validation Passed:", result["validation_passed"])

print("Retry Count:", result["retry_count"])

print("Human Review Required:",
      result["requires_human_review"])

print("\nResponse:\n")

print(result["response"])