# feature-prioritization

A Python toolkit for scoring and ranking product features using **RICE** (Reach × Impact × Confidence / Effort) and **ICE** (Impact + Confidence + Ease) frameworks. Combine both signals into a single ranked backlog and identify which features to ship next.

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-pytest-orange)

---

## Features

- **RICE scoring** with tier classification (must-have / high / medium / low)
- **ICE scoring** for rapid, qualitative prioritisation
- **Combined ranker** — weighted blend of normalised RICE + ICE scores
- **Backlog detection** — identify features below a combined-score threshold
- **Text formatters** — ranked tables for roadmap reviews and stakeholder updates
- **JSON data format** — easy to integrate with Notion, Linear, or spreadsheet exports

---

## Scoring Frameworks

### RICE
```
RICE = (Reach × Impact × Confidence%) / Effort
```
| Field | Description | Example |
|---|---|---|
| `reach` | Users affected per month | `5000` |
| `impact` | 1 = minimal, 2 = medium, 3 = massive | `3` |
| `confidence` | % certainty in estimates | `80` |
| `effort` | Person-months to build | `2` |

### ICE
```
ICE = (Impact + Confidence + Ease) / 3
```
Each dimension scored 1–10.

---

## Installation

```bash
git clone https://github.com/MVP-03/feature-prioritization.git
cd feature-prioritization
python -m venv .venv && source .venv/bin/activate
pip install pytest
```

---

## Quick Start

```python
import json
from src.rice import rank_by_rice, rice_tier
from src.ranker import rank_features, top_features
from src.formatter import format_ranking, format_top_n

with open("data/features.json") as f:
    features = json.load(f)["features"]

# Pure RICE ranking
rice_ranked = rank_by_rice(features)
for f in rice_ranked[:3]:
    print(f"{f['name']:<25} RICE: {f['rice_score']:>8.1f}  [{rice_tier(f['rice_score'])}]")

# Combined RICE + ICE ranking
ranked = rank_features(features)
print(format_top_n(ranked, n=5))

# Backlog — features to defer
from src.ranker import backlog_candidates
deferred = backlog_candidates(features)
print(f"{len(deferred)} features moved to backlog")
```

**Sample output**
```
SSO / SAML            RICE:   6000.0  [must-have]
AI-generated summaries RICE:  2400.0  [high]
Bulk CSV export        RICE:  3200.0  [high]

Top 5 Features to Ship Next
========================================
1. SSO / SAML (RICE: 6000.0)
2. Bulk CSV export (RICE: 3200.0)
3. AI-generated summaries (RICE: 2400.0)
4. Dark mode (RICE: 7200.0)
5. Custom webhooks (RICE: 700.0)
```

---

## Data Format

```json
{
  "features": [
    {
      "name": "SSO / SAML",
      "reach": 5000,
      "impact": 3,
      "confidence": 90,
      "effort": 3,
      "ease": 5,
      "tags": ["enterprise", "auth"]
    }
  ]
}
```

---

## Project Structure

```
feature-prioritization/
├── src/
│   ├── rice.py        # RICE score, tier classification, ranking
│   ├── ice.py         # ICE score and RICE/ICE variance detection
│   ├── ranker.py      # combined ranker and backlog candidate filter
│   └── formatter.py   # ranked table and top-N text output
├── tests/
│   ├── test_rice.py
│   └── test_ranker.py
└── data/
    └── features.json
```

---

## Running Tests

```bash
python -m pytest tests/ -v
```

---

## When to use RICE vs ICE

| Situation | Recommended |
|---|---|
| You have quantitative data (traffic, user counts) | RICE |
| Early-stage / limited data | ICE |
| Stakeholder alignment session | ICE (fast, intuitive) |
| Engineering planning | RICE (accounts for effort) |
| Both available | Combined ranker |

---

## License

MIT
