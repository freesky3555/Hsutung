from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()  
canvas = Canvas(root, width = 580, height = 1200)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("Your_image.jpeg"))  
canvas.create_image(20, 20, anchor=NW, image=img) 


root.mainloop() 
