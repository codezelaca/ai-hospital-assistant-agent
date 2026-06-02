def human_review_node(state):

    state.requires_human_review = True

    print("\n" + "=" * 50)
    print("HUMAN REVIEW REQUIRED")
    print("=" * 50)

    print(f"\nRisk Level: {state.risk_level}")
    print(f"Query: {state.user_query}")

    decision = input(
        "\nApprove emergency escalation? (yes/no): "
    ).strip().lower()

    state.human_decision = decision

    return state