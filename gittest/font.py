import tkinter as tk
from PIL import Image, ImageDraw, ImageFont

root = tk.Tk()
root.title("MyFont")

font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf")
im = Image.new("RGB", (200, 200), "white")
d = ImageDraw.Draw(im)
d.line(((0, 100), (200, 100)), "gray")
d.line(((100, 0), (100, 200)), "gray")
d.text((100, 100), "Quick", fill="black", anchor="ms", font=font)
root.mainloop()
