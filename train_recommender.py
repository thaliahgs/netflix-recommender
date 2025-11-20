import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import os

# ---- 1. Load cleaned dataset ----
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "netflix_cleaned_fixed.csv")
df = pd.read_csv(DATA_PATH)

# ---- 2. Check required columns exist ----
required_columns = ["type", "director", "cast", "country", "listed_in", "duration", "description"]

for col in required_columns:
    if col not in df.columns:
        print(f"Missing column in dataset: {col}. Creating empty placeholder.")
        df[col] = "unknown"

# ---- 3. Create combined text field ----
df["combined"] = (
    df["type"].astype(str) + " " +
    df["director"].astype(str) + " " +
    df["cast"].astype(str) + " " +
    df["country"].astype(str) + " " +
    df["listed_in"].astype(str) + " " +
    df["description"].astype(str)
)

# ---- 4. TF-IDF Vectorization ----
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["combined"])

# ---- 5. Cosine similarity matrix ----
similarity_matrix = cosine_similarity(tfidf_matrix)

# ---- 6. Make sure models folder exists ----
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models")
os.makedirs(MODEL_PATH, exist_ok=True)

# ---- 7. Save similarity matrix ----
with open(os.path.join(MODEL_PATH, "similarity.pkl"), "wb") as f:
    pickle.dump(similarity_matrix, f)

# ---- 8. Save dataset used for recommendations ----
df.to_csv(os.path.join(MODEL_PATH, "df_for_recommender.csv"), index=False)

print("\n----------------------------------")
print(" Recommender model successfully trained!")
print(" Files saved inside the /models folder.")
print("----------------------------------")
