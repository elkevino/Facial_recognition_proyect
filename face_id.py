from matplotlib import pyplot as plt
import zipfile
from zipfile import ZipFile
from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np


def open_to_img(zip_file,format):
    """"Opens a zip file and appends image files to a list
      return list of files"""

    images = []  # np.array used for image with cv

    with ZipFile(zip_file,'r') as zfile: # select your zip file to open
        for entry in zfile.infolist():
            #maybe put the process here for cv files
            if format == 'cv':
                data = zfile.read(entry)
                print('Making a cv object list')
                # img = cv.imread(file)
                #images.append(cv.cvtColor(img, cv.COLOR_BGR2GRAY))
                images.append(cv.imdecode(np.frombuffer(data, np.uint8), 1))
                print(len(images))
            else:
                with myzip.open(entry) as file:
                    print('Making a Image object')
                    img = Image.open(file)
                    print('Making a Image object list')
                    images.append(img)

    return images

def convert_to_array(zip_file):
        images = []
        for image in open_to_img(zip_file,'cv'):
            print('In goes .....',type(image))
            open_cv_image = np.array(image)
            #array =cv.imdecode(np.frombuffer(image, np.uint8), 1)
            print('Out comes .....',type(open_cv_image))


open_to_img('small_img.zip','cv')
#convert_to_array('small_img.zip')
# def make_images():
#     grays = []
#     colored = []
#     for image in images:
#         print('creating gray image')
#         grays.append(cv.cvtColor(image, cv.COLOR_BGR2GRAY ))
#         print('creating color image')
#         colored.append(Image.fromarray(image,"RGB"))
#
#     return grays,colored
#
#
# def show_image(images):
#
#     colored[0].show()
#     cv.imshow('GFG', grays[0])
#     cv.waitKey(0)
#     cv.destroyAllWindows()
#     return grays,colored
#
#
#
#
#
# #
# # for image in images:
# # print('going to open {}'.format(image))
# # print('closed')
# # # with myzip.open('a-0.png') as myfile:
# # # #data = myzip.read('a-0.png')
# # #     with Image.open(myfile) as image_crop:
# # #         image_crop.convert('L')
# # #         image_crop.show()
# #show_image(open_zip('small_img.zip'))
