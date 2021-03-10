FROM python:3.8.6-buster

COPY api /api
COPY requirements.txt /requirements.txt
COPY recommender_function.py /recommender_function.py
COPY toolbox.py /toolbox.py
COPY wth_actors_name/data /wth_actors_name/data
COPY predict_actor.py /predict_actor.py
COPY cnn_final_model_3 /cnn_final_model_3

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
