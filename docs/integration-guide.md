# Integration Guide

This guide shows how to connect your own agents to the framework.

## Integration principle

The runtime should not care whether an agent comes from AgentScope, LangGraph, AutoGen, CrewAI, a custom Python class, or an internal orchestration platform. It only needs a stable adapter contract.

## Minimum adapter contract

```python
class AgentAdapter:
    def act(self, observation: dict, context: dict) -> dict:
        ...

    def update_memory(self, event: dict) -> None:
        ...

    def importance_score(self) -> float:
        ...
```

## What your adapter should provide

- A way to receive world observations
- A way to produce a structured action
- A way to update or compress memory
- A way to expose importance or priority
- Optional metadata such as role, archetype, cost tier, and tool access

## Adapter examples

### Example 1: wrapping a custom Python agent

```python
class MyCustomAdapter(AgentAdapter):
    def __init__(self, agent):
        self.agent = agent

    def act(self, observation, context):
        return self.agent.run(observation=observation, context=context)

    def update_memory(self, event):
        self.agent.memory.append(event)

    def importance_score(self):
        return getattr(self.agent, "importance", 0.5)
```

### Example 2: wrapping a workflow-based agent

Use the adapter to translate between the framework's structured simulation events and your workflow engine's input and output schema.

## Routing guidance

Use routing rules to decide when to invoke:

- full reasoning
- lightweight reasoning
- batch prompting
- archetype diffusion
- non-LLM statistical updates

## Memory guidance

For long-running simulations, do not keep raw event history forever. Use layered memory:

- working memory for the current step
- episodic memory for recent meaningful events
- semantic summaries for long-term state
- archetype memory for shared group behavior

## Tool integration

You can expose tools selectively by role. For example:

- leaders get planning tools
- traders get market tools
- civilians get no external tools
- coordinators get world-state access

## Recommended first milestone

Before building a huge world, prove one full loop:

1. observe world state
2. route to the right reasoning tier
3. generate structured action
4. update memory
5. commit world changes

If that loop works, scaling becomes an engineering problem instead of a conceptual one.
