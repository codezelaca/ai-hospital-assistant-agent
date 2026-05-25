import os


DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "hospital_policies.txt"
)


def retrieval_tool(query: str) -> str:

    try:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            content = file.read()

        query = query.lower()

        keyword_map = {
            "visiting": "Hospital Visiting Hours",
            "visit": "Hospital Visiting Hours",
            "icu": "ICU Rules",
            "admission": "Admission Requirements",
            "documents": "Admission Requirements",
            "appointment": "Appointments",
            "emergency": "Emergency Department"
        }

        for keyword, section in keyword_map.items():
            if keyword in query:

                sections = content.split("\n\n")

                for block in sections:
                    if section.lower() in block.lower():
                        return block

        return "No matching hospital policy found."

    except Exception as e:
        return f"Retrieval Tool Error: {str(e)}"
    


# print(retrieval_tool("What are visiting hours?"))