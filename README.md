# What is this actors name? 🤔

A [web app](https://wth-actor-name.herokuapp.com/) for every cinema lover! :heart:

## About

This app is a collaboration of a Data Science and Web Development team as the final project of the [Le Wagon Data Science bootcamp](https://www.lewagon.com/data-science-course/full-time) and [Le Wagon Web Development bootcamp](https://www.lewagon.com/web-development-course/full-time) programs and was completed in less than 10 days

However, this is the repository of the Data Science team. The repository of the Web Development team can be found [here](https://github.com/MargauxPalvini/what-the-hell).

## Features

:camera: :camera_flash: **Image Recognition**&ast;: The user takes and uploads a picture of an actor and the app returns the name and a short bio of them!

:movie_camera: :clapper: **Movie Recommendation**&ast;: The user inputs a movie and the app returns three other movies recommendation!

*&ast; at the moment the models are trained on about 1300 movies and 100 actors and hopefully in the near future more movies and actors will be added*

## Technologies&Tools

For the **image recognition** part we used:

* **Cascade Classifiers** from `OpenCV` to capture the faces in the images

* **Transfer Learning** with **Densenet201** with `Keras` and `Tensorflow`. We implemented part of the pre-trained model in our custom **Convolutional Neural Network** 

For the **movie recommendation** part we used:

* `Beautiful Soup` for web scraping

* `Pandas` and `NumPy` for data wrangling

* **K-Nearest Neighbors** from `scikit-learn`

For the **communication with the Web Development team** we used:

* `FastAPI` for building API

* `Uvicorn` for ASGI server implementation

* `Docker` for hosting the API

* **Google Cloud Platform** for the management of the project

___

**A simple visualization of the technologies used in this project** (*part of the project presentation to general audience*):

![alt text](https://i.ibb.co/w69Ps1Y/Screenshot-from-2021-03-29-11-38-32.png "KNN")

![alt_text](https://i.ibb.co/C1jhC2W/Screenshot-from-2021-03-29-11-42-14.png "Cascade Classifiers")

![alt_text](https://i.ibb.co/Lzjqsz6/Screenshot-from-2021-03-29-11-42-30.png "CNN")

![alt_text](https://i.ibb.co/pXn7rTq/Screenshot-from-2021-03-29-11-43-13.png "Communication")

