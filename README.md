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

This repository focuses on a more practical goal: preserving realism where it matters while scaling to much larger populations through selective intelligence allocation.

That means:

- high-fidelity reasoning for critical agents
- lightweight templates for recurring roles
- archetype diffusion for representative groups
- macro statistical simulation for the long tail
- memory compression and semantic reuse to reduce waste

---

## Core Concepts

### 1. Layered population architecture
Not every entity should be modeled with the same reasoning depth. The system separates the population into four layers so fidelity can be concentrated where it matters most.

### 2. Cost-aware routing
The runtime should decide when full reasoning is worth paying for based on importance, event criticality, and expected downstream impact.

### 3. Hierarchical memory
Long-running simulations need more than raw transcripts. Working memory, episodic summaries, and compressed long-term state make simulations more stable.

### 4. Adapter-first integration
The framework standardizes the simulation boundary so you can plug in your own agents, tools, models, and memory backends without rebuilding everything.

---

## Features

- Four-layer population model for scaling beyond small demo populations
- Adapter interfaces for integrating custom agents and orchestration stacks
- Model routing for selective reasoning allocation
- Hierarchical memory and semantic cache patterns
- Research-friendly structure for benchmarking and experimentation
- Domain-agnostic design for social, economic, strategic, and game simulations

---

## Use Cases

- Synthetic societies and institutional behavior
- Macro and micro market simulations
- Game worlds and scalable NPC ecosystems
- Policy, contagion, and intervention modeling
- Agent infrastructure research and benchmarking

---

## Repository Structure

```text
assets/      public diagrams, GIFs, screenshots, and brand assets
examples/    minimal simulations and adapter examples
src/         framework skeleton and core abstractions
docs/        whitepaper, architecture notes, and integration guidance
```

### Key files

- `docs/whitepaper.md` - full thesis and architectural rationale
- `docs/framework-overview.md` - concise framework summary
- `docs/integration-guide.md` - how to connect your own agents
- `src/universal_multi_agent_sim/` - starter package layout
- `examples/minimal_simulation.py` - small end-to-end example

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

## Implementation Roadmap

- [x] Publish architecture documents and public repository structure
- [x] Add starter `assets/`, `src/`, and `examples/` directories
- [ ] Add final public diagrams and real product screenshots
- [ ] Add benchmark tables for fidelity versus cost
- [ ] Add replay, evaluation, and observability examples
- [ ] Add reference adapters for external agent stacks

---

## Quick Start

```bash
git clone https://github.com/ab410010066-byte/universal-multi-agent-simulation-engine.git
cd universal-multi-agent-simulation-engine
python -m venv .venv
source .venv/bin/activate
PYTHONPATH=src python examples/minimal_simulation.py
```

---

## Documentation

- Framework overview: `docs/framework-overview.md`
- Whitepaper: `docs/whitepaper.md`
- Integration guide: `docs/integration-guide.md`

---

## License

MIT
