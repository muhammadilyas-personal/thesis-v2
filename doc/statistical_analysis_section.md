STATISTICAL ANALYSIS (ACADEMIC IMPROVEMENTS)

I. REPEATED MEASURES ANOVA
To account for the within-subjects experimental design, Repeated Measures ANOVA (RM-ANOVA) was utilized to analyze the quality metrics. 
For Mutation Score, the analysis revealed a statistically significant effect of TDD mode, F(2, 18) = 52.22, p < 0.001. 
For Defect Density, a significant effect was also observed, F(2, 18) = 33.02, p < 0.001. 
For Coverage %, the effect was significant, F(2, 18) = 16.19, p < 0.001. 
These results provide robust evidence that the TDD paradigm strictly dictates the resulting software quality.

II. QUALITY-EFFICIENCY COMPOSITE INDEX (QECI)
To mathematically evaluate the optimal tradeoff (RQ3), a QECI was computed using a 60/40 weighted normalization model (Quality/Efficiency).
The QECI rankings were calculated as follows:
- Hybrid TDD: 0.766 (Rank 1)
- Manual TDD: 0.601 (Rank 2)
- Fully AI-TDD: 0.559 (Rank 3)

Interpretation: The Hybrid model mathematically dominates the Pareto frontier because its slight reduction in temporal efficiency compared to Fully AI-TDD is vastly outweighed by its superiority in semantic quality (Mutation Score and Defect Density).
