from matplotlib import pyplot as plt
import zipfile
from zipfile import ZipFile
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np


def open_and_list(zip_file,format = 'pil'):
    """"Opens a zip file and appends image files to a list
      return list of files"""

    images = []  # np.array used for image with cv

    with ZipFile(zip_file,'r') as zfile: # select your zip file to open
        for entry in zfile.infolist():
            with zfile.open(entry) as file:
                print(file.name)
                if format == 'cv':
                    print('Appending opencv image object from: {}'.format(file))
                    pil_image = Image.open(file)
                    # covnert image to gray
                    opencvImage = cv.cvtColor(np.array(pil_image), cv.COLOR_BGR2GRAY)
                    images.append(opencvImage)
                else:
                    print('Making a Image object from: {}'.format(file))
                    pil_image = Image.open(file)
                    print('Appending a Image object list')
                    images.append(pil_image)


    return images

def face_detect(list,classifier):

    rectangle_coordinates = []
    for image in list:
        haar_cascade = cv.CascadeClassifier(classifier)
        faces_rect = haar_cascade.detectMultiScale(image)
        print('Number of faces found: {}'.format(len(faces_rect)))

        for (x,y,w,h) in faces_rect:
            cv.rectangle(image,(x,y), (x+w, y+h), (0,255,0), thickness = 2)
            ## append each rect coordinate into a list of tuples
            rectangle_coordinates.append((x,y,w,h))
            print(len(rectangle_coordinates))
    return rectangle_coordinates

        #cv.imshow('Detected Faces',image) ---used to check images with faces
        #cv.waitKey(0)

def resize_opencv(image,scale_percent):
    """Returns a resized image when an image does not fit
        in the users scree"""

    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv.resize(image, dim, interpolation = cv.INTER_AREA)
    print('Resized Dimensions : ',resized.shape)
    return resized

def croping_faces(faces,listpil): #dont forget to add faces param back

    for im in listpil:
        plt.imshow(im)
        for (x, y, w, h) in faces:
            im_crop = im.crop((x, y, (x+w), (y+h)))
            plt.imshow(im_crop)




listcv = open_and_list('small_img.zip','cv')
listpil = open_and_list('small_img.zip')
faces = face_detect(listcv,'haar_face.xml')
croping_faces(faces,listpil) # dont forget to add faces param back
