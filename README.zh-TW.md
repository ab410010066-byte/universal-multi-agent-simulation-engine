<div align="center">

# Universal Multi-Agent Simulation Engine

[English](README.md) | [繁體中文](README.zh-TW.md)

**一個可整合自有 agents、記憶系統、模型與工具的大規模模擬框架。**

![License](https://img.shields.io/badge/license-MIT-black)
![Status](https://img.shields.io/badge/status-research%20framework-blue)
![Architecture](https://img.shields.io/badge/architecture-layered-green)
![Simulation](https://img.shields.io/badge/focus-multi--agent-purple)

</div>

---

## 專案概覽

Universal Multi-Agent Simulation Engine 是一個通用型的大規模模擬框架，目標是在不綁定單一 agent stack 的前提下，協助你建立可延展的多 Agent 模擬系統。

它適合用在合成社會、經濟系統、遊戲世界、政策模擬，以及任何需要讓不同實體以不同保真度運作的場景。

這個框架的核心不是讓每個 Agent 都使用相同等級的推理，而是把算力分配到真正重要的地方。

---

## Demo Preview

### 架構預覽圖

![Architecture Overview](assets/architecture-overview.png)

> 之後把 `assets/architecture-overview.png` 換成你的公開版主架構圖即可。

### 模擬 Demo

![Simulation Demo](assets/demo-simulation.gif)

> 之後把 `assets/demo-simulation.gif` 換成一段短 GIF，展示模擬執行、dashboard 更新，或 agent 互動流程。

### Screenshots

<p align="center">
  <img src="assets/screenshot-dashboard.png" alt="Simulation dashboard" width="31%" />
  <img src="assets/screenshot-population.png" alt="Population view" width="31%" />
  <img src="assets/screenshot-timeline.png" alt="Timeline and replay view" width="31%" />
</p>

> 建議畫面:
> - `assets/screenshot-dashboard.png`: 主 simulation dashboard
> - `assets/screenshot-population.png`: 分層人口或 agent 狀態畫面
> - `assets/screenshot-timeline.png`: event timeline、replay 或 evaluation 面板

### Runtime Flow

```text
你的 Agents / 自定義 Agent Stack / 工具型 Agents
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
          - Layer 1: 關鍵個體 agents
          - Layer 2: 模板化自適應 agents
          - Layer 3: 原型群組
          - Layer 4: 統計型宏觀人口
                      |
                      v
              Logging / Replay / Evaluation
```

---

## 為什麼做這個專案

很多多 Agent 專案在小規模 demo 時看起來很吸引人，但一旦實體數量上升，成本、複雜度與可維護性問題就會快速出現。

這個專案聚焦的是更務實的目標: 在維持表現力的同時，把模擬系統擴展到更大的群體規模。

核心想法很簡單:

- 只讓真正重要的 agents 使用高保真推理
- 用較輕量的抽象處理中層人口
- 把長尾群體壓縮成原型與統計群組
- 盡量重用記憶與已快取的行為
- 透過 adapters 接入你既有的 agent 系統

---

## 核心特色

- 分層人口架構，可同時容納高細節 agents 與大規模合成人口
- adapter-first 設計，可整合你自己的 agents、tools 與 model providers
- 成本感知路由，決定什麼時候值得使用更深層推理
- 階層式記憶與 semantic cache 模式，適合長時間模擬
- 便於研究、實驗、benchmark 與延展的專案結構
- 適用於社會、經濟、策略與遊戲等多種模擬場景

---

## 適用場景

### 合成社會
模擬制度、社會規範、群體互動與湧現過程。

### 經濟模擬
表示消費者、企業、交易者、衝擊事件與總體-微觀回饋。

### 遊戲世界與 NPC 系統
建立活的環境，讓只有一部分角色需要完整認知能力。

### 政策與流行病學
探索介入策略、行為變化、擴散過程與後續效果。

### Agent 基礎設施研究
測試記憶、路由、壓縮與可擴展模擬策略。

---

## Bring Your Own Agents

這個框架的設計前提，就是能與你已經存在的系統協作。

你可以接入:

- LLM agents
- tool-using agents
- workflow agents
- retrieval-based agents
- rule-based agents
- 自訂記憶系統
- 外部 orchestration layers

這套框架想標準化的是模擬邊界，而不是取代你的整個 stack。

---

## 最小 Adapter 介面

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

- `docs/whitepaper.md` - 完整白皮書與架構動機
- `docs/framework-overview.md` - 框架總覽
- `docs/integration-guide.md` - 接入自有 agents 的整合指南
- `src/` - 框架骨架與核心抽象
- `examples/` - 最小 demo 與整合範例

---

## 快速開始

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

- [ ] 補上公開版架構圖
- [ ] 補上最小可執行模擬範例
- [ ] 補上 fidelity 與成本的 benchmark 表格
- [ ] 補上 evaluation 與 replay 範例
- [ ] 補上外部 agent stacks 的參考 adapters

---

## 文件導覽

- Framework overview: `docs/framework-overview.md`
- Whitepaper: `docs/whitepaper.md`
- Integration guide: `docs/integration-guide.md`

---

## 引用

如果你在研究或系統設計中使用本專案，請引用 `docs/whitepaper.md` 中的白皮書內容。

---

## License

MIT
