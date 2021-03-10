./merging/merge.sh

echo "ALL MERGING IS DONE"
echo "======================================================================"
python web_scraping/imdb_movie_scraper.py

echo "ALL SCRAPING IS DONE"
echo "======================================================================"


rm merging/new_movies_data.csv

./data_preparation/prepare.sh

echo "ALL DATA PREPARATION IS DONE"
echo "NEW DATASET ADDED IN wth_actors_name/data/movies_ohe_scaled.csv"