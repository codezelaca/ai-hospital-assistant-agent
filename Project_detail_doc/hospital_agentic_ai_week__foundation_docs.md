# Hospital Support & Triage Agent System

# Project Overview

---

# 1. Introduction

The Hospital Support & Triage Agent System is a domain-specific agentic AI project designed to demonstrate how modern AI systems can move beyond simple chatbot behavior.

Instead of directly answering every user query, the system follows a structured workflow:

1. Understand the user request
2. Classify the request type
3. Create a plan
4. Decide how the request should be handled
5. Generate a response
6. Escalate risky situations when necessary

This project is intentionally focused on the healthcare support domain because:

- the domain is easy to understand
- workflow decisions are realistic
- human review naturally makes sense
- risk handling becomes meaningful
- students can clearly understand why workflows are needed

The system is NOT designed to replace doctors.

The system acts as a hospital support assistant that helps with:

- hospital information
- symptom guidance
- policy retrieval
- emergency escalation
- safe response generation

---

# 2. Why We Need Agentic AI

A normal LLM chatbot works like this:

```text
User Query
↓
LLM
↓
Answer
```

This approach has several problems.

---

## Problem 1 — The LLM May Give Wrong Answers

Example:

```text
User: "I have chest pain and breathing difficulty"
```

A normal chatbot may generate unsafe medical advice.

This is dangerous.

---

## Problem 2 — The LLM May Not Understand the Request Type

Example:

```text
"What are visiting hours?"
```

This is a hospital FAQ.

But:

```text
"I accidentally overdosed on medicine"
```

This is a high-risk emergency query.

Both queries should NOT be handled the same way.

---

## Problem 3 — The LLM May Not Use Project-Specific Data

Example:

```text
"What documents are required for surgery admission?"
```

The answer depends on the hospital’s internal policy.

A general LLM may hallucinate information.

---

## Problem 4 — The LLM Does Not Know When to Use Tools

Example:

```text
"What are dengue symptoms?"
```

The system may need external medical information.

A workflow system can decide:

- use hospital documents
- use web search
- answer directly

---

## Problem 5 — The LLM Does Not Validate Its Own Output

The generated answer may:

- miss important details
- contain incorrect information
- contain unsupported claims
- fail to answer the actual question

---

## Problem 6 — The LLM Does Not Know When to Escalate

Example:

```text
"My child is unconscious"
```

The system should not continue normal conversation.

The system should:

- detect high risk
- avoid unsafe guidance
- escalate immediately

---

# 3. What Is Agentic AI?

Agentic AI is an AI system that follows a workflow and makes decisions step by step.

Instead of only generating answers, the system:

- understands tasks
- makes decisions
- routes requests
- uses tools
- validates outputs
- handles failures
- escalates risky situations

---

# Chatbot vs Agentic System

| Chatbot | Agentic System |
|---|---|
| Direct answer generation | Workflow-based execution |
| One-step interaction | Multi-step decision process |
| No workflow state | Shared workflow state |
| Limited reliability | Controlled execution |
| No tool orchestration | Conditional tool usage |
| No escalation awareness | Human review support |

---

# Example Comparison

## Traditional Chatbot

```text
User: "I have chest pain"
↓
LLM generates answer
```

---

## Agentic Workflow

```text
User Query
↓
Risk Classification
↓
High-Risk Detection
↓
Create Escalation Plan
↓
Generate Safe Response
↓
Recommend Immediate Medical Attention
```

---

# 4. Project Scope

The system supports:

- hospital FAQs
- admission information
- symptom guidance
- hospital policies
- emergency risk detection
- medical information lookup
- escalation handling

The system does NOT:

- diagnose diseases
- prescribe medicine
- replace doctors
- make autonomous medical decisions

---

# 5. Tools Used in the Project

The project intentionally uses only a few tools to keep the workflow understandable.

| Tool | Purpose |
|---|---|
| LLM | General response generation |
| Retrieval Tool | Internal hospital document lookup |
| Web Search Tool | External medical information |

---

# 6. High-Level Workflow

```text
User Query
↓
Classify Request
↓
Risk Check
↓
Decide Tool
↓
Tool Execution
↓
Generate Response
↓
Validation
↓
Retry if Needed
↓
Final Response OR Human Review
```

---

# 7. 3-Week Plan

| Week | Focus |
|---|---|
| Week 1 | Basic workflow, classification, planning |
| Week 2 | Tool usage, validation, retry logic |
| Week 3 | Risk handling, HITL, frontend integration |

---

# WEEK 1 THEORY GUIDE

---

# 1. What Is an LLM?

A Large Language Model (LLM) is an AI model trained on large amounts of text data.

LLMs can:

- answer questions
- summarize text
- generate content
- classify information
- follow instructions

Examples:

- GPT models
- Claude
- Gemini

---

# In Our Project

The LLM helps:

- classify hospital-related queries
- create plans
- generate draft responses

Example:

```text
User: "What are dengue symptoms?"
```

The LLM can:

- understand the query
- identify the topic
- generate a draft answer

---

# 2. What Is a Chatbot?

A chatbot is a system that directly generates responses from user input.

Basic chatbot workflow:

```text
User Query
↓
LLM
↓
Response
```

---

# Problem With Simple Chatbots

Simple chatbots:

- may hallucinate
- may ignore project data
- may not validate outputs
- may not detect risk
- may not know when to escalate

---

# In Our Project

Example:

```text
"I accidentally consumed too much medicine"
```

A simple chatbot may continue normal conversation.

This is unsafe.

---

# 3. Why Agentic AI Exists

Agentic AI exists because:

- LLMs alone are unreliable
- workflows improve control
- systems need decision-making
- tools must be used conditionally
- risky situations require escalation

---

# In Our Project

The system must decide:

- Is this query risky?
- Should web search be used?
- Should retrieval be used?
- Should this be escalated?

This requires workflow-based thinking.

---

# 4. What Is a Workflow?

A workflow is a sequence of controlled steps.

Instead of directly generating an answer, the system performs tasks step by step.

---

# In Our Project

Example workflow:

```text
User Query
↓
Classify Request
↓
Create Plan
↓
Generate Draft Response
```

---

# 5. What Is State?

State is shared information passed between workflow steps.

Each node can:

- read state
- update state
- pass state forward

---

# In Our Project

Example state:

```python
{
    "user_query": "I have chest pain",
    "request_type": "high_risk",
    "risk_level": "high",
    "plan": "Escalate immediately",
    "draft_response": "Please seek emergency care"
}
```

---

# Why State Matters

Without state:

- nodes cannot share information
- workflows become disconnected
- routing becomes difficult

---

# 6. What Is a Node?

A node is a single workflow step.

Each node performs one responsibility.

---

# In Our Project

Examples:

| Node | Responsibility |
|---|---|
| Classifier Node | Identify request type |
| Planner Node | Create response plan |
| Response Node | Generate draft response |

---

# 7. What Is an Edge?

An edge connects workflow nodes.

Edges define:

- execution flow
- node transitions
- workflow direction

---

# In Our Project

Example:

```text
Classifier Node
↓
Planner Node
↓
Response Node
```

The arrows represent edges.

---

# 8. What Is Conditional Routing?

Conditional routing means the system chooses different paths based on conditions.

---

# In Our Project

Example:

```text
If request is high-risk
→ escalate

If request is FAQ
→ generate response
```

Different conditions create different workflow paths.

---

# 9. What Is Planning?

Planning means deciding what steps should happen before generating the final response.

---

# In Our Project

Example:

User Query:

```text
"I have chest pain"
```

Possible plan:

1. Detect high risk
2. Avoid diagnosis
3. Recommend emergency care
4. Escalate for human review

---

# 10. Week 1 Workflow

This week we only build the first minimal workflow.

---

# Week 1 Goal

Build:

```text
User Query
↓
Classify Request
↓
Create Plan
↓
Generate Draft Response
```

No tools yet.

No validation yet.

No retry logic yet.

No human review yet.

These will be added in later weeks.

---

# 11. Week 1 Expected Output

By the end of Week 1, interns should understand:

- why simple chatbots are insufficient
- why workflows matter
- how state works
- how nodes work
- how routing works
- how planning works
- how LangGraph workflows are structured

They should also build:

- a basic LangGraph workflow
- request classification
- planning node
- draft response generation

---

# 12. Important Learning Objective

The most important idea in Week 1 is:

```text
Agentic AI is not just an LLM with prompts.

Agentic AI is a workflow system that controls how the LLM behaves.
```

