import cv2
import os
import glob

def load_images_from_folder(folder, fraction):
    images = []

    #fraction is the fraction of the total image dataset to be loaded

    #iterating through the image files in the folder
    for image_number in range(int(len(os.listdir(folder))*fraction)):
        filename = str(image_number) + ".jpg"

        # loading the image in greyscale
        img = cv2.imread(os.path.join(folder,filename),cv2.IMREAD_GRAYSCALE)

        #if image with correct filename was found then append to image list
        if img is not None:
            images.append(img)

    return images

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


def save_preprocessed_images(origin_folder,cropped_folder, fraction):

    #loading images
    image_list = load_images_from_folder(origin_folder,fraction)

    #set output image dimensions
    dim = (100,100)

    for i in range(len(image_list)):

        #calcultating coordinates of face
        coordinates = detect_face(image_list[i])


        #if the detect face function found a face then proceed
        if coordinates is not None:

            #unpacking coordinates
            x1, y1, x2, y2 = coordinates

            #cropping and resizing the image
            resized_image = cv2.resize(image_list[i][y1:y2,x1:x2], dim, interpolation = cv2.INTER_AREA)


            #saving to cropped_folder
            cv2.imwrite(os.path.join(cropped_folder, str(i) + ".jpg"), resized_image)


#this function is essential os.listdir without showing hidden files


def listdir_nohidden(path):
    return glob.glob(os.path.join(path, '*'))


def full_folder_preprocessing(origin, destination, fraction = 1):

    folders_in_origin = listdir_nohidden(origin)

    #iterate over the names of the actors in the main folder:
    for actor_name in folders_in_origin:

        #only select last part of the filepath in folders_in_origin which is the actor name
        actor_name = os.path.basename(os.path.normpath(actor_name))

        #create a new subfolder named after the actor
        os.mkdir(os.path.join(destination, actor_name))

        #save path of the subfolder
        destination_subfolder = os.path.join(destination,actor_name)

        #preprocess images for one actor and save them too destination subfolder
        save_preprocessed_images(os.path.join(origin,actor_name), destination_subfolder, fraction)
