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

NUM_PER_TYPE = 20
MIN_POINTS = 5
MAX_POINTS = 10
MIN_VAL = 5
MAX_VAL = 100

def generate_chart(chart_type, idx):
    n = random.randint(MIN_POINTS, MAX_POINTS)

    values = [random.randint(MIN_VAL, MAX_VAL) for _ in range(n)]
    labels = list(range(1, n + 1))

    # pick two distinct sections to compare
    a, b = random.sample(labels, 2)

    v1 = values[a-1]
    v2 = values[b-1]

    true_percent = round(min(v1, v2) / max(v1, v2) * 100)

    return {
        "chart_id": f"{chart_type}_{idx:02d}",
        "type": chart_type,
        "values": values,
        "labels": labels,
        "compare": [a, b],
        "true_percent": true_percent
    }


charts = []

for t in ["pie", "bar_vertical", "bar_horizontal"]:
    for i in range(1, NUM_PER_TYPE + 1):
        charts.append(generate_chart(t, i))

# shuffle order for experiment randomization
random.shuffle(charts)

with open("generated_charts.json", "w") as f:
    json.dump(charts, f, indent=2)

print("Generated generated_charts.json with", len(charts), "charts")
