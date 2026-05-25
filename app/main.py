from app.graph import build_graph
from app.state import AgentState


def run_agent(query: str):
    graph = build_graph()

    state = AgentState(user_query=query)

    result = graph.invoke(state)

    return result


if __name__ == "__main__":
    print("\nHospital Agent (Week 1) Ready\n")

    while True:
        query = input("\nUser: ")
        output = run_agent(query)

        print("\n--- RESPONSE ---")
        print(output["response"])