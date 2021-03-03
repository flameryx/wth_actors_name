from bs4 import BeautifulSoup
import toolbox as tb
import requests

actor_iDs = tb.get_actor_id_list()

url = "https://www.imdb.com/name/"
headers = {"Accept-Language": "en-US,en;q=0.5"}

actors_dict = {}
#iD = "nm0000129"

for iD in actor_iDs:
    actor_data = {}

    profile_url = url + f"/{iD}/"
    full_bio_url = profile_url + "bio?ref_=nm_ov_bio_sm"
    awards_url = profile_url + "awards?red_=nm_awd"

    profile_resp = requests.get(profile_url, headers=headers)

    profile_soup = BeautifulSoup(profile_resp.text, "html.parser")

    # Birthday
    actor_data["birth_day"] = profile_soup.find("div", id_="name-born-info").find("time").text

    print("Birth day:")
    print(actor_data["birth_day"])


    actor_data["born_in"] = profile_soup.find("div", id_="name-born-info").find("a")

    print("Born in:")
    print(actor_data["born_in"])



