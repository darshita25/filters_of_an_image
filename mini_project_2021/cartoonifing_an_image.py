import cv2
#opencv is used which is a library in python
from tkinter.filedialog import *
#this contains a total of 7 functions
 
#here we are taking the image that we want to cartoonify
#the imread() function is reading the image

pic = askopenfilename()
image = cv2.imread(pic)

#next step is to make the image gray
#we need to make the image grey because we want to get the highlighted part of the image
#highlighted part is important in cartoon image as the cartoon image is made up of highlighted edges
#and smooth colours
#after we get these two image,we need to mask them ,and we get the cartoonified image

#image info
height = image.shape[0]  #rows
width = image.shape[1]   #columns
channels = image.shape[2]  #channels
size1 = image.size  
  
print('Image Height       : ',height)  
print('Image Width        : ',width)  
print('Number of Channels : ',channels)  
print('Image Size  : ', size1) 

grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #code to convert from blue green red to grey
grey = cv2.medianBlur(grey,5) 
edges = cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,5) #0 and 1

#cartoonize
color = cv2.bilateralFilter(image,9,75,75)
cartoon = cv2.bitwise_and(color,color,mask=edges) 
#merge

#resize initial image
width = 400
height = 300
dim = (width, height)  
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)  
print('Resized Dimensions : ', resized.shape)  
cv2.imshow("Resized image", resized)  
            
#resize cartoon image            
width = 400
height = 300 
dim = (width, height)  
resized1 = cv2.resize(cartoon, dim, interpolation=cv2.INTER_AREA)   
print('Resized Dimensions : ', resized.shape)  
cv2.imshow("Resized cartoon filter",resized1)

#resize grey image
width = 400
height = 300 
dim = (width, height)  
resized2 = cv2.resize(grey, dim, interpolation=cv2.INTER_AREA)   
print('Resized Dimensions : ', resized.shape)  
cv2.imshow("Resized black and white filter",resized2)

#resize soft image
width = 400
height = 300 
dim = (width, height)  
resized3 = cv2.resize(color, dim, interpolation=cv2.INTER_AREA)   
print('Resized Dimensions : ', resized.shape)  
cv2.imshow("Resized soft filter",resized3)

#resize edge image
width = 400
height = 300 
dim = (width, height)  
resized4 = cv2.resize(edges, dim, interpolation=cv2.INTER_AREA)   
print('Resized Dimensions : ', resized.shape)   
cv2.imshow("Resized edge filter",resized4)

#save the image on pc 
ss=asksaveasfilename()
cv2.imwrite(ss,cartoon)
ss=asksaveasfilename()
cv2.imwrite(ss,grey)
ss=asksaveasfilename()
cv2.imwrite(ss,color)
ss=asksaveasfilename()
cv2.imwrite(ss,edges)
k=cv2.waitkey(0)

#cartoonified image saved in pc successfully
