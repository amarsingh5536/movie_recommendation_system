# Import necessary libraries
import pandas as pd
from sklearn.neighbors import NearestNeighbors

def get_recomendations(description):
    try:
        """
        In the function we are using k-nearest neighbors (KNN) with scikit-learn to get recommendation.\
        first we prepare dataset with movie features cosine similarity metric to find \
        similar movies with the k-nearest neighbors algorithm.
        """

        # Load your movie dataset 
        # The dataset should have columns like 'Title','Cast','Genres','Writers' ...
        movies_df = pd.read_csv('movie_recommendation_app/recomendations/Hydra-Movie-Scrape.csv')

        # Extract features for similarity calculation (use one-hot encoding for genres)
        features = pd.get_dummies(movies_df[['Title','Cast','Genres','Writers']])

        # Initialize and fit the Nearest Neighbors model
        knn_model = NearestNeighbors(n_neighbors=5, metric='cosine')
        knn_model.fit(features)

        # Choose a movie to find similar movies
        query_movie = description #"Avatar"

        # Find the index of the query movie in the dataset
        query_index = movies_df[movies_df['Title'] == query_movie].index[0]

        # Get the distances and indices of the k-nearest neighbors
        distances, indices = knn_model.kneighbors(features.iloc[query_index, :].values.reshape(1, -1))

        # Display similar movies
        similar_movies = [(movies_df['Title'][i], distances[0, j]) for j, i in enumerate(indices.flatten()) if i != query_index]
        response = list()
        print(f"Movies similar to '{query_movie}':")
        for movie, distance in similar_movies:
            print(f"{movie} (Distance: {distance:.4f})")
            response.append(movie)
        return response
    except Exception as e:
        print(e)
        return "Something Went Wrong!"