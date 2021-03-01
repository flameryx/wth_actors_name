from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
def find_actor_by_pic(url = "https://ca-times.brightspotcdn.com/dims4/default/2a094f0/2147483647/strip/true/crop/311x512+0+0/resize/840x1383!/quality/90/?url=https%3A%2F%2Fcalifornia-times-brightspot.s3.amazonaws.com%2Fe4%2Fad%2F8a7dabb97bf844d7684968f611e5%2Fsdut-in-this-april-27-2007-file-ph-20160828"
):
    # image = Image.open(url)
    # model = joblib.load('modeljoblib')
    # pred = model.predict(image)
    return {"actor": "Woody Harrelson"}


@app.get("/movie_recommender")
def movie_recommender(movie = "Natural Born Killers"):
    # model = joblib.load('modeljoblib')
    # pred = model.predict(image)

    return {"similar_movie": "Reservoir Dogs"}

@app.get("/test")
def test(param):
    # model = joblib.load('modeljoblib')
    # pred = model.predict(image)

    return {"Status": "OK"}
