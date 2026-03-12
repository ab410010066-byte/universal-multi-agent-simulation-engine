from universal_multi_agent_sim import AgentAdapter, RoutingPolicy, SimulationEngine


class DemoAgent(AgentAdapter):
    def __init__(self, name: str, importance: float) -> None:
        self.name = name
        self._importance = importance
        self.memory = []

    def act(self, observation, context):
        return {
            "agent": self.name,
            "selected_tier": context["selected_tier"],
            "decision": f"respond_to_{observation['event']}"
        }

    def update_memory(self, event):
        self.memory.append(event)

    def importance_score(self) -> float:
        return self._importance


if __name__ == "__main__":
    routing = RoutingPolicy(high_fidelity_threshold=0.75, medium_fidelity_threshold=0.35)
    engine = SimulationEngine(routing_policy=routing)

    agents = [
        DemoAgent(name="mayor", importance=0.95),
        DemoAgent(name="merchant", importance=0.55),
        DemoAgent(name="resident_cluster", importance=0.20),
    ]

    actions = engine.step(
        agents=agents,
        observation={"event": "market_shock"},
        context={"tick": 1, "world": "demo_city"},
    )

    for action in actions:
        print(action)
