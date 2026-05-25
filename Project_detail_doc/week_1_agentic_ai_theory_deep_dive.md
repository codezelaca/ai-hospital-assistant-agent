# Week 1 — From LLM to Agentic Workflow

# Detailed Theory Guide

---

# 1. Introduction

In this week, we focus on understanding:

- why simple chatbot systems are limited
- why modern AI systems need workflows
- how agentic AI systems work
- how workflows improve reliability and control

We will use our project:

# Hospital Support & Triage Agent System

throughout all explanations.

This is important because learning abstract concepts without a real project often becomes confusing.

---

# 2. Understanding the Core Problem

Before learning Agentic AI, we must first understand the limitations of normal LLM-based systems.

---

# Traditional Chatbot Architecture

A basic chatbot works like this:

```text
User Query
↓
LLM
↓
Generated Response
```

The user asks a question.

The LLM immediately generates a response.

This architecture is simple.

But real-world systems become much more complicated.

---

# Example 1 — Simple Question

```text
User: "What are visiting hours?"
```

A chatbot may answer correctly.

This is a low-risk FAQ question.

---

# Example 2 — Risky Question

```text
User: "I have severe chest pain and difficulty breathing"
```

Now the situation changes.

A chatbot may:

- hallucinate medical advice
- give incomplete guidance
- fail to recognize emergency risk
- continue normal conversation

This is dangerous.

---

# Key Learning Point

Not all requests should be handled the same way.

Different requests require:

- different decisions
- different workflows
- different safety rules
- different response strategies

This is one of the main reasons Agentic AI exists.

---

# 3. What Is an LLM?

LLM stands for:

# Large Language Model

An LLM is an AI model trained using massive amounts of text data.

LLMs learn:

- language patterns
- reasoning patterns
- sentence structures
- relationships between words

Examples:

- GPT models
- Claude
- Gemini

---

# What LLMs Are Good At

LLMs are very good at:

- generating text
- answering questions
- summarizing content
- classifying information
- understanding instructions

---

# What LLMs Are NOT Good At

LLMs are NOT naturally reliable.

They may:

- hallucinate information
- generate inconsistent outputs
- ignore project-specific rules
- fail to validate responses
- fail to detect dangerous situations

---

# In Our Project

Example:

```text
"My child swallowed unknown medicine"
```

A raw LLM may generate unsafe medical guidance.

A reliable system should instead:

- detect emergency risk
- avoid diagnosis
- recommend immediate emergency help
- escalate for human review

---

# 4. What Is a Chatbot?

A chatbot is a conversational AI system that directly generates responses.

Most basic chatbot systems follow this architecture:

```text
User Input
↓
LLM
↓
Response
```

---

# Why Simple Chatbots Become a Problem

Simple chatbots:

- do not follow workflows
- do not validate outputs
- do not track state properly
- do not make structured decisions
- do not know when to escalate

---

# Example in Our Project

## Query 1

```text
"What are hospital visiting hours?"
```

This is safe.

---

## Query 2

```text
"I cannot breathe properly"
```

This is high-risk.

A normal chatbot may treat both queries similarly.

That is unsafe.

---

# Important Understanding

A chatbot mainly focuses on:

# generating text

An agentic system focuses on:

# making controlled decisions

This is the biggest difference.

---

# 5. Why Agentic AI Exists

Agentic AI exists because real-world AI systems need:

- reliability
- workflows
- decision-making
- safety
- tool usage
- validation
- escalation handling

---

# Agentic AI Definition

Agentic AI is a workflow-based AI system that performs tasks step by step.

Instead of directly generating a response, the system:

- understands the request
- makes decisions
- follows workflows
- uses tools when needed
- validates outputs
- handles failures
- escalates risky situations

---

# In Our Project

The system should decide:

| Question | Example |
|---|---|
| Is this risky? | chest pain |
| Is a tool needed? | hospital policy lookup |
| Is web search needed? | dengue symptoms |
| Should this be escalated? | overdose situation |
| Is the response safe? | emergency advice |

---

# 6. Chatbot vs Agentic System

| Chatbot | Agentic System |
|---|---|
| Direct answer generation | Workflow-based execution |
| Single-step reasoning | Multi-step orchestration |
| No workflow state | Shared workflow state |
| No routing | Conditional routing |
| No validation | Validation support |
| No escalation handling | HITL support |
| No workflow visibility | Observable execution |

---

# Example Comparison

## Chatbot

```text
User: "I accidentally overdosed"
↓
LLM generates answer
```

---

## Agentic Workflow

```text
User Query
↓
Risk Detection
↓
Emergency Classification
↓
Create Safe Plan
↓
Generate Escalation Response
↓
Recommend Emergency Services
```

---

# 7. What Is Workflow Thinking?

Workflow thinking means:

# solving problems step by step

Instead of asking the LLM to do everything at once.

---

# Bad Design

```text
"Classify the request, decide the risk, search documents, validate the answer, and generate the final response"
```

This overloads the LLM.

---

# Better Design

Break the system into separate workflow steps.

Example:

```text
User Query
↓
Classification
↓
Planning
↓
Response Generation
```

Each step has one responsibility.

This improves:

- reliability
- debugging
- maintainability
- observability

---

# In Our Project

The system should not immediately answer.

Instead:

1. Understand request type
2. Decide risk level
3. Create a response strategy
4. Generate a controlled response

---

# 8. What Is State?

State is shared information used throughout the workflow.

Each node can:

- read state
- update state
- pass updated state forward

---

# Why State Matters

Without state:

- nodes cannot communicate
- workflows lose context
- routing becomes difficult
- retries become impossible

---

# State in Our Project

Example state:

```python
{
    "user_query": "I have chest pain",
    "request_type": "medical_emergency",
    "risk_level": "high",
    "plan": "Escalate immediately",
    "draft_response": "Please seek immediate medical attention"
}
```

---

# Understanding State Flow

## Step 1 — User Query

```python
{
    "user_query": "I have chest pain"
}
```

---

## Step 2 — Classifier Updates State

```python
{
    "user_query": "I have chest pain",
    "request_type": "medical_emergency",
    "risk_level": "high"
}
```

---

## Step 3 — Planner Updates State

```python
{
    "user_query": "I have chest pain",
    "request_type": "medical_emergency",
    "risk_level": "high",
    "plan": "Escalate immediately"
}
```

---

# Key Understanding

State acts like:

# shared memory for the workflow

---

# 9. What Is a Node?

A node is a single workflow step.

Each node should perform:

# one clear responsibility

---

# Why Small Nodes Matter

Small focused nodes improve:

- debugging
- testing
- readability
- maintenance
- reliability

---

# In Our Project

Examples:

| Node | Responsibility |
|---|---|
| Classifier Node | classify request |
| Planner Node | create plan |
| Response Node | generate draft response |

---

# Example Node Execution

## Classifier Node Input

```python
{
    "user_query": "I have chest pain"
}
```

---

## Classifier Node Output

```python
{
    "request_type": "medical_emergency",
    "risk_level": "high"
}
```

---

# 10. What Is an Edge?

Edges connect workflow nodes.

Edges define:

- execution order
- workflow direction
- next step selection

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

The arrows are edges.

---

# Why Edges Matter

Edges allow workflows to become:

- structured
- observable
- controllable

Without edges:

- workflow execution becomes unclear
- routing becomes difficult

---

# 11. What Is Conditional Routing?

Conditional routing means:

# choosing different workflow paths based on conditions

---

# Example in Our Project

## Condition 1

```text
If request is FAQ
→ normal response flow
```

---

## Condition 2

```text
If request is high-risk
→ escalation flow
```

---

# Why Conditional Routing Matters

Not all requests should follow the same workflow.

Different situations require:

- different actions
- different tools
- different safety rules

---

# 12. What Is Planning?

Planning means:

# deciding what actions should happen before generating the final response

---

# Why Planning Matters

Without planning:

- responses become uncontrolled
- workflows become inconsistent
- risky situations may be mishandled

---

# Planning Example in Our Project

## User Query

```text
"I accidentally consumed too much medicine"
```

---

# Planner Output

```text
1. Detect emergency risk
2. Avoid diagnosis
3. Recommend emergency services
4. Escalate for human review
```

---

# Important Understanding

The planner does NOT generate the final response.

The planner creates:

# execution strategy

---

# 13. Week 1 Workflow Architecture

This week we intentionally keep the workflow simple.

---

# Week 1 Workflow

```text
User Query
↓
Classifier Node
↓
Planner Node
↓
Draft Response Node
```

---

# What Each Node Does

| Node | Responsibility |
|---|---|
| Classifier | identify request type |
| Planner | create response strategy |
| Response Generator | generate draft response |

---

# Why We Start Simple

Week 1 focuses on:

- workflow understanding
- state flow
- orchestration basics
- node design
- routing concepts

We intentionally avoid:

- tools
- validation
- retries
- HITL

These are introduced later.

---

# 14. Manual Workflow Walkthrough

Before coding, always understand the workflow logically.

---

# Example Query

```text
"I have severe chest pain"
```

---

# Step 1 — Classifier Node

The system identifies:

```text
request_type = emergency
risk_level = high
```

---

# Step 2 — Planner Node

The system creates a plan:

```text
1. Avoid diagnosis
2. Recommend emergency care
3. Generate safe response
```

---

# Step 3 — Draft Response Node

The system generates:

```text
"Please seek immediate emergency medical attention or contact emergency services immediately."
```

---

# Important Observation

The system did NOT:

- directly answer immediately
- randomly generate text
- skip risk handling

Instead:

# it followed a controlled workflow

---

# 15. Core Learning Objective of Week 1

The most important understanding from Week 1 is:

```text
Agentic AI is not just prompt engineering.

Agentic AI is workflow orchestration around LLM reasoning.
```

The workflow controls:

- what happens
- when it happens
- why it happens
- which path should be followed

This is the foundation of modern agentic AI systems.

