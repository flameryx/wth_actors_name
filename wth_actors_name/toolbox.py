def get_actor_names_list():
    with open("data/actor_names.txt", "r") as f:
        return f.read().splitlines()

def get_actor_id_list():
    with open("data/actor_ids.txt", "r") as f:
        return f.read().splitlines()

def get_actor_with_id_dict():
    with open("data/actors_with_id", "r") as f:
        actor_id_dict = {}

        actor_with_id_list = f.read().splitlines()

        for actor in actor_with_id_list:
            actor_id = actor.split(" : ")

            actor_id_dict[actor_id[0]] = actor_id[1]
        

        return actor_id_dict