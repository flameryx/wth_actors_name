import numpy as np

import cv2

import urllib

import tensorflow as tf


#mapping actor to one hot encoded index
name_to_index = {‘Aaron Paul’: 0,
 ‘Aaron Taylor-Johnson’: 1,
 ‘Abigail Breslin’: 2,
 ‘Adam Sandler’: 3,
 ‘Adriana Barraza’: 4,
 ‘Adrianne Palicki’: 5,
 ‘Adrien Brody’: 6,
 ‘Al Pacino’: 7,
 ‘Alan Alda’: 8,
 ‘Alan Arkin’: 9,
 ‘Alan Rickman’: 10,
 ‘Albert Brooks’: 11,
 ‘Albert Finney’: 12,
 ‘Alec Baldwin’: 13,
 ‘Alexandra Daddario’: 14,
 ‘Alexis Thorpe’: 15,
 ‘Alice Eve’: 16,
 ‘Alicia Vikander’: 17,
 ‘Amanda Bynes’: 18,
 ‘Amanda Peet’: 19,
 ‘Amanda Seyfried’: 20,
 ‘Amber Heard’: 21,
 ‘Amy Adams’: 22,
 ‘Amy Ryan’: 23,
 ‘Andrew Garfield’: 24,
 ‘Andrew Lincoln’: 25,
 ‘Andy Garcia’: 26,
 ‘Andy Samberg’: 27,
 ‘Andy Serkis’: 28,
 ‘Angela Bassett’: 29,
 ‘Angelina Jolie’: 30,
 ‘Anjelica Huston’: 31,
 ‘Anna Faris’: 32,
 ‘Anna Kendrick’: 33,
 ‘Anna Paquin’: 34,
 ‘AnnaSophia Robb’: 35,
 ‘Anne Bancroft’: 36,
 ‘Anne Baxter’: 37,
 ‘Anne Hathaway’: 38,
 ‘Annette Bening’: 39,
 ‘Anthony Hopkins’: 40,
 ‘Anthony Mackie’: 41,
 ‘Anthony Perkins’: 42,
 ‘Antonio Banderas’: 43,
 ‘Armin Mueller-Stahl’: 44,
 ‘Arnold Schwarzenegger’: 45,
 ‘Art Carney’: 46,
 ‘Ashley Judd’: 47,
 ‘Ashton Kutcher’: 48,
 ‘Audrey Hepburn’: 49,
 ‘Audrey Tautou’: 50,
 ‘Ava Gardner’: 51,
 ‘Barbra Streisand’: 52,
 ‘Barry Pepper’: 53,
 ‘Ben Affleck’: 54,
 ‘Ben Johnson’: 55,
 ‘Ben Kingsley’: 56,
 ‘Ben Stiller’: 57,
 ‘Benedict Cumberbatch’: 58,
 ‘Benicio Del Toro’: 59,
 ‘Bernie Mac’: 60,
 ‘Bette Midler’: 61,
 ‘Betty White’: 62,
 ‘Bill Hader’: 63,
 ‘Bill Murray’: 64,
 ‘Billy Burke’: 65,
 ‘Billy Crudup’: 66,
 ‘Billy Crystal’: 67,
 ‘Blake Lively’: 68,
 ‘Bob Hoskins’: 69,
 ‘Bonnie Hunt’: 70,
 ‘Brad Pitt’: 71,
 ‘Bradley Cooper’: 72,
 ‘Breckin Meyer’: 73,
 ‘Brenda Blethyn’: 74,
 ‘Brenda Fricker’: 75,
 ‘Brendan Fraser’: 76,
 ‘Brendan Gleeson’: 77,
 ‘Brian Cox’: 78,
 ‘Brie Larson’: 79,
 ‘Brittany Snow’: 80,
 ‘Bruce Davison’: 81,
 ‘Bruce Dern’: 82,
 ‘Bruce Lee’: 83,
 ‘Bruce Willis’: 84,
 ‘Bruno Ganz’: 85,
 ‘Bryan Cranston’: 86,
 ‘Burt Reynolds’: 87,
 ‘Cam Gigandet’: 88,
 ‘Cameron Diaz’: 89,
 ‘Carey Mulligan’: 90,
 ‘Carol Burnett’: 91,
 ‘Cary Elwes’: 92}




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


