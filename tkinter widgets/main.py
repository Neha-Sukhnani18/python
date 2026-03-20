from tkinter import * 
from PIL import Image, ImageTk
root=Tk()
root.title('image')
root.geometry('400x400')
#now use image.open to open and identify the given image file
upload = Image.open("roses.jpg")
#convert this image into tkinter compatible image
image = ImageTk.PhotoImage(upload)
#add image to tkinter label
label = Label(root, image= image, height=350, wigth=300)
label.place(x=50,y=0)
label2=Label(root, text="this is how you add an image in tkinter")
label2.place(x=40,y=360)
root.mainloop()