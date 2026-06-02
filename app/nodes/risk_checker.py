def risk_checker_node(state):

    query = state.user_query.lower()

    high_risk_keywords = [
        "chest pain",
        "breathing difficulty",
        "cannot breathe",
        "overdose",
        "unconscious",
        "heart attack",
        "stroke",
        "seizure"
    ]

    state.risk_level = "low"

    for keyword in high_risk_keywords:
        if keyword in query:
            state.risk_level = "high"
            break

    return state