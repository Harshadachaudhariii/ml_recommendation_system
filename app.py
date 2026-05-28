import streamlit as st  
import pickle
import requests 
import os
from dotenv import load_dotenv
load_dotenv()
tmdb_api_key = os.getenv("TMDB_API_KEY")

movies = pickle.load(open("movies_list.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))
movies_list = movies['title'].values

st.header("Movie Recommendation System")
select_values = st.selectbox("Select movie from dropdown", movies_list)

def fetch_poster(movie_id):
    if not tmdb_api_key:
        st.error("API Key is missing! Please check your .env file setup.")
        return "https://via.placeholder.com/500x750?text=No+API+Key"
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}&language=en-US"
    try: 
        responses = requests.get(url)
        data = responses.json()
    # Check if 'poster_path' exists in the response
        if 'poster_path' in data and data['poster_path']:
            poster_path = data['poster_path']
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            # Print the API response to the app UI to debug why it failed
            st.warning(f"Could not fetch poster for ID {movie_id}. API Response: {data.get('status_message', 'Unknown Error')}")
            return "https://via.placeholder.com/500x750?text=Poster+Not+Found"
            
    except Exception as e:
        st.error(f"Connection Error: {e}")
        return "https://via.placeholder.com/500x750?text=Error"



def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distance =sorted(list(enumerate(similarity[index])), reverse=True, key = lambda vector:vector[1])
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:6]:
        movie_id  = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movie_id))
    return recommend_movie, recommend_poster

if st.button("Show Recommend"):
    movie_name, movie_poster = recommend(select_values)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
