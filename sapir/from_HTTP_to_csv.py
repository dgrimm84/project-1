from pathlib import Path

import pandas as pd

# Define the path to the .txt file and output CSV file
input_file = Path.home() / "Downloads" / "GMSL_TPJAOS_5.1.txt"

output_file = "GMSL_TPJAOS_5.1.csv"

# Read the file while skipping header information
data = []
with open(input_file, "r") as file:
    for line in file:
        # Skip lines that are headers or empty
        if line.startswith("HDR") or line.startswith("=") or line.strip() == "":
            continue
        # Split data lines by whitespace
        values = line.split()
        data.append(values)

# Convert the data to a DataFrame
columns = [
    "altimeter_type",
    "merged_file_cycle",
    "year_fraction",
    "num_observations",
    "weighted_observations",
    "GMSL_variation_no_GIA",
    "std_dev_no_GIA",
    "smoothed_GMSL_no_GIA",
    "GMSL_variation_with_GIA",
    "std_dev_with_GIA",
    "smoothed_GMSL_with_GIA",
    "GMSL_removed_annual_signal_no_GIA",
    "GMSL_removed_annual_signal_with_GIA",
]
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame to CSV
df.to_csv(output_file, index=False)

# Display the CSV file path
output_file