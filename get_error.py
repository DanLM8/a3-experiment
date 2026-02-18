import csv
import math

INPUT = "total_results.csv"
OUTPUT = "total_results_error.csv"

with open(INPUT, newline="") as infile, open(OUTPUT, "w", newline="") as outfile:

    reader = csv.DictReader(infile)

    fieldnames = reader.fieldnames + ["error"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        try:

            true_val = float(row["correct_median"])
            judged_val = float(row["chosen_value"])

            error = math.log2(abs(judged_val - true_val) + 1)
            row["error"] = error

            if error == -3:
                error = 0

        except:
            error = ""

        row["error"] = error
        writer.writerow(row)

print("Error column added")
