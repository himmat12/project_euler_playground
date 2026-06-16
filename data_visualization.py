import json
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the JSON file
with open("./docs/problem_zero/problem_zero_computation.json") as f:
    data = json.load(f)

# 2. Keep only records that have iteration info
records = [d for d in data if "iteration" in d]
df = pd.DataFrame(records)

# 3. Line plot: duration vs iteration
plt.figure(figsize=(10, 4))
plt.plot(df["iteration"], df["duration"])
plt.xlabel("Iteration")
plt.ylabel("Duration (seconds)")
plt.title("Duration per Iteration")
plt.tight_layout()
plt.show()

# 4. Optional: square count over iterations
plt.figure(figsize=(10, 4))
plt.plot(df["iteration"], df["square_nums"])
plt.xlabel("Iteration")
plt.ylabel("Number of squares found")
plt.title("Squares Found vs Iteration")
plt.tight_layout()
plt.show()