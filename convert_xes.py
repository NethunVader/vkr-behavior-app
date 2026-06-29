import pm4py
import pandas as pd
import os

print("Starting conversion... This will take a few minutes and use a lot of RAM.")

# The path to your heavy XES file
xes_path = "data/raw/bpi_2019.xes"
csv_path = "data/raw/bpi_2019.csv"

if not os.path.exists(xes_path):
    print(f"Error: Could not find {xes_path}")
else:
    # 1. Read the heavy XES file
    print("Reading XES file (this is the slow part)...")
    log = pm4py.read_xes(xes_path)
    
    # 2. Convert to Pandas
    print("Converting to dataframe...")
    df = pm4py.convert_to_dataframe(log)
    
    # 3. Save as a clean CSV
    print(f"Saving to {csv_path}...")
    df.to_csv(csv_path, index=False)
    
    print("Success! You can now use the CSV file in your Streamlit app.")