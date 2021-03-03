from bs4 import BeautifulSoup
import subprocess
import requests
import time


n_movies = int(input("Enter how many movie titles: "))
genre = input("Enter the genre: ").lower()
start = 1

with open("../../data/movie_names.txt", "r") as f:
    saved_movie_names = f.read().splitlines()

headers = {"Accept-Language": "en-US,en;q=0.5"}

movie_names = []
counter = 0

while counter < n_movies:
    response = requests.get(f"https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres={genre}&sort=user_rating,desc&start={start}&ref_=adv_nx", headers=headers)
    start += 50
    #time.sleep(10)

    soup = BeautifulSoup(response.text, "html.parser")

    for movie in soup.find_all("h3", class_="lister-item-header"):
        title = movie.find("a").text
        year = movie.find("span", class_="lister-item-year").text
        movie_names.append(title + " " + year)
        counter += 1

        if counter > n_movies: break

new_movie_names = []
new_movie_counter = 0
with open("../../data/movie_names.txt", "a") as f:
    for movie in movie_names:
        if movie not in saved_movie_names:
            f.write(movie + "\n")
            new_movie_names.append(movie)
            new_movie_counter += 1

print(new_movie_names)
print(f"{new_movie_counter} new movies added.")
