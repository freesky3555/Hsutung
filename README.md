# README
### Creat time   
> Tue 12 Jan 2021 05:  17:  42 AM CST

## 
This is my first project for github. First programe Name is Hello world.
On here I will learn and Familiar with various git command. This is a begaining.
_I'm a **student**, I will always be a **student**._

## Local development

1. _Use python3 to run Helloworld.py_
2. ~~Open index.html in your browser.~~

## Learning progress

1. Use GitHub Help
2. Learning `git clone`
3. Learning `git add`
4. Learning `git commit`
5. Learning `git pull`
6. Learning `git push`
7. Learning `git branch`
8. Learning `git rebase`
9. Learning `git reset`

## Helloworld.py

```
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
```
