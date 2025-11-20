from flask import Flask, request, jsonify
import pandas as pd
import pickle
import os
from fuzzywuzzy import process

app = Flask(__name__)

# -----------------------------------
# LOAD MODEL + DATASET
# -----------------------------------
MODEL_FOLDER = os.path.join(os.path.dirname(__file__), "..", "models")

with open(os.path.join(MODEL_FOLDER, "similarity.pkl"), "rb") as f:
    similarity = pickle.load(f)

df = pd.read_csv(os.path.join(MODEL_FOLDER, "df_for_recommender.csv"))

# Pre-lowercase titles for faster search
titles_lower = df["title"].str.lower().tolist()


# -----------------------------------
# CLEAN FORMAT FUNCTION
# -----------------------------------
def format_recommendation(row, score):
    return {
        "title": row["title"],
        "genre": row["listed_in"],
        "director": row["director"],
        "cast": row["cast"],  # already one-line
        "year": int(row["release_year"]) if "release_year" in row and not pd.isna(row["release_year"]) else None,
        "description": row["description"],
        "score": round(float(score), 3)
    }


# -----------------------------------
# HOME ROUTE
# -----------------------------------
@app.route("/")
def home():
    return jsonify({"message": "Netflix API with Recommender is running!"})


# -----------------------------------
# RECOMMENDATION ENDPOINT
# -----------------------------------
@app.route("/recommend", methods=["GET"])
def recommend():
    user_input = request.args.get("title")

    if not user_input:
        return jsonify({"error": "Missing ?title= parameter"}), 400

    # Fuzzy match best title
    best_match, score = process.extractOne(user_input, titles_lower)

    # If match confidence low, warn user
    if score < 60:
        return jsonify({
            "error": "No close match found for your input",
            "input": user_input,
            "confidence": score
        }), 404

    # Find exact index of matched title
    idx = df[df["title"].str.lower() == best_match].index[0]

    # Get similarity scores
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Pick top 10 (skip index 0 — itself)
    top_indices = [i for i, s in scores[1:11]]

    recommendations = []
    for i in top_indices:
        row = df.iloc[i]
        recommendations.append(format_recommendation(row, similarity[idx][i]))

    return jsonify({
        "input": user_input,
        "matched_title": df.loc[idx, "title"],
        "confidence": score,
        "recommendations": recommendations
    })


if __name__ == "__main__":
    app.run(debug=True)
