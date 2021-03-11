import pandas as pd


print("CLEANING SCRAPED DATASET")

dirty_csv = pd.read_csv("new_movies_scraped.csv")

# Clean actors

actors = list(dirty_csv["actors"])

for i, row in enumerate(actors):
    if type(row) != float:
        actors[i] = row.replace("[", "").replace("]", "").replace("'", "").replace(", ", ",")


# Clean awards
awards = list(dirty_csv["awards"])

for i, row in enumerate(awards):
    if type(row) != float:
        row = row.replace(" ", "").replace("\\n", "").replace("[", "").replace("]", "")
        awards[i] = row.replace("'", "").replace("for", "").replace("&", "").replace("Another", "").replace(".", "")


# Clean country
countries = list(dirty_csv["country"])
for i, row in enumerate(countries):
    if type(row) != float:
        countries[i] = row.replace("\n", "").replace("|", ",").replace(" ", "")


# Clean language
languages = list(dirty_csv["language"])

for i, row in enumerate(languages):
    if type(row) != float:
        languages[i] = row.replace("\n", "").replace("|", ",").replace(" ", "")


# Clean Worldwide Gross
ww_gross = list(dirty_csv["worldwideGross"])

for i, row in enumerate(ww_gross):
    if type(row) != float:
        ww_gross[i] = row.replace(" ", "").replace("\n", "")


# Replacing dirty with clean strings
dirty_csv["actors"] = actors
dirty_csv["awards"] = awards
dirty_csv["country"] = countries
dirty_csv["language"] = languages
dirty_csv["worldwideGross"] = ww_gross


# Separate awards string
awards = list(dirty_csv["awards"])

for i, row in enumerate(awards):
    if type(row) != float:
        awards[i] = row.split(",")

n_wins_list = []
n_noms_list = []
oscar_wins_list = []
oscar_noms_list = []
gg_wins_list = []
gg_noms_list = []

for i, row in enumerate(awards):
    
    n_wins = "0"
    n_noms = "0"
    oscar_wins = "0"
    oscar_noms = "0"
    gg_wins = "0"
    gg_noms = "0"

    if type(row) != float:

        if len(row) == 1:
            
            
            if row[0].find("Oscar") != -1:
                if row[0].find("Won") != -1:
                    oscars_i = row[0].find("Oscar")
                    oscar_wins = row[0][len("Won"):oscars_i]

                if row[0].find("Nominated") != -1:
                    oscars_i = row[0].find("Oscar")
                    oscar_noms = row[0][len("Nominated"):oscars_i]


            elif row[0].find("GoldenGlobe") != -1:
                if row[0].find("Won") != -1:
                    gg_i = row[0].find("GoldenGlobe")
                    gg_wins = row[0][len("Won"):gg_i]

                if row[0].find("Nominated") != -1:
                    gg_i = row[0].find("GoldeGlobe")
                    gg_noms = row[0][len("Nominated"):gg_i]
            
            else:   
                wins_i = row[0].find("win")

                if wins_i != -1:
                    n_wins = row[0][:wins_i]
                #row[1] = row[1][wins_i + len("wins"):]

                noms_i = row[0].find("nomination")

                if row[0].find("wins") != -1:
                    n_noms = row[0][wins_i + len("wins"):noms_i]
                else:
                    if wins_i == -1:
                        n_noms = row[0][:noms_i]
                    else:
                        n_noms = row[0][wins_i + len("win"):noms_i]



        # Get wins and nominations if len(row) > 1
        if len(row) > 1:

            if row[0].find("Oscar") != -1:
                if row[0].find("Won") != -1:
                    oscars_i = row[0].find("Oscar")
                    oscar_wins = row[0][len("Won"):oscars_i]

                if row[0].find("Nominated") != -1:
                    oscars_i = row[0].find("Oscar")
                    oscar_noms = row[0][len("Nominated"):oscars_i]


            if row[0].find("GoldenGlobe") != -1:
                if row[0].find("Won") != -1:
                    gg_i = row[0].find("GoldenGlobe")
                    gg_wins = row[0][len("Won"):gg_i]

                if row[0].find("Nominated") != -1:
                    gg_i = row[0].find("GoldenGlobe")
                    gg_noms = row[0][len("Nominated"):gg_i]        


            wins_i = row[1].find("win")
            
            if wins_i != -1:
                n_wins = row[1][:wins_i]
            #row[1] = row[1][wins_i + len("wins"):]

            noms_i = row[1].find("nomination")

            if row[1].find("wins") != -1:
                n_noms = row[1][wins_i + len("wins"):noms_i]
            else:
                if wins_i == -1:
                    n_noms = row[1][:noms_i]
                else:
                    n_noms = row[1][wins_i + len("win"):noms_i]
    


    if n_noms == "Nominated1BAFTAFilmAwar":
        n_noms = "0"

    n_wins_list.append(n_wins)
    n_noms_list.append(n_noms)
    oscar_wins_list.append(oscar_wins)
    oscar_noms_list.append(oscar_noms)
    gg_wins_list.append(gg_wins)
    gg_noms_list.append(gg_noms)


dirty_csv["oscarsWon"] = oscar_wins_list
dirty_csv["oscarsNom"] = oscar_noms_list
dirty_csv["goldenGlobesWon"] = gg_wins_list
dirty_csv["goldenGlobesNom"] = gg_noms_list
dirty_csv["totalWins"] = n_wins_list
dirty_csv["totalNoms"] = n_noms_list


movies_df = pd.read_csv("../../data/main_movie.csv").drop(columns=["Unnamed: 0"])

movies_df = movies_df.append(dirty_csv)


movies_df.drop(columns=["titleType","originalTitle", "isAdult", "endYear"], inplace=True)


# Dealing with NaN values
movies_df = movies_df[movies_df["numVotes"].notnull()]
movies_df = movies_df[movies_df["runtimeMinutes"] != "\\N"]
movies_df["totalNoms"] = movies_df["totalNoms"].fillna(0)
movies_df[["totalNoms"]] = movies_df[["totalNoms"]].replace(to_replace="", value="0")

# Converting to int or float dtypes
movies_df["numVotes"] = movies_df["numVotes"].astype(int)

movies_df["runtimeMinutes"] = movies_df["runtimeMinutes"].astype(int)

movies_df["totalNoms"] = movies_df["totalNoms"].astype(int)


wwg_list = list(movies_df["worldwideGross"])

for i, gross in enumerate(wwg_list):
    
    if type(gross) == int: continue

    elif type(gross) != float:
        wwg_list[i] = int(gross.replace("$", "").replace(",", ""))
        
movies_df["worldwideGross"] = wwg_list

wwg_median = movies_df["worldwideGross"].median()

movies_df["worldwideGross"].fillna(wwg_median, inplace=True)

movies_df["worldwideGross"] = movies_df["worldwideGross"].astype(int)

movies_df.reset_index(inplace=True)
movies_df.drop(columns="index", inplace=True)

print()
print("FINISHED CLEANING")
print()


movies_df.drop_duplicates(inplace=True)

movies_df.to_csv("../../data/main_movie.csv")
movies_df.to_csv("new_movies_clean.csv")