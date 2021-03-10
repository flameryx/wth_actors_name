from sklearn.preprocessing import MinMaxScaler
import pandas as pd

print("SCALING DATASET")

movies_ohe = pd.read_csv("new_movies_ohe.csv").drop(columns="Unnamed: 0")

scaler = MinMaxScaler().fit(movies_ohe[movies_ohe.columns[2:]])
movies_ohe[movies_ohe.columns[2:]] = scaler.transform(movies_ohe[movies_ohe.columns[2:]])


print()
print("FINISHED SCALING")
print()

movies_ohe.to_csv("../../data/movies_ohe_scaled.csv")