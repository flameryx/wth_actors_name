# Path to virtualenv:
# /home/flameryx/.pyenv/versions/wth_actors_name/lib/python3.8/site-packages/

import pandas as pd


def get_actor_names_list():
    with open("/home/flameryx/code/flameryx/wth_actors_name/wth_actors_name/data/actor_names.txt", "r") as f:
        return f.read().splitlines()


def get_actor_basics_csv():
    return pd.read_csv("/home/flameryx/code/flameryx/wth_actors_name/wth_actors_name/data/actor_basics.csv").drop(columns="Unnamed: 0")


def get_movie_names_list():
    with open("/home/flameryx/code/flameryx/wth_actors_name/wth_actors_name/data/movie_names.txt", "r") as f:
        return f.read().splitlines()

def get_movie_names_not_found():
    with open("/home/flameryx/code/flameryx/wth_actors_name/wth_actors_name/data/movie_names_not_found.txt", "r") as f:
        return f.read().splitlines()

def get_main_movie_csv():
        return pd.read_csv("/home/flameryx/code/flameryx/wth_actors_name/wth_actors_name/data/main_movie.csv").drop(columns="Unnamed: 0")


def get_movies_ohe_scaled():
    return pd.read_csv("/home/flameryx/code/flameryx/wth_actors_name/wth_actors_name/data/movies_ohe_scaled.csv").drop(columns="Unnamed: 0")


def get_ohe_movie():
    return pd.read_csv("/home/flameryx/code/flameryx/wth_actors_name/wth_actors_name/data/ohe_movie.csv").drop(columns="Unnamed: 0")


def print_recommendations_verbose(df, model, input_movie, amount):
    
    dist, ind = model.kneighbors(input_movie, amount)

    
    dist = dist.tolist()[0]
    ind = ind.tolist()[0]
        
    for i, el in enumerate(ind):
        print(df.loc[el]["tconst"] + ": " + df.loc[el]["primaryTitle"] + "  :  " + str(dist[i]))
        
    return

def print_recommendations_names(df, model, input_movie, amount):

    dist, ind = model.kneighbors(input_movie, amount)

    
    dist = dist.tolist()[0]
    ind = ind.tolist()[0][1:]
        
    for el in ind:
        print(df.loc[el]["primaryTitle"])
        
    return


def get_movie_id(movieName):
    
    df = pd.read_csv("../wth_actors_name/data/main_movie.csv")
    
    return list(df[df["primaryTitle"] == movieName]["tconst"])[0]


def get_movie_index(df, movieName):

    movie = df[df["primaryTitle"] == movieName]

    if len(movie) == 0:
        return None
    
    return movie.index[0]


"""
This function creates an ohe_df from the features that you select from the ohe_df
"""
def select_features(ohe_df, features):
    
    genres = []
    writers = []
    actors = []
    countries = []
    languages = []
    directors = []
    
    columns = list(ohe_df.columns)
    all_features = ["tconst", "primaryTitle"]
    
    if "genres" in features:
        
        for feat in columns:
            if feat.find("genres") != -1:
                genres.append(feat)
            
    
    if "writers" in features:
        
        for feat in columns:
            if feat.find("writers") != -1:
                writers.append(feat)
    
    
    if "actors" in features:
        
        for feat in columns:
            if feat.find("actors") != -1:
                actors.append(feat)
            
            
    if "directors" in features:
        
        for feat in columns:
            if feat.find("directors") != -1:
                directors.append(feat)
    
    
    if "countries" in features:
        
        for feat in columns:
            if feat.find("country") != -1:
                countries.append(feat)
                
                    
    if "languages" in features:
        
        for feat in columns:
            if feat.find("languages") != -1:
                languages.append(feat)
    
    
    if "startYear" in features:
        all_features.append("startYear")
    
    if "runtimeMinutes" in features:
        all_features.append("runtimeMinutes")
        
    if "averageRating" in features:
        all_features.append("averageRating")
        
    if "numVotes" in features:
        all_features.append("numVotes")
        
    if "worldwideGross" in features:
        all_features.append("worldwideGross")

    if "oscarsWon" in features:
        all_features.append("oscarsWon")
        
    if "totalWins" in features:
        all_features.append("totalWins")
        
    if "totalNoms" in features:
        all_features.append("totalNoms")
        
    
    all_features += genres + writers + actors + countries + languages + directors
    
    return ohe_df[all_features]