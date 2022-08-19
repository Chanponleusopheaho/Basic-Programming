#Importing OpenCV-Python modules
import cv2

#Save image in set directory 
#Read RGB image 

img = cv2.imread(r'C:\Users\Chanponleusophea Ho\OneDrive\Documents\CamTech University\Year 1\Term 1\Basic Programming\Python\Classroom\Session_11\citysketching.jpg')

#Output img with window bame as'image'
cv2.imshow('image', img)

#Maintain output window untill user presses a key
cv2.waitKey(0)

#Destraying present windows on screnn 
cv2.destroyAllWindows()