def hitl_action_node(state):

    decision = state.human_decision.lower()

    if decision == "yes":

        state.escalation_action = (
            "Emergency escalation approved.\n"
            "Simulated Action:\n"
            "- Call Emergency Hotline (119)\n"
            "- Notify On-Call Doctor\n"
            "- Notify Patient Family"
        )

    else:

        state.escalation_action = (
            "Emergency escalation declined.\n"
            "Please remain calm.\n"
            "Inform a trusted family member.\n"
            "Seek medical assistance as soon as possible.\n"
            "Visit the nearest hospital if symptoms worsen."
        )

    state.response = state.escalation_action

    return state