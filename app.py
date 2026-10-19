
import streamlit as st
import pickle
import pandas as pd

# Load Saved Models
movies_df = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie_title):
    movie_index = movies_df[movies_df['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies

st.title("🎬 Movie Recommendation System")
st.write("Select a movie to get similar recommendations:")

selected_movie = st.selectbox(
    "Choose a Movie:",
    movies_df['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    st.subheader("Recommended Movies:")
    for col, movie in enumerate(recommendations, 1):
        st.write(f"{col}. {movie}")