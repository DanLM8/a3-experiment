import csv
import glob

# output file
OUTPUT = "total_results.csv"

# find all trial files
files = sorted(glob.glob("trial*.csv"))

if not files:
    print("No trial CSV files found.")
    exit()

print("Found files:", files)

with open(OUTPUT, "w", newline="") as out_file:
    writer = None

    for i, file in enumerate(files):
        with open(file, newline="") as f:
            reader = csv.reader(f)

            header = next(reader)

            # write header only once
            if writer is None:
                writer = csv.writer(out_file)
                writer.writerow(header + ["trial_file"])

            for row in reader:
                writer.writerow(row + [file])

print(f"\nCombined CSV saved as: {OUTPUT}")
