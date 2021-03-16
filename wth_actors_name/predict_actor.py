import numpy as np

import cv2

import urllib

import tensorflow as tf


#mapping actor to one hot encoded index
name_to_index = {'Aaron Judge': 0,
 'Aaron Paul': 1,
 'Aaron Taylor-Johnson': 2,
 'Abigail Breslin': 3,
 'Adam Sandler': 4,
 'Adele': 5,
 'Adriana Barraza': 6,
 'Adriana Lima': 7,
 'Adrianne Palicki': 8,
 'Adrien Brody': 9,
 'Akemi Darenogare': 10,
 'Al Pacino': 11,
 'Al Roker': 12,
 'Alan Alda': 13,
 'Alan Arkin': 14,
 'Alan Rickman': 15,
 'Albert Brooks': 16,
 'Albert Finney': 17,
 'Alec Baldwin': 18,
 'Alexander Skarsgard': 19}




#define cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def detect_face(img):

    #setting the cascade classifier
    rectangle = face_cascade.detectMultiScale(img, scaleFactor = 1.1, minNeighbors = 4)

    #if no face is found the
    if len(rectangle) == 0:
        return None

    #setting the right coordinates
    rectangle[:,2:] += rectangle[:,:2]

    return rectangle[0]


def preprocess(url):

    #loading images
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)

    #set output image dimensions
    dim = (100,100)

    #calcultating coordinates of face
    coordinates = detect_face(image)

    #if the detect face function found a face then proceed
    if coordinates is not None:

        #unpacking coordinates
        x1, y1, x2, y2 = coordinates

        #cropping and resizing the image
        resized_image = cv2.resize(image[y1:y2,x1:x2], dim, interpolation = cv2.INTER_AREA)

        #normalizing
        resized_image = resized_image/255

        #adding dimension
        resized_image = resized_image[None, :]

        #saving to cropped_folder
        return resized_image


def predict(model,image):

    index_to_name = {v:key for key,v in name_to_index.items()}

    predicted_index = np.argmax(model.predict(image))

    predicted_name = index_to_name[predicted_index]

    return predicted_name


if __name__ == "__main__":

    model = tf.keras.models.load_model("/Users/elias/code/Final_Project/wth_actors_name/cnn_final_model_3")
    url = "https://upload.wikimedia.org/wikipedia/commons/7/7c/Adele_2016.jpg"
    image = preprocess(url)
    print(predict(image))


