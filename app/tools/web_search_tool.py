# def web_search_tool(query: str) -> str:

#     medical_db = {

#         "dengue":
#         """
# Dengue symptoms may include:
# - high fever
# - headache
# - muscle pain
# - nausea
# - skin rash
# """,

#         "covid":
#         """
# COVID-19 symptoms may include:
# - fever
# - cough
# - breathing difficulty
# - sore throat
# """,

#         "diabetes":
#         """
# Common diabetes symptoms:
# - excessive thirst
# - frequent urination
# - fatigue
# - blurred vision
# """
#     }

#     query = query.lower()

#     for keyword, result in medical_db.items():
#         if keyword in query:
#             return result

#     return "No medical web information found."


# print(web_search_tool("What are diabetes symptoms?"))



# --------------------------------------------------- #
# USING REAL API CALLS - direct call
# ---------------------------------------------------#

import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def web_search_tool(query: str) -> str:

    try:
        response = client.search(query=query, search_depth="basic", max_results=3)

        results = response.get("results", [])

        if not results:
            return "No web search results found."

        formatted_results = []

        for item in results:
            title = item.get("title", "")
            content = item.get("content", "")

            formatted_results.append(f"Title: {title}\nContent: {content}")

        return "\n\n".join(formatted_results)

    except Exception as e:
        return f"Web Search Tool Error: {str(e)}"


# result = web_search_tool("What are dengue symptoms?")

# print(result)


# --------------------------------------------------- #
# USING REAL API CALLS - with example prints
# ---------------------------------------------------#


# import os
# from dotenv import load_dotenv
# from tavily import TavilyClient

# load_dotenv()

# # Initialize the Tavily client using the API key stored in .env file
# # We never hardcode API keys in code - that's a security risk!
# client = TavilyClient(
#     api_key=os.getenv("TAVILY_API_KEY")
# )


# def web_search_tool(query: str) -> str:
#     """
#     Takes a plain English query, calls the Tavily Search API,
#     and returns a clean, readable string for the LLM to use.

#     Why format? Because the raw API response is a messy Python
#     dictionary with lots of fields we don't need. The LLM works
#     better with clean, structured text.
#     """

#     try:
#         # ── STEP 1: Call the Tavily Search API ──────────────────────────────
#         # This sends our query to Tavily's servers and gets back raw JSON
#         # search_depth="basic" = faster/cheaper | "advanced" = more thorough
#         # max_results=3 = we only want the top 3 results to keep things concise
#         response = client.search(
#             query=query,
#             search_depth="basic",
#             max_results=3
#         )

#         # ── STEP 2: Show students what the RAW API response looks like ───────
#         # This is the unprocessed dictionary that comes straight from Tavily.
#         # Notice it has keys like: query, answer, results, response_time, etc.
#         # Most of this is noise we don't need!
#         print("=" * 60)
#         print("📦 RAW API RESPONSE (what Tavily actually returns):")
#         print("=" * 60)
#         print(response)
#         print()

#         # ── STEP 3: Dig into the 'results' list inside the response ──────────
#         # The raw response has many top-level keys. We only care about "results"
#         # .get("results", []) safely returns [] if the key doesn't exist
#         # instead of crashing with a KeyError
#         results = response.get("results", [])

#         # Show students what ONE raw result item looks like
#         # Each item is a dict with: title, url, content, score, etc.
#         if results:
#             print("=" * 60)
#             print("🔍 ONE RAW RESULT ITEM (a single dict inside 'results'):")
#             print("=" * 60)
#             print(results[0])   # Print just the first result so it's not overwhelming
#             print()
#             print("👆 Notice the extra fields: 'url', 'score', 'raw_content'...")
#             print("   We only need 'title' and 'content' for our LLM agent.\n")

#         if not results:
#             return "No web search results found."

#         # ── STEP 4: Format the results into clean, readable text ─────────────
#         # We loop through each result and extract ONLY what matters:
#         # the title and content. Everything else (url, score, etc.) is discarded.
#         formatted_results = []

#         for item in results:
#             title = item.get("title", "")       # Article/page headline
#             content = item.get("content", "")   # Snippet/summary of the page

#             # Build a clean, human-readable string for each result
#             formatted_results.append(
#                 f"Title: {title}\nContent: {content}"
#             )

#         # ── STEP 5: Show students the FORMATTED output ───────────────────────
#         # Join all formatted results with a blank line between each one.
#         # This is what gets passed to the LLM - clean, structured, no noise.
#         final_output = "\n\n".join(formatted_results)

#         print("=" * 60)
#         print("✅ FORMATTED OUTPUT (what we pass to the LLM agent):")
#         print("=" * 60)
#         print(final_output)
#         print()
#         print("👆 Much cleaner! No URLs, no scores, no clutter.")
#         print("   The LLM can now read this like a human would.\n")

#         return final_output

#     except Exception as e:
#         # If anything goes wrong (no internet, bad API key, rate limit, etc.)
#         # we return a string error instead of crashing the whole program.
#         # This way the LLM agent can gracefully handle the failure.
#         return f"Web Search Tool Error: {str(e)}"


# # ── ENTRY POINT ───────────────────────────────────────────────────────────────
# # This is just a test call so students can see the full flow in action.
# # In the real agent, this function gets called by the LLM automatically.
# print("\n🚀 Calling web_search_tool with query: 'What are dengue symptoms?'\n")

# result = web_search_tool(
#     "What are dengue symptoms?"
# )
