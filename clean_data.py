import pandas as pd
import os

# Path to dataset
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "netflix_titles.csv")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "netflix_cleaned.csv")

print(f"Loading dataset from: {DATA_PATH}")

# Load dataset
df = pd.read_csv(DATA_PATH)

# Columns we want to keep
columns_to_keep = [
    "type",
    "director",
    "cast",
    "country",
    "release_year",
    "rating",
    "duration",
    "listed_in"
]

df = df[columns_to_keep]

# -------------------------------------------------
# 1️⃣ Replace NaN with "Unknown"
# -------------------------------------------------
df = df.fillna("Unknown")

# -------------------------------------------------
# 2️⃣ Normalize duration
# Creates two new columns:
# duration_value → number
# duration_type → "min" / "Season"
# -------------------------------------------------
def parse_duration(value):
    text = value.lower().strip()

    # If "min" → extract number of minutes
    if "min" in text:
        num = int(text.replace("min", "").strip())
        return num, "min"

    # If "season" → extract number of seasons
    if "season" in text:
        num = int(text.replace("seasons", "").replace("season", "").strip())
        return num, "season"

    return None, "unknown"

df["duration_value"], df["duration_type"] = zip(*df["duration"].apply(parse_duration))

# -------------------------------------------------
# 3️⃣ Clean text for easier searching
# lowercase + remove extra spaces
# -------------------------------------------------
def clean_text(x):
    if isinstance(x, str):
        return " ".join(x.lower().split())
    return x

df["director"] = df["director"].apply(clean_text)
df["cast"] = df["cast"].apply(clean_text)
df["country"] = df["country"].apply(clean_text)
df["listed_in"] = df["listed_in"].apply(clean_text)
df["rating"] = df["rating"].apply(clean_text)
df["type"] = df["type"].apply(clean_text)

# -------------------------------------------------
# 4️⃣ Save cleaned dataset
# -------------------------------------------------
df.to_csv(OUTPUT_PATH, index=False)

print("\n=== First 10 rows of cleaned dataset ===")
print(df.head(10))

print("\n=== New Shape (rows, columns) ===")
print(df.shape)

print(f"\nCleaned dataset saved as: {OUTPUT_PATH}")


