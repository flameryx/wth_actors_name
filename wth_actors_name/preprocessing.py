import cv2
import os
import glob

def load_images_from_folder(folder, number_of_images):
    images = []

    counter = 0
    #fraction is the fraction of the total image dataset to be loaded


    #iterating through the image files in the folder
    for image_number in range(len(os.listdir(folder))):

        if counter < int(number_of_images*1.5):

            filename = str(image_number) + ".jpg"

            # loading the image in greyscale
            img = cv2.imread(os.path.join(folder,filename),cv2.IMREAD_GRAYSCALE)

            #if image with correct filename was found then append to image list
            if img is not None:
                images.append(img)



                counter += 1

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



def save_preprocessed_images(origin_folder,cropped_folder, number_of_images):

    #loading images
    image_list = load_images_from_folder(origin_folder, number_of_images)

    #set output image dimensions
    dim = (100,100)

    counter = 0

    for i in range(len(image_list)):

        #calcultating coordinates of face
        coordinates = detect_face(image_list[i])


        #if the detect face function found a face then proceed
        if coordinates is not None:

            if counter < number_of_images:

                counter += 1

                #unpacking coordinates
                x1, y1, x2, y2 = coordinates

                #cropping and resizing the image
                resized_image = cv2.resize(image_list[i][y1:y2,x1:x2], dim, interpolation = cv2.INTER_AREA)

                #saving to cropped_folder
                cv2.imwrite(os.path.join(cropped_folder, str(i) + ".jpg"), resized_image)




def listdir_nohidden(path):
    return glob.glob(os.path.join(path, '*'))


def full_folder_preprocessing(origin, destination, number_of_images = 20):

    folders_in_origin = listdir_nohidden(origin)

    #define cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    #iterate over the names of the actors in the main folder:
    for actor_name in folders_in_origin:

        #only select last part of the filepath in folders_in_origin which is the actor name
        actor_name = os.path.basename(os.path.normpath(actor_name))

        #create a new subfolder named after the actor
        os.mkdir(os.path.join(destination, actor_name))

        #save path of the subfolder
        destination_subfolder = os.path.join(destination,actor_name)

        #preprocess images for one actor and save them too destination subfolder
        save_preprocessed_images(os.path.join(origin,actor_name), destination_subfolder, number_of_images)


