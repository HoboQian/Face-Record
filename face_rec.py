import cv2
import os
import time
import numpy as np

author__ = 'hobo'
# -*- coding: utf-8 -*-

cascade_xml = "D:\Python\sample code\data\haarcascades\haarcascade_frontalface_default.xml"
cascade_fn = cv2.CascadeClassifier(cascade_xml)
RootPath = 'F:/Work_File_share/Face_Recognize_hobo/raw/'

def face_record(path):
    print("Let's ROCK !!!!!!")
    camera = cv2.VideoCapture(0)

    num = 0
    while (True):
        ret, img = camera.read()
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # gray2 = cv2.equalizeHist(gray)
        cv2.imshow("test1", img)
        faces = cascade_fn.detectMultiScale(img, 1.3, 5)
        if faces is not ():
            cv2.imwrite(path + '/%s.jpg'%str(num),img)
            print (num)
            num = num + 1

        # time.sleep(1)

        if cv2.waitKey(5) == 27:
            break

        if num == 100:
            break

    cv2.destroyAllWindows()

def main():
    print("In  main func, jump to record face")
    folder_Name = raw_input ("Input your name: ")
    print ("Your name is " + folder_Name)
    folder_path = os.path.join(RootPath, folder_Name)
    isExists = os.path.exists(folder_path)
    if isExists == False:
        os.makedirs(folder_path)

    face_record(folder_path)

if __name__ == '__main__':
    main()