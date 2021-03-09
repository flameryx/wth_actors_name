import pandas as pd 
import toolbox as tb


def find_my_movies(movie_ids_list, df):

    new_df = pd.DataFrame()
    counter = 0

    for movie_id in movie_ids_list:
        new_df = new_df.append(df[df["tconst"] == movie_id])
        counter += 1
        print(counter, end="  ", flush=True)

    
    print()
    print("ALL MY_MOVIES FOUND")
    return new_df



merged_data = pd.read_csv("merged_basics.csv").drop(columns="Unnamed: 0")
movie_ids_list = list(merged_data["tconst"])


# Extracting title_ratings data
title_ratings = pd.read_csv("../../../raw_data/imdb_datasets/films/title_ratings.tsv", sep="\t")
print("FETCHED TITLE_RATINGS")
my_title_ratings = find_my_movies(movie_ids_list, title_ratings)

merged_data = merged_data.set_index("tconst").join(my_title_ratings.set_index("tconst"), on="tconst", how="left")
print("MERGED TITLE_RATINGS")
print()


merged_data.to_csv("merged_basics_ratings.csv")