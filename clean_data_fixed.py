import pandas as pd
import os

RAW_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "netflix_titles.csv")
SAVE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "netflix_cleaned_fixed.csv")

df = pd.read_csv(RAW_PATH)

# Keep title!
columns_to_keep = [
    "show_id", "type", "title", "director", "cast", "country",
    "date_added", "release_year", "rating", "duration",
    "listed_in", "description"
]

df = df[columns_to_keep]

# Fill missing
df = df.fillna("unknown")

# Extract duration_type + duration_value
df["duration_value"] = df["duration"].str.extract(r"(\d+)").astype(float)
df["duration_type"] = df["duration"].str.extract(r"([A-Za-z]+)")

df.to_csv(SAVE_PATH, index=False)

print("✔ Cleaned dataset created WITH TITLE column!")
