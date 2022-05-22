from PIL import Image 
import PIL 
  
# creating a image object (main image) 
im1 = Image.open(r"D:\\New folder\\image_merge\\uploadimg\\static\\images\\shirt.jpg") 
  
# save a image using extension
im1.save("logo.jpg")
