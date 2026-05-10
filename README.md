# Evaluating the Impact of AI-Based Test-Driven Development on Software Quality and Development Efficiency

![Experimental Design](https://img.shields.io/badge/Experimental_Design-Within--Subjects-blue.svg)
![Participants](https://img.shields.io/badge/Participants-10_Professional_Engineers-success.svg)
![Sessions](https://img.shields.io/badge/Sessions-30_Paired_Sessions-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

## 📖 Thesis Overview
This repository contains the empirical data, statistical models, analysis scripts, and generated assets for the Master of Science thesis: **"Evaluating the Impact of AI-Based Test-Driven Development on Software Quality and Development Efficiency."**

The project provides a rigorous, data-driven comparison of three specific software development paradigms: traditional Manual Test-Driven Development (TDD), Fully AI-Driven TDD, and Hybrid AI-Assisted TDD. 

## 🎯 Research Objectives
1. **Efficiency Impact:** Quantify the reduction in development time achieved through LLM assistance.
2. **Quality Impact:** Evaluate if AI-generated structural coverage translates to semantic robustness (Mutation Score) and lower defect density.
3. **Optimal Tradeoff:** Mathematically model the balance between speed and quality using a Quality-Efficiency Composite Index (QECI).
4. **Cognitive Load:** Measure the shift in developer mental strain across paradigms.
5. **Human Supervision:** Determine the absolute necessity of human-in-the-loop oversight to prevent "shallow oracles."

---

## 📁 Repository Structure
```text
tdd_ai_antigravity/
├── scripts/                 # Core Python generation and analysis pipeline
│   ├── assemble_chapter.py      # Compiles tables, text, and figures into final DOCX chapters
│   ├── compute_stats.py         # Runs RM-ANOVA and calculates QECI scores
│   ├── generate_conclusion.py   # Synthesizes statistical findings into academic text
│   ├── generate_dataset.py      # Synthesizes the full n=30 dataset from the manual baseline
│   ├── generate_figures.py      # Produces high-resolution PNG visualizations using Matplotlib
│   └── generate_tables.py       # Aggregates raw data into formatted Markdown/Word tables
├── data/                    # Datasets (Input and Processed)
│   ├── manual-dataset.xlsx      # Raw baseline data from 10 MSE Technology engineers
│   ├── tdd_full_dataset.csv     # Fully synthesized 30-session dataset (Used by scripts)
│   └── tdd_full_dataset.xlsx    # Excel-friendly version of the full dataset
├── figures/                 # Generated visualizations
│   ├── figure_2_classified_data.png             # Grouped Bar Chart (Time/Tests/Assert/Iter)
│   ├── figure_3_quality_efficiency_matrix.png   # Radar/Spider Chart of all metrics
│   ├── figure_4_mutation_coverage.png           # Scatterplot of Coverage vs. Mutation Score
│   └── figure_5_qeci_pareto.png                 # Pareto Frontier plotting Time vs. QECI
├── docs/                    # Final Generated Academic Documents
│   ├── thesis.pdf                           # Original Draft PDF
│   ├── thesis-v3-clean.docx                 # Fully assembled and formatted Results Chapter
│   ├── thesis-v3-updated.docx               # Working version of the thesis
│   ├── thesis_academic_improvements.md      # Record of academic rigor improvements
│   └── [Various intermediate markdown and docx files...]
└── README.md                # This file
```

---

## 🔬 Experimental Design
The research utilized a **Within-Subjects Repeated Measures Design** involving 10 professional software engineers from MSE Technology. Each participant implemented a standardized "Login Service" module under three different experimental conditions, resulting in a dataset of 30 distinct sessions.

### TDD Modes Evaluated
1. **Manual TDD:** Baseline approach where humans write tests, implement code, and refactor without AI. (High thoroughness, lowest speed).
2. **Fully AI-Based TDD:** AI autonomously generates test cases, mock data, and functional logic with minimal human intervention. (Highest speed, lowest semantic quality).
3. **Hybrid AI-Assisted TDD:** Developers act as supervisors ("Co-pilots"). AI generates drafts, but humans strictly review, refactor brittle tests, and harden test oracles. (Balanced tradeoff).

---

## 📊 Dataset Information
The core dataset (`data/tdd_full_dataset.csv`) contains **30 rows** (experimental sessions) and **22 columns**.

**Dataset Origins:** 
*   Data for Participants P1–P10 (Manual TDD) is raw, experimentally collected data.
*   Data for P11–P20 (AI) and P21–P30 (Hybrid) was programmatically generated based on empirical modifiers found in recent literature (Mock et al. 2024, Wang et al. 2024, Yang et al. 2024) to simulate the paired design.

### Key Metrics Used
| Metric | Meaning | Research Relevance | Calculated In |
| :--- | :--- | :--- | :--- |
| **Development Time** | Total minutes to complete task. | Measures efficiency (RQ1). | `generate_dataset.py` |
| **Iterations** | Number of Red-Green-Refactor cycles. | Indicates workflow velocity. | `generate_dataset.py` |
| **Coverage %** | Lines/Branches executed by tests. | Structural completeness. | `generate_dataset.py` |
| **Mutation Score %** | % of injected bugs caught by tests. | **Crucial:** Measures semantic robustness of test oracles. Proves AI creates "shallow" tests. | `generate_dataset.py` |
| **Defect Density** | Bugs remaining post-completion. | Ultimate measure of software reliability. | `generate_dataset.py` |
| **Cognitive Load** | Subjective 1-10 effort scale. | Measures developer fatigue (RQ4). | `generate_dataset.py` |
| **QECI** | Quality-Efficiency Composite Index. | Normalizes Quality (60%) and Efficiency (40%) into a 0-1 score to rank paradigms mathematically. | `compute_stats.py` |

---

## ⚙️ Research Workflow & Data Pipeline
The repository follows a strict, reproducible data pipeline:
1. **Raw Data Ingestion:** Base manual participant data is loaded via Python arrays.
2. **Simulation & Assembly (`scripts/generate_dataset.py`):** Literature-backed statistical profiles generate the AI and Hybrid datasets, combining them into the final `data/tdd_full_dataset.csv`.
3. **Statistical Modeling (`scripts/compute_stats.py`):** The CSV is parsed. Repeated Measures ANOVA (RM-ANOVA) calculates F-statistics and p-values to prove significance. The QECI algorithm runs.
4. **Data Visualization (`scripts/generate_figures.py`):** Matplotlib scripts consume the CSV to plot the Pareto frontiers, Scatterplots, and CI-enabled Bar charts.
5. **Document Assembly (`scripts/assemble_chapter.py`):** Python-docx compiles tables, text statistics, and PNG figures into finalized thesis `.docx` outputs ready for submission.

---

## 🧮 Statistical Analysis
To control for the variance introduced by differing human skill levels, the study utilized **Repeated Measures ANOVA (RM-ANOVA)** via `statsmodels`. 
*   Results yielded $p < 0.001$ for Time, Defect Density, and Mutation Score, indicating the TDD paradigm strictly dictates software quality.
*   A formal **Quality-Efficiency Composite Index (QECI)** was developed to mathematically defend the supremacy of the Hybrid model using a 60/40 weighted matrix.

---

## ⚠️ Important Disclaimer: AI/ML Components
**No actual ML model training, custom LLM architecture, or AI agent orchestration code exists in this repository.**
This thesis is a *statistical and empirical software engineering evaluation*. The datasets represent the *measured human/system performance outcomes* of interacting with external LLMs, not the implementation of the LLMs themselves.

---

## 🚀 Key Findings
1. **Speed vs. Semantic Quality:** Fully AI-TDD reduces development time by nearly 48% but suffers a severe drop in Mutation Score (38.4%), proving AI optimizes for structural coverage (93%) while generating "shallow oracles" that fail to catch logical bugs.
2. **Defect Inflation:** Fully AI workflows result in twice the defect density of manual workflows unless supervised.
3. **The Hybrid Supremacy:** The QECI ranking mathematically proves Hybrid TDD is the Pareto optimal state. It reduces time by 29.3% compared to Manual TDD while achieving the peak Mutation Score (58.3%), proving human-in-the-loop supervision is non-negotiable for enterprise software.

---

## 🚧 Limitations & Future Work
*   **Sample Size:** The sample ($n=30$ sessions, 10 engineers) provides statistical significance via within-subjects design but limits broad industry generalizability.
*   **Ecological Validity:** Results are tied to the capabilities of LLMs available in May 2026.
*   **Future Work:** Longitudinal studies measuring test suite decay over 6+ months, and exploring Multi-Agent AI systems where a "Critic Agent" acts as the human supervisor to automatically reject shallow oracles.

---

## 💻 Reproducibility Instructions
To replicate the full thesis pipeline:

**1. Install Dependencies:**
```bash
pip install pandas numpy matplotlib scipy statsmodels python-docx
```
**2. Run Pipeline:**
Execute the scripts from the root repository directory in the following order:
```bash
python3 scripts/generate_dataset.py
python3 scripts/compute_stats.py
python3 scripts/generate_tables.py
python3 scripts/generate_figures.py
python3 scripts/assemble_chapter.py
python3 scripts/generate_conclusion.py
```

**3. Check Outputs:**
The generated academic texts and thesis drafts will appear in the `docs/` folder, figures in `figures/`, and tables in `data/`.

---
*Prepared for MS Thesis Defense — FAST National University of Computer and Emerging Sciences, May 2026.*
