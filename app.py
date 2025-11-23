import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_data
def load_data():
    df = pd.read_csv("movies.csv")
    df['combined'] = df[['genres','keywords','tagline','cast','director']].fillna('').agg(' '.join, axis=1)
    return df

@st.cache_resource
def build_model(df):
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['combined'])
    similarity = cosine_similarity(tfidf_matrix)
    return similarity

st.title("🎬 Movie Recommendation System")

df = load_data()
similarity = build_model(df)

movie_list = df['title'].tolist()
selected_movie = st.selectbox("Select a movie:", movie_list)

if st.button("Recommend"):
    idx = df[df['title'] == selected_movie].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:11]
    st.subheader("Top Recommendations:")
    for i, score in scores:
        st.write(df.iloc[i]['title'])
