import pandas as pd
import numpy as np
import os

# Set seed for reproducibility but maintain variance
np.random.seed(42)

# 1. Define Manual Data
manual_data = [
    ["P1", "Pakistan", "3–5", "Software Engineer", "Intermediate", "Moderate", "Manual", "Login Service", 42, 38, 9, 12, 78, 4, 6, 25, 7, "High", "No", "No", "Time-consuming"],
    ["P2", "Pakistan", "6–10", "Full Stack", "Expert", "Advanced", "Manual", "Login Service", 25, 27, 6, 9, 86, 2, 5, 34, 5, "High", "Yes", "No", "Prompt tuning"],
    ["P3", "Pakistan", "0–2", "QA Engineer", "Beginner", "Basic", "Manual", "Login Service", 14, 10, 3, 5, 88, 5, 4, 45, 3, "Medium", "Yes", "Yes", "Wrong test cases"],
    ["P4", "Pakistan", "10+", "Software Engineer", "Expert", "Moderate", "Manual", "Login Service", 48, 41, 10, 13, 75, 3, 7, 22, 8, "High", "No", "No", "High effort"],
    ["P5", "Pakistan", "3–5", "Full Stack", "Intermediate", "Advanced", "Manual", "Login Service", 22, 26, 5, 8, 87, 2, 5, 37, 5, "High", "Yes", "No", "Edge cases"],
    ["P6", "Pakistan", "0–2", "QA Engineer", "Beginner", "Basic", "Manual", "Login Service", 13, 9, 2, 4, 89, 6, 3, 48, 3, "Medium", "Yes", "Yes", "Incorrect logic"],
    ["P7", "Pakistan", "6–10", "Software Engineer", "Expert", "Advanced", "Manual", "Login Service", 26, 29, 6, 9, 85, 2, 5, 33, 5, "High", "Yes", "No", "Minor fixes"],
    ["P8", "Pakistan", "3–5", "Full Stack", "Intermediate", "Moderate", "Manual", "Login Service", 40, 36, 8, 11, 77, 3, 6, 26, 7, "High", "No", "No", "Slow iterations"],
    ["P9", "Pakistan", "0–2", "QA Engineer", "Beginner", "Basic", "Manual", "Login Service", 12, 8, 2, 3, 90, 7, 3, 50, 2, "Low", "Yes", "Yes", "Poor coverage logic"],
    ["P10", "Pakistan", "6–10", "Software Engineer", "Expert", "Advanced", "Manual", "Login Service", 24, 28, 6, 10, 86, 2, 4, 35, 5, "High", "Yes", "No", "Refinement needed"]
]

columns = [
    "Participants ID", "Country", "Experience", "Role", "TDD Level", "AI Exp", "Mode", "Task",
    "Time (min)", "Iter", "Tests", "Assert", "Coverage %", "Defects", "Cyclomatic", "Churn",
    "Cog Load", "Confidence", "AI Productivity", "AI Error", "Challenges"
]

df_manual = pd.DataFrame(manual_data, columns=columns)

# 2. Generate AI-TDD Data (P11-P20)
ai_challenges = ["Hallucinated assertions", "Missed edge cases", "Incorrect oracle", "Shallow tests", "Wrong API usage"]
ai_tdd_rows = []

for i, row in df_manual.iterrows():
    # Time: 40-55% lower than manual
    reduction = np.random.uniform(0.40, 0.55)
    time_val = max(5, int(row["Time (min)"] * (1 - reduction)))
    
    # Iter: 3-8
    iter_val = np.random.randint(3, 9)
    
    # Tests: 2-5 (shallower)
    tests_val = np.random.randint(2, 6)
    
    # Assert: 3-7
    assert_val = np.random.randint(3, 8)
    
    # Coverage: 88-96%
    cov_val = np.random.randint(88, 97)
    
    # Defects: 4-9 (higher)
    defects_val = np.random.randint(4, 10)
    
    # Cyclomatic: 3-6
    cyc_val = np.random.randint(3, 7)
    
    # Churn: 10-22
    churn_val = np.random.randint(10, 23)
    
    # Cog Load: 1-3
    cog_val = np.random.randint(1, 4)
    
    new_row = [
        f"P{i+11}", row["Country"], row["Experience"], row["Role"], row["TDD Level"], row["AI Exp"],
        "AI-TDD", "Login Service", time_val, iter_val, tests_val, assert_val, cov_val, defects_val,
        cyc_val, churn_val, cog_val, 
        np.random.choice(["Medium", "Low"]), "Yes", "Yes", 
        np.random.choice(ai_challenges)
    ]
    ai_tdd_rows.append(new_row)

df_ai = pd.DataFrame(ai_tdd_rows, columns=columns)

# 3. Generate Hybrid AI-Assisted Data (P21-P30)
hybrid_challenges = ["Prompt refinement", "Reviewing AI output", "Minor edits", "Context tuning", "Spec clarity"]
hybrid_rows = []

for i, row in df_manual.iterrows():
    # Time: ~30% lower than manual
    reduction = np.random.uniform(0.25, 0.35)
    time_val = max(10, int(row["Time (min)"] * (1 - reduction)))
    
    # Iter: 15-25
    iter_val = np.random.randint(15, 26)
    
    # Tests: 5-9
    tests_val = np.random.randint(5, 10)
    
    # Assert: 7-11
    assert_val = np.random.randint(7, 12)
    
    # Coverage: 88-94%
    cov_val = np.random.randint(88, 95)
    
    # Defects: 1-3 (lowest)
    defects_val = np.random.randint(1, 4)
    
    # Cyclomatic: 4-6
    cyc_val = np.random.randint(4, 7)
    
    # Churn: 18-32
    churn_val = np.random.randint(18, 33)
    
    # Cog Load: 3-5
    cog_val = np.random.randint(3, 6)
    
    new_row = [
        f"P{i+21}", row["Country"], row["Experience"], row["Role"], row["TDD Level"], row["AI Exp"],
        "Hybrid", "Login Service", time_val, iter_val, tests_val, assert_val, cov_val, defects_val,
        cyc_val, churn_val, cog_val, 
        "High", "Yes", np.random.choice(["No", "No", "Yes"]), # Mostly No
        np.random.choice(hybrid_challenges)
    ]
    hybrid_rows.append(new_row)

df_hybrid = pd.DataFrame(hybrid_rows, columns=columns)

# Combine datasets
df_full = pd.concat([df_manual, df_ai, df_hybrid], ignore_index=True)

# 4. Add Mutation Score % (Column 22)
def calculate_mutation_score(row):
    mode = row["Mode"]
    assertions = row["Assert"]
    
    if mode == "Manual":
        # Range 38-58, mean ~45. Correlated with Assertions (range 3-13)
        base = 38
        scale = (assertions - 3) / 10 * 15 # Factor in assertions
        score = base + scale + np.random.uniform(0, 5)
        return int(np.clip(score, 38, 58))
    
    elif mode == "AI-TDD":
        # Range 28-48, mean ~38. Correlated with Assertions (range 3-7)
        base = 28
        scale = (assertions - 3) / 4 * 15
        score = base + scale + np.random.uniform(0, 5)
        return int(np.clip(score, 28, 48))
    
    else: # Hybrid
        # Range 50-70, mean ~60. Correlated with Assertions (range 7-11)
        base = 50
        scale = (assertions - 7) / 4 * 15
        score = base + scale + np.random.uniform(0, 5)
        return int(np.clip(score, 50, 70))

df_full["Mutation Score %"] = df_full.apply(calculate_mutation_score, axis=1)

# Save files
df_full.to_csv("outputs/tdd_full_dataset.csv", index=False)
try:
    df_full.to_excel("outputs/tdd_full_dataset.xlsx", index=False)
except ImportError:
    print("Excel export skipped due to missing openpyxl.")

# Print Summary Statistics
print("\n--- SUMMARY STATISTICS BY MODE ---\n")
modes = ["Manual", "AI-TDD", "Hybrid"]
metrics = ["Time (min)", "Coverage %", "Defects", "Tests", "Mutation Score %"]

for mode in modes:
    mode_df = df_full[df_full["Mode"] == mode]
    print(f"[{mode} Mode]")
    for metric in metrics:
        m = mode_df[metric].mean()
        s = mode_df[metric].std()
        print(f"  {metric:18}: Mean={m:.2f}, StDev={s:.2f}")
    
    # 5. Verify Correlation (Mutation Score vs Assertions)
    correlation = mode_df["Mutation Score %"].corr(mode_df["Assert"])
    print(f"  Assertion Correlation: {correlation:.4f}")
    print("-" * 40)
