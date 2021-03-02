# Loads all images from a folder

import cv2
import os
def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename), cv2.IMREAD_GRAYSCALE)
        if img is not None:
            #th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,25,7)
            width = 400
            height = 400 # keep original height
            dim = (width, height)

            # resize image
            resized = cv2.resize(th3, dim, interpolation = cv2.INTER_AREA)
            images.append(resized)
    return images
folder="NewRecipes/NewPhotos"

imgs = load_images_from_folder(folder)