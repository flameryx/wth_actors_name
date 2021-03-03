# Path to virtualenv:
# /home/flameryx/.pyenv/versions/wth_actors_name/lib/python3.8/site-packages/

import pandas as pd

def get_actor_names_list():
    with open("/home/flameryx/code/flameryx/wth_actors_name/wth_actors_name/data/actor_names.txt", "r") as f:
        return f.read().splitlines()

def get_actor_id_list():
    with open("/home/flameryx/code/flameryx/wth_actors_name/wth_actors_name/data/actor_ids.txt", "r") as f:
        return f.read().splitlines()

def get_actor_with_id_dict():
    with open("/home/flameryx/code/flameryx/wth_actors_name/wth_actors_name/data/actors_with_id.txt", "r") as f:
        actor_id_dict = {}

        actor_with_id_list = f.read().splitlines()

        for actor in actor_with_id_list:
            actor_id = actor.split(" : ")

            actor_id_dict[actor_id[0]] = actor_id[1]
        

        return actor_id_dict

def get_actor_basics_csv():
    return pd.read_csv("/home/flameryx/code/flameryx/wth_actors_name/wth_actors_name/data/actor_basics.csv").drop(columns="Unnamed: 0")


def get_movie_names_list():
    with open("/home/flameryx/code/flameryx/wth_actors_name/wth_actors_name/data/movie_names.txt", "r") as f:
        return f.read().splitlines()
