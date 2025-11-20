Netflix Recommender System (Flask API)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This project implements a content-based recommendation system for Netflix movies and TV shows. It uses textual metadata (cast, description, genres) to suggest similar titles based on a given input.
A lightweight Flask API allows users to query recommendations by providing a title. 

Repository Layout 
----------------------------------------------------------------------------------------------------------------------------------------------------------------
├── .gitignore 

├── README.md

├── app.py                      # Flask API entry point

├── clean_data.py               # Initial data cleaning script|

├── clean_data_fixed.py         # Final cleaning adjustments

├── df_for_recommender.csv

├── load_dataset.py             # Loads and prepares data

├── netflix_clean.csv           # Intermediate cleaned version

├── netflix_cleaned.csv         # Further cleaned version

├── netflix_cleaned_fixed.csv   # Final cleaned version

├── netflix_titles.csv          # Original Netflix dataset

├── requirements.txt            # Dependencies for running the app

└── train_recommender.py        # Generates similarity matrix (not included in repo)

 Dataset
----------------------------------------------------------------------------------------------------
This project uses a Netflix dataset containing metadata about movies and TV shows. Each entry includes:
- Title
- Cast
- Director
- Genre (listed categories)
- Description
- Year
- Release year and country
This metadata is used to find similarities between titles based on shared actors, genres, and descriptions.


Methodology
----------------------------------------------------------------------------------------------------
The recommendation system works in four steps:
1. Data Cleaning
Python scripts clean and prepare the dataset by:
    - Removing missing values
    - Normalizing text (lowercase, stripped punctuation)
    - Combining cast, genres, and description into one searchable field
2. Feature Extraction
Text features are converted into numerical vectors using TF-IDF, which helps the system understand the importance of words across titles.
3. Similarity Computation
Using cosine similarity, the system compares titles and builds a matrix of how similar each show/movie is to others.
5. Flask API
The user enters a title in the search bar. The API:
     - Finds the closest match
     - Returns a list of similar titles based on genre and cast
     - Sends results in JSON format

Future Improvements
--------------------------------------------------------------------------------------------------
- Host the API online (e.g., Render, Railway)
- Add a web frontend for user interaction
- Include poster images and richer metadata
- Explore hybrid recommendation (content + popularity)

License
-----------------------------------------------------------------------------------------------------
This project is open-source and may be used for educational and non-commercial purposes.

Would you like a version in French too? Or maybe a shorter version for your portfolio or GitHub profile? I can also help you add a banner, badges, or a “How it works” diagram if you want to make it pop visually.







