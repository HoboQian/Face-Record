import cv2
import os

face_cascade = cv2.CascadeClassifier()
face_cascade.load('F:/Work_File_share/Face_Recognize_hobo/haarcascade_frontalface_default.xml')
graydirpath = 'F:/Work_File_share/Face_Recognize_hobo/at'

names=[]

def read_images(path):
	for dirname, dirnames, filenames in os.walk(path):

		for subdirname in dirnames:

			print ("==================================================")
			names.append(subdirname)

			print (subdirname + ":")
			subject_path = os.path.join(dirname, subdirname)

			grayPath=os.path.join(graydirpath, subdirname)

			isExists = os.path.exists(grayPath)
			if isExists == False:
				os.makedirs(grayPath)
			count = 0
			for filename in os.listdir(subject_path):
				if (filename == ".directory"):
					print ("continue")
					continue
				filepath = os.path.join(subject_path, filename)
				img = cv2.imread(os.path.join(subject_path, filename))
				if len(img) == 0:
					print ("imread ERROR")
					continue
				gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
				faces = face_cascade.detectMultiScale(gray, 1.3, 5)
				if len(faces) == 0:
					print (filename + " can't detect face.")
				else:
					for(x,y,w,h) in faces:
						f = cv2.resize(gray[y:y+h,x:x+w],(200, 200))
						cv2.imwrite(grayPath+'/%s.pgm'%str(count), f)
					print (count)
					count = count + 1

if __name__ == "__main__":
	read_images('F:/Work_File_share/Face_Recognize_hobo/raw')


