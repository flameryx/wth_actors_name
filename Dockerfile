FROM python:3.8.6-buster

COPY api /api
COPY requirements.txt /requirements.txt
COPY recommender_function.py /recommender_function.py
COPY toolbox.py /toolbox.py
COPY wth_actors_name/data /wth_actors_name/data

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
