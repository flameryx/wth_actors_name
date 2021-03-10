import toolbox as tb
import pandas as pd
from bs4 import BeautifulSoup
import requests

movies_df = pd.read_csv("../merging/new_movies_data.csv").drop(columns="Unnamed: 0")

movies_id_list = list(movies_df["tconst"])

ids_dict = {}
movie_counter = 0

print("SCRAPING ADDITIONAL MOVIE DATA")

for movie_id in movies_id_list:
    
    inner_dict = {}
    
    url = f"https://www.imdb.com/title/{movie_id}/"
    headers = {"Accept-Language": "en-US,en;q=0.5"}

    response = requests.get(url, headers=headers)
    
    while(response.status_code != 200):
        response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, "html.parser")


    # TOP 10 Actors Scraper
    cast_table = soup.find("table", class_="cast_list")
    mvp_actors = []
    counter = 0
    
    if cast_table == None: continue
        
    for row in cast_table.find_all("tr")[1:]:

        row_data = row.find_all("td")
        
        if len(row_data) < 4: break
            
        actor = (row_data[1].text)[2:-2]
        mvp_actors.append(actor)

        counter += 1

        if (counter == 10): break

    inner_dict["actors"] = mvp_actors
    #print(mvp_actors)

    # Awards Scraper
    awards = soup.find_all("span", class_="awards-blurb")
    awards_blurb = []

    for blurb in awards:
        awards_blurb.append(blurb.text)

        
    inner_dict["awards"] = awards_blurb
    #print(awards_blurb)

    # Other data scraper
    for block in soup.find_all("div", class_="txt-block"):

        h4 = block.find("h4", class_="inline")

        if h4 != None:
            if h4.text == "Country:":
                countries = block.text[9:]

                inner_dict["country"] = countries

            if h4.text == "Language:":
                languages = block.text[10:]

                inner_dict["language"] = languages

            if h4.text == "Budget:":
                budget = block.text[8:].split("\n")[0]
                
                inner_dict["budget"] = budget

            if h4.text == "Cumulative Worldwide Gross:":
                ww_gross = block.text[28:]

                inner_dict["worldwideGross"] = ww_gross
                
    ids_dict[movie_id] = inner_dict
    
    movie_counter += 1
    print(movie_counter, end="  ", flush=True)

print()
print("FINISHED SCRAPING")
print()


new_df = pd.DataFrame.from_dict(ids_dict, orient="index")


main_movies = movies_df.set_index("tconst").join(new_df, on="tconst", how="left")


main_movies.to_csv("../data_preparation/new_movies_scraped.csv")
