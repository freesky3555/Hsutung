#!/usr/bin/python3

#############################################################
# FileName:Helloworld.py                                    #
# CreatTime: Wed 06 Jan 2021 07:24:11 AM CST                #
#############################################################
import tkinter as tk

def typeit(widget, index, string):
   if len(string) > 0:
      widget.insert(index, string[0])
      if len(string) > 1:
         # compute index of next char
         index = widget.index("%s + 1 char" % index)

         # type the next character in half a second
         widget.after(250, typeit, widget, index, string[1:])

root = tk.Tk()
text = tk.Text(root, width=40, height=8)
text.pack(fill="both", expand=True)
typeit(text, "1.0", "Hello, World!\nHello, 2021!\nHello, GitHub!\nThis is a greeting from City YUCI!")

root.mainloop()
#############################################################
# END
