from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import toolbox as tb
import recommender_function as rf
import pandas as pd
import predict_actor as pa
import tensorflow as tf

#load actor recognition model
model = tf.keras.models.load_model("cnn_final_model_3")

# Load ohe_df data
ohe_df = pd.read_csv("wth_actors_name/data/ohe_movie_scaled.csv")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"actor": "Woody Harrelson"}

@app.get("/find_actor_by_pic")
def find_actor_by_pic(url = "https://upload.wikimedia.org/wikipedia/commons/7/7c/Adele_2016.jpg"):

    image = pa.preprocess(url)

    return {"actor": pa.predict(model,image)}


@app.get("/movie_recommender")
def movie_recommender(movie = "Iron Man"):
    # model = joblib.load('modeljoblib')
    # pred = model.predict(image)

    recommendations = rf.recommend_movies(ohe_df, movie)

    if recommendations == None:
        return {"ERROR" : "This movie is not in the database. Cannot make recommendations."}

    counter = 1

    movie_dict = {}

    for rec in recommendations:
        movie_dict[counter] = rec
        counter += 1

    return movie_dict


# @app.get("/test")
# def test(param):
#     # model = joblib.load('modeljoblib')
#     # pred = model.predict(image)

#     return {"Status": "OK"}
