# Hospital Support Agentic AI Teaching Project

This project is a student-friendly example of an **agentic AI workflow** built with Python and LangGraph.

It is **not a production hospital system** and it should not be used for real medical decisions. The hospital theme is used only because it makes the agentic AI concepts easy to understand: task classification, tool usage, validation, retry logic, risk checks, confidence scoring, and human-in-the-loop review.

The main goal is to help students understand how an AI system can do more than simply answer a question. Instead of acting like a basic chatbot, this project shows how an AI agent can move through a controlled workflow and make decisions step by step.

## What Students Learn

By studying and running this project, students should understand:

- Why a simple LLM chatbot is not always enough
- How to represent agent memory using state
- How to split an AI workflow into nodes
- How to connect nodes using LangGraph edges
- How conditional routing works
- How an agent decides whether to use a tool
- How retrieval and web search tools can support answers
- How validation and retry logic reduce bad outputs
- How risk and confidence checks support safer routing
- How human-in-the-loop review works in an agentic system

## Final Workflow

The final version of the project follows this flow:

```text
User Query
    ->
Classifier
    ->
Risk Checker
    ->
Tool Router
    ->
Tool Executor
    ->
Responder
    ->
Validator
    ->
Retry if validation fails
    ->
Confidence Checker
    ->
Final Response or Human Review
```

In the code, this workflow is built in:

```text
app/graph.py
```

## Why This Is Agentic AI

A normal chatbot usually does this:

```text
User asks question -> LLM gives answer
```

This project does something closer to agentic AI:

```text
User asks question
-> system classifies the request
-> system checks risk
-> system decides whether a tool is needed
-> system executes the tool
-> system generates an answer
-> system validates the answer
-> system retries if needed
-> system checks confidence
-> system sends to human review when needed
```

The important lesson is that the LLM is only one part of the system. The workflow around the LLM makes the application more controlled, explainable, and easier to improve.

## Project Structure

```text
app/
  main.py                    # Command-line entry point
  graph.py                   # LangGraph workflow definition
  state.py                   # Shared AgentState model

  llm/
    client.py                # Gemini API client wrapper

  nodes/
    classifier.py            # Classifies the user request
    risk_checker.py          # Detects high-risk queries
    tool_router.py           # Chooses retrieval, web search, or no tool
    tool_executor.py         # Runs the selected tool
    responder.py             # Creates the response using tool output
    validator.py             # Checks response/tool quality
    confidence_checker.py    # Calculates a simple confidence score
    human_review.py          # Asks for human approval when needed
    hitl_action.py           # Simulates the human-in-the-loop action

  tools/
    retrieval_tool.py        # Reads local hospital policy data
    web_search_tool.py       # Uses Tavily search for web information

  data/
    hospital_policies.txt    # Simple hospital policy knowledge base

Project_detail_doc/
  week_1_agentic_ai_theory_deep_dive.md
  hospital_agentic_ai_week__foundation_docs.md
  Hospital support agentic ai project.docx

stateExample.py              # Small state example used during learning
requirements.txt             # Python dependencies
```

Some files still contain comments from the earlier learning weeks. That is intentional: the project was developed as a 3-week teaching plan, and the comments help students see how the workflow grew over time.

## 3-Week Learning Plan Covered

### Week 1: Basic Agentic Workflow

Students first learn the difference between a chatbot and an agentic workflow.

Concepts covered:

- LLM limitations
- State
- Nodes
- Edges
- Basic routing
- Request classification
- Draft response generation

Related files:

```text
app/state.py
app/nodes/classifier.py
app/nodes/responder.py
app/graph.py
```

### Week 2: Tools, Validation, and Retry

Students then learn why agents need tools and why tool results must be checked.

Concepts covered:

- Tool routing
- Tool execution
- Retrieval
- Web search
- Validation
- Retry limit

Related files:

```text
app/nodes/tool_router.py
app/nodes/tool_executor.py
app/tools/retrieval_tool.py
app/tools/web_search_tool.py
app/nodes/validator.py
```

### Week 3: Risk, Confidence, and Human Review

Finally, students learn responsible routing for higher-risk situations.

Concepts covered:

- Risk classification
- Confidence scoring
- Human-in-the-loop review
- Escalation logic
- Responsible AI thinking

Related files:

```text
app/nodes/risk_checker.py
app/nodes/confidence_checker.py
app/nodes/human_review.py
app/nodes/hitl_action.py
```

## How State Works

The shared state is defined in `app/state.py`.

Each node receives the same `AgentState`, updates part of it, and returns it to the graph.

Important state fields include:

```text
user_query              # Original user question
request_type            # faq, emergency, or medical_info
selected_tool           # retrieval, web_search, or none
tool_result             # Output from the selected tool
response                # Generated answer
validation_passed       # True or False
retry_count             # Number of failed validation attempts
risk_level              # low or high
confidence_score        # Simple score from 0 to 100
requires_human_review   # True when human review is needed
human_decision          # Human approval decision
escalation_action       # Simulated action after review
```

This is one of the most important concepts in the project. State is how the workflow remembers what happened at each step.

## Tools Used by the Agent

### Retrieval Tool

The retrieval tool reads from:

```text
app/data/hospital_policies.txt
```

It is useful for questions such as:

```text
What are the hospital visiting hours?
What documents are needed for admission?
Can family members visit the ICU?
How can I book an appointment?
```

### Web Search Tool

The web search tool uses Tavily search through:

```text
app/tools/web_search_tool.py
```

It is useful for general medical information questions such as:

```text
What are common dengue symptoms?
What are common diabetes symptoms?
```

The responder is instructed not to provide a diagnosis. It should only use the tool result and keep the answer short.

## Setup

### 1. Create a virtual environment

```powershell
python -m venv .venv
```

### 2. Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

The current code also imports Tavily:

```python
from tavily import TavilyClient
```

If Tavily is not already installed in your environment, install it with:

```powershell
pip install tavily-python
```

### 4. Create a `.env` file

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

`GEMINI_API_KEY` is required for the LLM calls.

`TAVILY_API_KEY` is required when the agent chooses the web search tool.

## How to Run

From the project root, run:

```powershell
python -m app.main
```

Then enter a query when prompted.

Example:

```text
Enter your query: What are the visiting hours?
```

The program prints the internal workflow result:

```text
Request Type
Risk Level
Tool Used
Confidence Score
Validation Passed
Retry Count
Human Review Required
Response
```

This output is useful for learning because students can see what the agent decided at each stage.

## Demo Queries

Try these examples:

```text
What are the hospital visiting hours?
```

Expected idea:

- The request should be treated like an FAQ.
- The retrieval tool should be useful.
- The response should come from the hospital policy file.

```text
What documents do I need for admission?
```

Expected idea:

- The retrieval tool should find admission requirements.

```text
What are dengue symptoms?
```

Expected idea:

- The web search tool may be selected.
- Tavily API access is needed.
- The response should avoid giving a diagnosis.

```text
I have chest pain and cannot breathe
```

Expected idea:

- The risk checker should mark the query as high risk.
- The graph should route to human review.
- The program will ask for human approval.
- The final response will be a simulated escalation action.

## Human-in-the-Loop Example

For a high-risk query, the system prints:

```text
HUMAN REVIEW REQUIRED
```

Then it asks:

```text
Approve emergency escalation? (yes/no):
```

This is a teaching simulation. It shows how a system can pause and ask a human before taking an important action.

## Validation and Retry Logic

Validation happens in:

```text
app/nodes/validator.py
```

The validator checks:

- Was a tool result produced?
- Did the tool return an error?
- Was a response generated?
- Is the response too short?

If validation fails, the graph retries the response generation.

The retry limit is defined in:

```text
app/graph.py
```

```python
MAX_RETRIES = 2
```

If validation still fails after the retry limit, the graph routes to human review.

## Confidence Logic

Confidence is calculated in:

```text
app/nodes/confidence_checker.py
```

The current version uses a simple teaching rule:

- Tool result exists: +30
- Response exists: +30
- Validation passed: +40

This creates a score out of 100.

If confidence is below 70, the graph routes to human review.

This is intentionally simple so students can understand the concept before building more advanced scoring.

## Important Safety Note

This project is only for learning agentic AI concepts.

It does not:

- Diagnose patients
- Replace doctors
- Make real emergency decisions
- Guarantee medical accuracy
- Provide production-grade safety, privacy, logging, security, or compliance

For real medical concerns, users should contact qualified medical professionals or emergency services.

## Ideas for Student Extensions

Students can build similar projects by changing the domain and tools.

Example project ideas:

- University student support agent
- Library helpdesk agent
- Banking FAQ and escalation agent
- Travel booking support agent
- HR policy support agent
- IT helpdesk troubleshooting agent

Possible improvements:

- Add a planner node
- Add better semantic validation
- Store conversation history
- Add a database tool
- Add structured JSON outputs
- Add tests for each node
- Add a web UI
- Replace keyword risk checks with an LLM-based risk classifier
- Add logs showing every state transition
- Add graph visualization

## Final Deliverables Covered

This project demonstrates the main deliverables from the 3-week training plan:

- Workflow diagram
- LangGraph implementation
- State definition
- Classifier node
- Tool decision node
- Tool execution node
- Response generation node
- Validation node
- Retry logic
- Risk check node
- Confidence check node
- Human review routing
- Demo inputs and outputs

## Quick Reference

Run the project:

```powershell
python -m app.main
```

Main workflow:

```text
app/graph.py
```

Shared state:

```text
app/state.py
```

Local hospital data:

```text
app/data/hospital_policies.txt
```

Start reading from:

```text
app/main.py
```

Then follow the graph in:

```text
app/graph.py
```


### GitHub repo link - https://github.com/codezelaca/ai-hospital-assistant-agent