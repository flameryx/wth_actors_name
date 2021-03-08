import pandas as pd
import toolbox as tb
import numpy as np
from sklearn.neighbors import NearestNeighbors

ohe_df = pd.read_csv("../data/ohe_movie_scaled.csv").drop(columns=["Unnamed: 0", "oscarsNom", "goldenGlobesWon", "goldenGlobesNom"])

movie_name = input("Enter a movie title: ")

df_1 = tb.select_features(ohe_df, ["genres", "directors", "countries"])
X_1 = df_1.drop(columns=["tconst", "primaryTitle"])

movie_index = tb.get_movie_index(df_1, movie_name)

model_1 = NearestNeighbors()
model_1.fit(X_1)

distance, index = model_1.kneighbors(X_1.loc[[movie_index]], X_1.shape[0])

distance = distance.tolist()[0]
index = index.tolist()[0]

chosen_ones = []
last_dist = distance[100]

for i, dist in enumerate(distance):
    
    if dist > last_dist: break
    chosen_ones.append(index[i])


first_filter = pd.DataFrame()

for movie in chosen_ones:
    
    first_filter = first_filter.append(ohe_df.loc[[movie]])
    
first_filter.reset_index(inplace=True)


df_2 = tb.select_features(first_filter, ["tconst", "primaryTitle", "genres", "actors", "directors", "writers", "numVotes", "averageRating"])
X_2 = df_2.drop(columns=["tconst", "primaryTitle"])


movie_index = tb.get_movie_index(df_2, movie_name)

model_2 = NearestNeighbors()
model_2.fit(X_2)


distance, index = model_2.kneighbors(X_2.loc[[movie_index]], X_2.shape[0])

distance = distance.tolist()[0]
index = index.tolist()[0]


chosen_ones = []
last_dist = distance[30]

for i, dist in enumerate(distance):
    
    if dist > last_dist: break
    chosen_ones.append(index[i])


tb.print_recommendations_names(df_2, model_2, X_2.loc[[movie_index]], 11)
    