#!/usr/bin/python3

#############################################################
# FileName:Helloworld.py                                    #
# CreatTime: Wed 06 Jan 2021 07:24:11 AM CST                #
#############################################################
import tkinter as tk
from PIL import ImageTk,Image  

def typeit(widget, index, string):
   if len(string) > 0:
      widget.insert(index, string[0])
      if len(string) > 1:
         # compute index of next char
         index = widget.index("%s + 1 char" % index)

         # type the next character in half a second
         widget.after(130, typeit, widget, index, string[1:])

root = tk.Tk()
text = tk.Text(root, width=40, height=8, font=("Arial",25), fg = "#8B0000")
canvas = tk.Canvas(root, width = 580, height = 1200)  
canvas.pack()  
root.img = ImageTk.PhotoImage(Image.open("Your_image.jpeg"))  
canvas.create_image(20, 20, anchor=NW, image=img) 
text.pack(fill="both", expand=True)
typeit(text, "1.0", "\t\t\nHello, World!\nHello, 2021!\nHello, GitHub!\nThis is a greeting from CITY YuCi(榆次) !!")

root.mainloop()
#############################################################
# END
