<div align="center">

# Universal Multi-Agent Simulation Engine

[English](README.md) | [繁體中文](README.zh-TW.md)

**A scalable framework for building large-scale simulations with your own agents, memory systems, models, and tools.**

![License](https://img.shields.io/badge/license-MIT-black)
![Status](https://img.shields.io/badge/status-research%20framework-blue)
![Architecture](https://img.shields.io/badge/architecture-layered-green)
![Simulation](https://img.shields.io/badge/focus-multi--agent-purple)

</div>

---

## Overview

Universal Multi-Agent Simulation Engine is a domain-agnostic framework for building large-scale simulation systems without forcing you into a single agent stack.

It is designed for teams working on synthetic societies, economic systems, game worlds, policy simulation, and other environments where different entities should operate at different levels of fidelity.

Instead of giving every agent the same reasoning budget, this framework organizes populations into layers and routes compute where it matters most.

---

## Demo Preview

### Architecture Snapshot

![Architecture Overview](assets/architecture-overview.png)

> Replace `assets/architecture-overview.png` with your main public-facing architecture image.

### Simulation Demo

![Simulation Demo](assets/demo-simulation.gif)

> Replace `assets/demo-simulation.gif` with a short GIF showing a running simulation, dashboard update, or agent interaction loop.

### Screenshots

<p align="center">
  <img src="assets/screenshot-dashboard.png" alt="Simulation dashboard" width="31%" />
  <img src="assets/screenshot-population.png" alt="Population view" width="31%" />
  <img src="assets/screenshot-timeline.png" alt="Timeline and replay view" width="31%" />
</p>

> Suggested screenshots:
> - `assets/screenshot-dashboard.png`: main simulation dashboard
> - `assets/screenshot-population.png`: layered population or agent state view
> - `assets/screenshot-timeline.png`: event timeline, replay, or evaluation panel

### Runtime Flow

```text
Your Agents / Custom Agent Stack / Tool Agents
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

---

## Why this repository exists

Most multi-agent demos look impressive at small scale but become expensive and difficult to extend once the number of entities grows.

This repository focuses on a more practical goal: building simulation systems that remain expressive while scaling to much larger populations.

The core idea is simple:

- keep high-fidelity reasoning for the agents that matter most
- use lighter abstractions for the middle of the population
- compress the long tail into archetypes and statistical groups
- reuse memory and cached behavior whenever possible
- integrate existing agent systems through adapters

---

## Features

- Layered population architecture for mixing detailed agents with large synthetic populations
- Adapter-first design for integrating your own agents, tools, and model providers
- Cost-aware routing for deciding when deeper reasoning is actually worth it
- Hierarchical memory and semantic cache patterns for long-running simulations
- Research-friendly structure for experimentation, benchmarking, and extension
- Domain-agnostic design for social, economic, strategic, and game simulations

---

## Use Cases

### Synthetic societies
Model institutions, social norms, group behavior, and emergence over time.

### Economic simulations
Represent consumers, firms, traders, shocks, and macro-micro feedback loops.

### Game worlds and NPC systems
Support living environments where only a subset of characters need full cognition.

### Policy and epidemiology
Explore intervention effects, behavior shifts, diffusion, and downstream outcomes.

### Agent infrastructure research
Test memory, routing, compression, and scalable simulation strategies.

---

## Bring Your Own Agents

This framework is meant to work with the systems you already have.

You can connect:

- LLM agents
- tool-using agents
- workflow agents
- retrieval-based agents
- rule-based agents
- custom memory systems
- external orchestration layers

The goal is to standardize the simulation boundary, not to replace your entire stack.

---

## Minimal Adapter Interface

```python
class AgentAdapter:
    def act(self, observation: dict, context: dict) -> dict:
        raise NotImplementedError

    def update_memory(self, event: dict) -> None:
        raise NotImplementedError

    def importance_score(self) -> float:
        raise NotImplementedError
```

---

## Repository Structure

- `docs/whitepaper.md` - full whitepaper and architectural rationale
- `docs/framework-overview.md` - concise overview of the framework
- `docs/integration-guide.md` - guide for connecting your own agents
- `src/` - framework skeleton and core abstractions
- `examples/` - minimal demos and integration examples

---

## Quick Start

```bash
git clone https://github.com/your-name/universal-multi-agent-simulation-engine.git
cd universal-multi-agent-simulation-engine
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python examples/minimal_simulation.py
```

---

## Roadmap

- [ ] Add public architecture diagram
- [ ] Add minimal runnable simulation example
- [ ] Add benchmark table for fidelity vs cost
- [ ] Add evaluation and replay examples
- [ ] Add reference adapters for external agent stacks

---

## Documentation

- Framework overview: `docs/framework-overview.md`
- Whitepaper: `docs/whitepaper.md`
- Integration guide: `docs/integration-guide.md`

---

## Citation

If you use this project in research or system design, please cite the whitepaper in `docs/whitepaper.md`.

---

## License

MIT
