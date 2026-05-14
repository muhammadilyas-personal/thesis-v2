# Thesis Results Tables

### Table 1 — Classified Data (Time, LOC, Assertions)
| Mode   |   Mean Time (min) |   LOC/Churn |   Mean Tests |   Mean Assertions |   Mean Iterations |
|:-------|------------------:|------------:|-------------:|------------------:|------------------:|
| Manual |              26.6 |        35.5 |          5.7 |               8.4 |              25.2 |
| AI-TDD |              13.7 |        15.6 |          4.1 |               5.2 |               5.7 |
| Hybrid |              18.8 |        23.4 |          6.7 |               8.6 |              20.1 |

**Observation:** AI-TDD reduces development time by 48.5% compared to Manual TDD but results in the fewest mean iterations (5.7). Hybrid mode balances high assertion counts (8.6) with a moderate time efficiency of 29.3% reduction.

### Table II — Classified Metrics Data
| Mode   |   Coverage % |   Mutation Score % |   Defect Density |   Cyclomatic Complexity |   Cognitive Load |   Code Churn |
|:-------|-------------:|-------------------:|-----------------:|------------------------:|-----------------:|-------------:|
| Manual |         84.1 |               48.4 |              3.6 |                     4.8 |              5   |         35.5 |
| AI-TDD |         93.3 |               38.4 |              7.2 |                     4.8 |              2   |         15.6 |
| Hybrid |         91.2 |               58.3 |              2.2 |                     4.3 |              3.9 |         23.4 |

**Observation:** While AI-TDD achieves the highest coverage (93.3%), its mutation score (38.4%) is lower than both Manual and Hybrid modes, indicating shallower test quality. Hybrid AI-Assisted TDD maximizes quality metrics, achieving a peak mutation score of 58.3% while maintaining significantly lower cognitive load than Manual TDD.
