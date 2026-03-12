<div align="center">

# Universal Multi-Agent Simulation Engine
[English](README.md) | [繁體中文](README.zh-TW.md)

**A scalable architecture for building large-scale simulations with layered agents, routing, memory compression, and adapter-based integration.**

![License](https://img.shields.io/badge/license-MIT-black)
![Status](https://img.shields.io/badge/status-open%20architecture-blue)
![Architecture](https://img.shields.io/badge/architecture-layered-green)
![Simulation](https://img.shields.io/badge/focus-multi--agent-purple)

</div>

---

## Overview

Universal Multi-Agent Simulation Engine is an open architecture for teams that want to build large-scale simulations without forcing every entity to run the same reasoning stack.

It is designed for synthetic societies, economic systems, game worlds, policy models, and other environments where only a subset of agents need deep cognition while the rest should remain cheap, scalable, and structurally consistent.

The framework combines four ideas:

- layered population modeling
- cost-aware routing
- hierarchical memory
- adapter-based integration with your existing agents

---

## Architecture Snapshot

### Public Architecture Diagram

![Architecture Overview](assets/architecture-overview.png)

For a more detailed systems view, see `assets/architecture-detail.png`.

`assets/architecture-overview.png` is the main public-facing diagram for the repository. It should present the full stack from external agents and adapters down to runtime orchestration and the four-layer population model.

### Reference Runtime Flow

```text
Your Agents / External Agent Stack / Tool Agents
                    |
                    v
          Adapter Interface Layer
                    |
                    v
          Simulation Runtime Core
      - world engine
      - event scheduler
      - model router
      - memory manager
      - semantic cache
                    |
                    v
      Four-Layer Population Architecture
      - Layer 1: key individual agents
      - Layer 2: templated adaptive agents
      - Layer 3: archetype groups
      - Layer 4: macro statistical population
                    |
                    v
          Logging / Replay / Evaluation
```

### Demo and Screenshots

![Simulation Demo](assets/demo-simulation.gif)

<p align="center">
  <img src="assets/screenshot-dashboard.png" alt="Simulation dashboard" width="31%" />
  <img src="assets/screenshot-population.png" alt="Population view" width="31%" />
  <img src="assets/screenshot-timeline.png" alt="Timeline and replay view" width="31%" />
</p>

Use the `assets/` directory for polished public visuals. The current repository includes placeholders so the structure is ready for diagrams, GIFs, and screenshots.

---

## Why this repository exists

Most multi-agent demos look impressive at small scale but become expensive, rigid, or difficult to interpret once the number of entities grows.

This repository focuses on a more practical goal: providing a general architecture that separates who needs deep cognition, who can be approximated, how memory should be compressed, and how different agent frameworks can plug into the same simulation backbone.

This makes it easier to prototype:

- persistent world simulations
- synthetic organizations
- market and policy experiments
- education and training sandboxes
- city-scale digital twins

---

## Core design principles

### 1. Population should not be uniformly expensive
A realistic simulation may contain millions of entities, but only a very small subset should run high-cost reasoning at any given time.

### 2. Memory should be layered
Not every event deserves full retention. Episodic traces, summaries, long-term traits, and world-level aggregates should live at different resolutions.

### 3. Coordination needs explicit runtime services
Scheduling, event propagation, tool access, replay, observability, and model routing should live in system infrastructure, not be hidden inside each individual agent.

### 4. Integration should be adapter-first
The architecture should support plugging in existing LLM agents, rule systems, retrieval pipelines, reinforcement learners, and human-in-the-loop workflows.

---

## Repository structure

```text
/assets          public diagrams, GIFs, screenshots
/docs            whitepaper, framework overview, integration guide
/examples        example scenarios and simulation templates
```

---

## Included documents

- `docs/whitepaper.md` - conceptual overview and design thesis
- `docs/framework-overview.md` - system structure and major modules
- `docs/integration-guide.md` - how to connect external agents and tools
- `README.zh-TW.md` - Traditional Chinese version of the main README

---

## License

MIT License
