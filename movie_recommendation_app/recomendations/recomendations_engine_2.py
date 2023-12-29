import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_recomendations(description):
    try:
        """
            In this function, the CountVectorizer vectorizer is used to convert product descriptions \
            into vectors, and then cosine similarity is calculated between the vectors to \
            determine product similarity.

        """

        df = pd.read_csv("movie_recommendation_app/recomendations/Hydra-Movie-Scrape.csv")

        features = ['Title','Cast','Genres','Writers']

        def combine_features(row):
            return row['Title'] +" "+row['Cast']+" "+row["Genres"]+" "+row["Writers"]

        for feature in features:
            df[feature] = df[feature].fillna('')
        df["combined_features"] = df.apply(combine_features,axis=1)
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(df["combined_features"])
        cosine_sim = cosine_similarity(count_matrix)

        def get_title_from_index(index):
            return df[df.index == index]["Title"].values[0]

        def get_index_from_title(title):
            return df[df.Title == title]["index"].values[0]

        movie_user_likes = description #"Avatar"
        movie_index = get_index_from_title(movie_user_likes)
        similar_movies =  list(enumerate(cosine_sim[movie_index]))

        sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]

        i=0
        response = list()
        print("Top 5 similar movies to "+movie_user_likes+" are:\n")
        for element in sorted_similar_movies:
            response.append(get_title_from_index(element[0]))
            print(get_title_from_index(element[0]))

            i=i+1
            if i>=5:
                break
        return response 
    except Exception as e:
        print(e)
        return "Something Went Wrong!"


#ref: https://medium.com/@sumanadhikari/building-a-movie-recommendation-engine-using-scikit-learn-8dbb11c5aa4b