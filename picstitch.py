import numpy as np
import cv2
import glob2
import imutils
n=0
image_paths=glob2.glob(('samples/des'+str(n)+'/*.jpeg').replace(' ',''))
images=[]

for image in image_paths:
    img=cv2.imread(image)
    images.append(img)
    s=str(image)+'-Input'
    cv2.imshow(s,img)

imageStitcher=cv2.Stitcher_create()

error,stitchedimage=imageStitcher.stitch(images)
# print('\nNumber of Images= '+str(len(images)))

if not error:
    # cv2.imwrite(('result/stitched_des'+str(n)+'.png').replace(' ',''),stitchedimage)
    cv2.imshow('stitched image',stitchedimage)
    cv2.waitKey(0)
else:
    print(error)