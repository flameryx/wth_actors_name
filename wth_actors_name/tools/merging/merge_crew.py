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



merged_data = pd.read_csv("merged_basics_ratings.csv")
movie_ids_list = list(merged_data["tconst"])


# Extracting title_crew data
title_crew = pd.read_csv("../../../raw_data/imdb_datasets/films/title_crew.tsv", sep="\t")
print("FETCHED TITLE_CREW")
my_title_crew = find_my_movies(movie_ids_list, title_crew)

merged_data = merged_data.join(my_title_crew.set_index("tconst"), on="tconst", how="left")
print("TITLE CREW MERGED")
print()


# Save dataframe in csv file
merged_data.to_csv("new_movies_data.csv")