# Multi-Agent AI System

Multi-agent AI system built in Python to explore collaborative agent workflows, authorization-aware task execution, and practical LLM orchestration.

This project focuses on how multiple agents can work together to solve tasks, route work between specialised roles, and operate with clearer control over permissions and responsibilities rather than relying on a single monolithic prompt.

## What This Project Demonstrates

- multi-agent workflow design
- task routing across specialised agents
- authorization-aware execution
- collaborative problem solving with LLMs
- structured orchestration in Python
- experimentation with agent responsibilities, delegation, and control

## Why This Project Matters

A lot of AI demos stop at a single chat interface. This project explores a more realistic system shape where:
- different agents are assigned different responsibilities
- work can be delegated across multiple stages
- agent actions can be constrained through authorizations
- orchestration logic is separated from individual prompts
- the system is easier to reason about, test, and extend

This is useful for real-world agentic systems where reliability, control, and task separation matter more than a single one-shot response.

## Core Ideas Explored

### Multi-Agent Collaboration
The project explores how multiple agents can cooperate on a shared task rather than relying on one general-purpose model call.

### Agent Specialisation
Each agent can be assigned a defined role, helping separate responsibilities such as planning, execution, validation, or refinement.

### Authorization and Control
A key part of the system is experimenting with authorization-aware agent behaviour so that actions and task handling can be constrained intentionally.

### Practical Orchestration
The project is built to better understand how routing, sequencing, and coordination affect output quality and system behaviour in agentic applications.

## What It Shows Recruiters

This project highlights hands-on work with:
- Python-based AI system design
- multi-agent orchestration concepts
- authorization-aware workflow logic
- prompt-driven task decomposition
- agent routing and coordination
- practical experimentation with applied AI systems

It also reflects an interest in building systems that are more structured, controllable, and production-relevant than simple single-prompt demos.

## Repository Contents

- `agents.ipynb` — main notebook containing the multi-agent workflow logic and experimentation
- supporting code and configuration as the project evolves

## Current Focus

This project is part of a broader body of work around:
- agentic AI systems
- RAG and tool-connected workflows
- evaluation and observability
- production-minded AI engineering
- full-stack and backend AI delivery

## Future Improvements

Planned areas for extension include:
- clearer modularisation beyond notebook form
- reusable agent interfaces
- stronger evaluation of agent outputs
- better observability and traceability
- API or app layer for easier interaction
- richer authorization and workflow policies
