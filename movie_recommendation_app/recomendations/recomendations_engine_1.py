import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import sigmoid_kernel

def get_recomendations(description):
    try:
        """
            In this function, the TF-IDF vectorizer is used to convert product descriptions \
            into vectors, and then cosine similarity is calculated between the vectors to \
            determine product similarity.

        """
        title=description #"Avatar"
        movies = pd.read_csv("movie_recommendation_app/recomendations/Hydra-Movie-Scrape.csv")


        movies_cleaned = movies.drop(columns=['Runtime'])

        # Use TF-IDF Vectorizer to convert text descriptions into vectors
        tfv = TfidfVectorizer(min_df=3,  max_features=None,
                strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}',
                ngram_range=(1, 3),
                stop_words = 'english')

        soup = movies_cleaned['Title'] + " " + movies_cleaned['Genres'] + " " + movies_cleaned['Writers'] + " " + movies_cleaned['Cast'] 
        
        # soup =  movies_cleaned['Short Summary']
        tfv_matrix = tfv.fit_transform(soup.values.astype('U'))

        # Compute cosine similarity between products the sigmoid kernel
        sig = sigmoid_kernel(tfv_matrix, tfv_matrix)

        indices = pd.Series(movies_cleaned.index, index=movies_cleaned['Title']).drop_duplicates()

        # Get the index corresponding to original_title
        idx = indices[title]

        # Get the pairwsie similarity scores
        sig_scores = list(enumerate(sig[idx]))

        # Sort the movies
        sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

        # Scores of the 10 most similar movies
        sig_scores = sig_scores[1:11]

        # Movie indices
        movie_indices = [i[0] for i in sig_scores]

        # Top 10 most similar movies
        res = movies_cleaned['Title'].iloc[movie_indices]

        return res.to_dict()
    except Exception as e:
        print(e)
        return "Something Went Wrong!"