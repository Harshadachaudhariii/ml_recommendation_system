## Movie Recommendation System 
A complete end-to-end Machine Learning web application that recommends movies based on textual similarity. This project demonstrates data preprocessing, feature engineering with NLP, similarity modeling, and web deployment.

# Live Features
Content-Based Filtering: Recommends movies similar to a user's selection by analyzing genres and plot overviews.

Dynamic Poster Fetching: Integrates with the TMDB API to fetch and display high-resolution movie posters in real-time.

Interactive UI: A clean, responsive dashboard built with Streamlit for a seamless user experience.

# Technical Stack
 * Language: Python
 * Data Manipulation: Pandas
 * Machine Learning: Scikit-Learn (CountVectorizer & Cosine Similarity)
 * Web Framework: Streamlit
 * API: TMDB (The Movie Database)
 * Model Persistence: Pickle

## How It Works
* Data Preprocessing & EDA: The system uses a dataset of 10,000 movies. I performed data cleaning to handle missing values in genres and overviews and selected key features (id, title, genre, overview) for the model.
* Feature Engineering:
 * To find similarities, I created a "Tags" system: Combined the overview and genre columns into a single string for each movie. Used CountVectorizer to convert these text tags into 10,000-dimensional vectors, removing English stop words to focus on meaningful content.

* Similarity Modeling:
Instead of simple keyword matching, the system calculates the Cosine Similarity between movie vectors. This measures the cosine of the angle between two vectors, allowing the system to find the "nearest" movies in a high-dimensional space.

* Application Logic
The trained model and similarity matrix are exported using pickle.
The Streamlit app loads these files to provide instant recommendations without retraining.
When a movie is selected, the recommend() function identifies the top 5 closest matches and fetches their posters via API.

* Project Structure
main.ipynb: Data cleaning, EDA, and model building logic.
app.py: Streamlit frontend code and API integration.
movies_list.pkl: Pickled dataframe of processed movies.
similarity.pkl: Pre-computed similarity matrix for fast retrieval.

* Installation & Usage
Clone the repository.
Install dependencies: 
```
pip install -r requirements.txt
```
Run the app: 
```
streamlit run app.py.
```
