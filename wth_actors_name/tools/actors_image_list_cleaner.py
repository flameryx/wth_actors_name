"""Runs throug all the images folders in the celebrity image database, finds the celebrities that are actors and that are
   inside the actors_list.txt and moves them to the actors folders"""

# This code should be run from Windows and with the PHOENIX hard drive (D:) connected

import os
import subprocess
import shutil

with open("D:/LeWagon/final_project/actors_list.txt", "r") as f:
    saved_actors_list = f.read().splitlines()

path = "D:/LeWagon/final_project/data/celebrities"

img_dirs = os.listdir(path)

actor_counter = 0

for dir_name in img_dirs:
    img_dir_list = os.listdir(f"{path}/{dir_name}")
    
    for celebrity in img_dir_list:
        if celebrity in saved_actors_list:
            shutil.move(f"D:/LeWagon/final_project/data/celebrities/{dir_name}/{celebrity}", f"D:/LeWagon/final_project/data/actors/{celebrity}")
            actor_counter += 1
            print(celebrity)