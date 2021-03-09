import pandas as pd

"""Converts columns which contain strings of values as elements, into OneHotEncode"""

def create_features_ohe(df, column):
    column_list = list(df[column])
    
    # Split values
    for i, row in enumerate(column_list):
        if type(row) != float:
            column_list[i] = row.split(",")
    
    # Create list of unique values
    all_features = []
    for row in column_list:
        
        if type(row) != float:
            for feature in row:
                if feature not in all_features:
                    all_features.append(feature)
            
    all_features.sort()
    
    
    # Create a column for each value in all_features
    for feature in all_features:
        df[f"{column}_{feature.lower()}"] = 0
        
    
    # OneHotEncoding for each row
    for i, row in enumerate(column_list):
        
        if type(row) != float:
            for feature in row:

                df.loc[i, f"{column}_{feature.lower()}"] = 1 

    return


print("ONE HOT ENCODING DATASET")

movies_clean = pd.read_csv("new_movies_clean.csv").drop(columns="Unnamed: 0")

movies_clean.drop_duplicates(inplace=True)


create_features_ohe(movies_clean, "genres")

create_features_ohe(movies_clean, "directors")

create_features_ohe(movies_clean, "writers")

create_features_ohe(movies_clean, "actors")

create_features_ohe(movies_clean, "country")

create_features_ohe(movies_clean, "language")


movies_clean = movies_clean.drop(columns=["genres", "directors", "writers", "actors", "country", "language", "awards", "budget"])

print()
print("FINISHED ONE HOT ENCODING")
print()

movies_clean.to_csv("new_movies_ohe.csv")