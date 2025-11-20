# src/load_dataset.py

import pandas as pd
import os

def main():
    # Path to your Netflix dataset inside /data/
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'netflix_titles.csv')

    print(f"Loading dataset from: {csv_path}")

    # Load the CSV
    df = pd.read_csv(csv_path)

    # Print first 10 rows
    print("\n=== First 10 Rows ===")
    print(df.head(10))

    # Print column names
    print("\n=== Columns ===")
    print(df.columns)

    # Print dataset shape
    print("\n=== Shape (rows, columns) ===")
    print(df.shape)

if __name__ == "__main__":
    main()
