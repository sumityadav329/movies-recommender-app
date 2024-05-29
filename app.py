import streamlit as st
import pandas as pd
import pickle


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    
    for i in movies_list:
        recommended_movies.append(movies['title'].iloc[i[0]])
    return recommended_movies



movies = pickle.load(open('models\movie_list.pkl','rb'))
similarity = pickle.load(open('models\similarity.pkl','rb'))

st.header('Movie Recommender Web App')

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie)
    for i in recommendations:
        st.write(i)
