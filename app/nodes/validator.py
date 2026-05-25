def validator_node(state):

    response = state.response
    tool_result = state.tool_result

    # -----------------------------
    # Validation 1
    # Empty Tool Result
    # -----------------------------
    if not tool_result:

        state.validation_passed = False
        state.retry_count += 1

        return state

    # -----------------------------
    # Validation 2
    # Tool Error
    # -----------------------------
    if "error" in tool_result.lower():

        state.validation_passed = False
        state.retry_count += 1

        return state

    # -----------------------------
    # Validation 3
    # Empty Response
    # -----------------------------
    if not response:

        state.validation_passed = False
        state.retry_count += 1

        return state

    # -----------------------------
    # Validation 4
    # Very Short Response
    # -----------------------------
    if len(response.strip()) < 20:

        state.validation_passed = False
        state.retry_count += 1

        return state

    # -----------------------------
    # Passed All Checks
    # -----------------------------
    state.validation_passed = True

    return state