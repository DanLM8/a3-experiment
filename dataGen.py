"""
3 visual types
5-10 data points per visual, valued at 5-100 per data point
20 trials per visual
10+ participants
===
randomly generate 20 charts per type (vertical bar chart, horizontal bar chart, pie chart),
consisting of 5-10 data points each. 
"""

import random
import json
import statistics

NUM_PER_TYPE = 20
MIN_POINTS = 5
MAX_POINTS = 10
MIN_VAL = 5
MAX_VAL = 100

COLORS = ["#1976d2", "#ef6c00", "#2e7d32", "#6a1b9a", "#c62828"]

def generate_chart(chart_type, idx):
    n = random.randint(MIN_POINTS, MAX_POINTS)

    values = [random.randint(MIN_VAL, MAX_VAL) for _ in range(n)]
    labels = list(range(1, n + 1))

    data_points = [
        {"label": labels[i], "value": values[i]}
        for i in range(n)
    ]

    median_val = statistics.median(values)

    return {
        "chart_id": f"{chart_type}_{idx:02d}",
        "type": chart_type,
        "color": random.choice(COLORS),
        "data": data_points,
        "median": median_val
    }

charts = []

for t in ["pie", "bar_vertical", "bar_horizontal"]:
    for i in range(1, NUM_PER_TYPE + 1):
        charts.append(generate_chart(t, i))

random.shuffle(charts)

with open("generated_charts.json", "w") as f:
    json.dump(charts, f, indent=2)

print("Generated generated_charts.json with", len(charts), "charts")

