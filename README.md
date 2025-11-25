# Movie-Recommendation-System

The primary goal of this project is to develop a reliable system that can suggest movies to a user based on their preferences. This implementation focuses on a Content-Based Filtering approach by analyzing the descriptive features of a movie (such as genre, keywords, cast, and director) to find recommendations.

The code explores three main paradigms of recommendation systems:

Content-Based Filtering (Implemented): Recommends items similar to those the user liked in the past.

Popularity-Based Filtering (Conceptual): Recommends items that are currently popular or trending.

Collaborative Filtering (Conceptual): Recommends items based on the past preferences of other similar users.

🚀 Core Implementation: Content-Based Filtering
The functioning of the content-based engine is achieved in three main stages: Data Preprocessing, Feature Vectorization, and Similarity Calculation.

1. Data Processing & Feature Preparation
The system first cleans the raw movie data and combines relevant textual information for analysis.

Data Source: The project utilizes the movies.csv dataset.

Selected Features: The following columns are extracted and combined into a single string for each movie, forming the "content" used for similarity calculation:

genres

keywords

tagline

cast

director

Missing Data Handling: All missing values (NaN) in the selected features are replaced with an empty string ('') to prevent errors during the vectorization step.

2. Feature Vectorization (TF-IDF)
Since machine learning models require numerical input, the textual data is converted into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency).

Process: The TfidfVectorizer is used to quantify the importance of each word (token) in a movie's combined feature string relative to the entire dataset.

Term Frequency (TF): How often a word appears in the current movie's description.

Inverse Document Frequency (IDF): How rare the word is across all movie descriptions.

Output: A matrix (feature_vector) where each row represents a movie, and columns represent unique words, with values being their calculated TF-IDF scores.

3. Similarity Calculation (Cosine Similarity)
The final step in determining recommendations is calculating how similar every movie is to every other movie.

Metric: Cosine Similarity is applied to the TF-IDF feature vectors. This mathematical measure calculates the cosine of the angle between two vectors.

Score Interpretation: The resulting similarity score ranges from 0 to 1.

1.0: The two movies are identical in their content.

0.0: The two movies share no common content.

Recommendation Logic: When a user selects a movie, the system retrieves its scores from the similarity matrix, sorts them in descending order, and recommends the top-scoring movies (excluding the query movie itself).
