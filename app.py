import streamlit as st
import pickle
import pandas as pd
import requests



def recommend(movie):
    index = movies[movies['title']==movie].index[0]
    distances=similarity[index]
    recommendation_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies = []

    for i in recommendation_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetching api posters
    return recommended_movies

movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title("🎬 Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select movie name:",
    movies_list,
)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for j in recommendations:
        st.write(j)

