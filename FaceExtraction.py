
#Python 2.7.14
#Opencv 2.4.13
#Haar files from 2.4.9
'''
# This is the main utility for face extraction
# It uses openCV and its premade haarfiles for extracting
# faces from images.

# TODO:
# Add the option to choose face orientation
# Add other landmarks like eyes and whole body (just suing more haarfiles)
'''

from subprocess import call
from PIL import Image
import cv2.cv as cv
import glob
import sys
import os

'''
# The real meat of the file. This is where the faces actually get found and their
# co-ordinates returned
'''
def detect_face(image, faceCascade):
    #variables    
    min_size = (20,20)
    haar_scale = 1.1
    min_neighbors = 3
    haar_flags = 0

    # Equalize the histogram
    cv.EqualizeHist(image, image)

    # Detect the faces
    faces = cv.HaarDetectObjects(
            image, faceCascade, cv.CreateMemStorage(0),
            haar_scale, min_neighbors, haar_flags, min_size
        )
    return faces

'''
#Convert pillow to open cv image
'''
def pillow_to_cvgrey(pillow_image):
    pillow_image = pillow_image.convert('L')
    cv_im = cv.CreateImageHeader(pillow_image.size, cv.IPL_DEPTH_8U, 1)
    cv.SetData(cv_im, pillow_image.tobytes(), pillow_image.size[0]  )
    return cv_im

'''
#Crop the image with pillow
'''
def crop_image(image, bounds):
    # Offset so that we get the entire face
    x_diff=bounds[2]/6
    y_diff=bounds[3]/6

    # Convert from cv to pillow
    crop_area=[bounds[0]-(x_diff), bounds[1]-(y_diff), bounds[0]+bounds[2]+(x_diff), bounds[1]+bounds[3]+(y_diff)]

    return image.crop(crop_area)

'''
#Get all detected faces
'''
def get_faces(img_file):
    # The haarcascade file was selected based on
    # how consistent it was at identifying faces.
    # Your mileage may vary
    faceCascade = cv.Load(os.getcwd() + r'\res\haarfiles\haarcascade_frontalface_alt.xml')

    imgList = glob.glob(img_file)
    if len(imgList)<=0:
        print 'No Images Found'
        return

    for img in imgList:
        pillow_image=Image.open(img)
        cv_im=pillow_to_cvgrey(pillow_image)
        faces=detect_face(cv_im,faceCascade)
        if faces:
            n=1
            for face in faces:
                croppedImage=crop_image(pillow_image, face[0])
                fname,ext=os.path.splitext(img)
                croppedImage.save(fname+'_crop'+str(n)+ext)
                n+=1
        #else:
            # You think you want this on but you dont
            #print 'No faces found:', img 


