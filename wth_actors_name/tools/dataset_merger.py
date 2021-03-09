import pandas as pd 
import toolbox as tb


def find_new_movies(movie_names, df):

    not_found = tb.get_movie_names_not_found()
    old_titles = list(movie_csv["primaryTitle"])
    new_titles = []

    for movie in movie_names:

        if movie.find("(I)") != -1:
            movie = movie.replace(" (I)", "")
        elif movie.find("(II)") != -1:
            movie = movie.replace(" (II)", "")
        elif movie.find("(III)") != -1:
            movie = movie.replace(" (III)", "")
            
        if movie[:-7] not in old_titles:
            if movie not in not_found:
                new_titles.append(movie)
    
    return new_titles


def find_movies_id(movie_names, df):

    new_df = pd.DataFrame()
    counter = 0

    with open("../data/movie_names_not_found.txt", "a") as f:

        for movie in movie_names:

            if movie.find("(I)") != -1:
                movie = movie.replace(" (I)", "")
            elif movie.find("(II)") != -1:
                movie = movie.replace(" (II)", "")
            elif movie.find("(III)") != -1:
                movie = movie.replace(" (III)", "")
            
            title = movie[:-7]
            year = movie[-5:-1]

            new_row = df[(df["titleType"] == "movie") & (df["primaryTitle"] == title) & (df["startYear"] == year)]
            if len(new_row) == 0:
                f.write(movie + "\n")

            new_df = new_df.append(new_row)
            counter += 1
            print(counter, end="  ", flush=True)

    print()
    return new_df


def find_my_movies(movie_ids_list, df):

    new_df = pd.DataFrame()
    counter = 0

    for movie_id in movie_ids_list:
        new_df = new_df.append(df[df["tconst"] == movie_id])
        counter += 1
        print(counter, end="  ", flush=True)

    
    print()
    print("ALL MY_MOVIES FOUND")
    print()
    return new_df
        


movie_names = tb.get_movie_names_list()
movie_csv = tb.get_main_movie_csv()

movie_names = find_new_movies(movie_names, movie_csv)

if len(movie_names) == 0:
    print("There are no new movies to add.")
    quit()
else:
    print("There are " + str(len(movie_names)) + " new movies.")

# Extracting title_basics data
title_basics = pd.read_csv("../../raw_data/imdb_datasets/films/title_basics.tsv", sep="\t")
print("FETCHED TITLE_BASICS")

all_movie_data = find_movies_id(movie_names, title_basics)

if len(all_movie_data) == 0:
    print("None of the new movies were found.")
    quit()

print("ALL MOVIE_IDS FOUND")
print()

movie_ids_list = list(all_movie_data["tconst"])


# Extracting title_ratings data
title_ratings = pd.read_csv("../../raw_data/imdb_datasets/films/title_ratings.tsv", sep="\t")
print("FETCHED TITLE_RATINGS")
my_title_ratings = find_my_movies(movie_ids_list, title_ratings)

all_movie_data = all_movie_data.set_index("tconst").join(my_title_ratings.set_index("tconst"), on="tconst", how="left")
print("MERGED TITLE_RATINGS")


# Extracting title_crew data
title_crew = pd.read_csv("../../raw_data/imdb_datasets/films/title_crew.tsv", sep="\t")
print("FETCHED TITLE_CREW")
my_title_crew = find_my_movies(movie_ids_list, title_crew)

all_movie_data = all_movie_data.join(my_title_crew.set_index("tconst"), on="tconst", how="left")
print("TITLE CREW MERGED")
print("=============================================")


# Save dataframe in csv file
all_movie_data.to_csv("../data/new_movies_data.csv")