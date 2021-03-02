from bs4 import BeautifulSoup
import subprocess
import requests

url = input("Enter IMDB url: ")
num_pages = input("Enter number of pages: ")

saved_actor_names = []

with open("../data/actor_names_list.txt", "r") as f:
    saved_actor_names = f.read().splitlines()


actor_names = []
counter = 1
for i in range(int(num_pages)):
    response = requests.get(f"{url}?sort=list_order,asc&mode=detail&page={counter}")
    counter += 1

    soup = BeautifulSoup(response.text, "html.parser")

    for actor in soup.find_all("div", class_="lister-item mode-detail"):
        header = actor.find("a")
        img = header.find("img")
        actor_names.append(img["alt"])


new_actor_names = []
new_actor_counter = 0
with open("actor_names_list.txt", "a") as f:
    for actor in actor_names:
        if actor not in saved_actor_names:
            f.write(actor + "\n")
            new_actor_names.append(actor)
            new_actor_counter += 1

print(new_actor_names)
print(f"{new_actor_counter} new actors added.")