import streamlit as st
import pandas as pd
import pickle
import requests


# Function to fetch the movie poster using TMDB API
def fetch_poster(movie_id):
    try:
        response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=d8b6829d5911ac53690864e80a380812')
        response.raise_for_status()
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')
    except Exception as e:
        st.error("Error fetching poster.")
        return "https://via.placeholder.com/500x750?text=No+Image+Available"


# Function to recommend movies
def recommend(movie):
    try:
        movie_index = int(movies[movies['title'] == movie].index[0])
        distances = similarity[movie_index]
        similars = list(enumerate(distances))
        cleaned_similarity = [(index, float(value)) for index, value in similars]
        movies_list = sorted(cleaned_similarity, reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_posters = []

        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_posters.append(fetch_poster(movie_id))

        return recommended_movies, recommended_movies_posters
    except IndexError:
        st.error("Movie not found in the dataset.")
        return [], []
    except Exception as e:
        st.error(f"Error in recommendation: {e}")
        return [], []



# Load data
movies_dictt = pickle.load(open('movie_dictt.pkl', 'rb'))
movies = pd.DataFrame(movies_dictt)

similarity = pickle.load(open('similarity.pkl', 'rb'))


# Streamlit app
st.title('Movie Recommender System')

# Dropdown to select a movie
selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies['title'].values
)

# Button to get recommendations
if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            if idx < len(names):  # Prevent out-of-range errors
                st.text(names[idx])
                st.image(posters[idx])
