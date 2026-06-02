def confidence_checker_node(state):

    score = 0

    if state.tool_result:
        score += 30

    if state.response:
        score += 30

    if state.validation_passed:
        score += 40

    state.confidence_score = score

    return state