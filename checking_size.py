import os
import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
li=os.listdir('train_seb')
newli=[]
path_dir_file=os.path.dirname(os.path.realpath('__file__'))
for f in li:
    image=cv2.imread(path_dir_file+'\\train_seb\\'+f)
    newli.append(image.shape)

li=os.listdir('train_melanoma')
for f in li:
    image=cv2.imread(path_dir_file+'\\train_melanoma\\'+f)
    newli.append(image.shape)
li=os.listdir('train_nevus')
for f in li:
    image=cv2.imread(path_dir_file+'\\train_nevus\\'+f)
    newli.append(image.shape)

print(max(newli))
# max_tuple_index=[i for i in range(len(newli)) if newli[i]==max(newli)]
# print(max_tuple_index)

image=cv2.imread(path_dir_file+'\\train_melanoma\\'+li[420])
cv2.imshow('image',image)
cv2.waitkey(0)
cv2.destroyAllWindows()
# image1=cv2.imread(path_dir_file+'\\train_seb\\'+li[420])
# image1=cv2.resize(image,(256,256),interpolation=cv2.INTER_AREA)
# cv2.imshow('image',image1)
# cv2.waitkwy(0)
# cv2.destroyAllWindows()
# size=(200,200)
# for f in li:
#     i=Image.open(path_dir_file+'\\train_seb\\'+f)
#     i.thumbnail(size)
#     i.save(path_dir_file+'\\thumb_seb\\'+f)

# i=cv2.imread(path_dir_file+'\\thumb_seb\\'+li[0])
# print(i.shape)

# a=np.zeros((1,256,256,3))
# image=cv2.imread(path_dir_file+'\\train_seb\\'+li[0],)
# #image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# image=cv2.resize(image,(256,256),interpolation = cv2.INTER_AREA)
# cv2.imshow("image",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# a[0]=image
# cv2.imshow("image",image)

# cv2.waitKey(0)  
  
# #closing all open windows  
# cv2.destroyAllWindows()  
# from matplotlib import pyplot as plt
# plt.imshow()

#print(a[0])