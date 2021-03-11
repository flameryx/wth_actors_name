cd merging
./merge.sh
cd ..

echo "ALL MERGING IS DONE"
echo "======================================================================"

cd web_scraping
python imdb_movie_scraper.py
cd ..

rm merging/new_movies_data.csv

echo "ALL SCRAPING IS DONE"
echo "======================================================================"

cd data_preparation
./prepare.sh
cd ..

echo "ALL DATA PREPARATION IS DONE"
echo "NEW DATASET ADDED IN wth_actors_name/data/movies_ohe_scaled.csv"