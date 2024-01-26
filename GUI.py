from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import test as ai
from threading import *

root = Tk()

windowW = 1200
windowH = 700
imgsize = int(windowW / 2), int(windowH / 1.6)
root.geometry(f"{windowW}x{windowH}")

# Load the image
image = Image.open("./docs/none.gif")
image = image.resize(imgsize, Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.place(x=0, y=50)

# Larg image
image2 = Image.open("./docs/none.gif")
image2 = image2.resize(imgsize, Image.Resampling.LANCZOS)
photo2 = ImageTk.PhotoImage(image2)

label2 = Label(root, image=photo2)
label2.place(x=windowW / 2, y=50)


# for process
def threading():
    t1 = Thread(target=getFile)
    t1.start()


def getFile():
    filename = askopenfilename(filetypes=(("png file", '*.png'),("jpg file", "*.jpg"), ("All files", " *.* "),))
    print(filename)
    if filename=='':
        return ''

    saved.config(text='loading...')
    ent1.insert(END, filename)  # add this
    img2 = Image.open(filename)
    img2 = img2.resize(imgsize, Image.Resampling.LANCZOS)
    img2 = ImageTk.PhotoImage(img2)

    label.configure(image=img2)
    label.image = img2

    ai.resolve_and_plot(filename)

    saved.config(text='/new-img.png')
    img2 = Image.open('./new-img.png')
    img2 = img2.resize(imgsize, Image.Resampling.LANCZOS)
    img2 = ImageTk.PhotoImage(img2)
    label2.configure(image=img2)
    label2.image = img2


ent1 = Entry(root, font=40)
elm = (windowH / 1.4)+50
ent1.place(x=50, y=elm)

saved = Label(root, font=40,text="")
saved.place(x=700, y=elm)

b1 = Button(root, text="انتخاب تصویر", font=40, command=threading)
b1.place(x=300, y=elm)

root.mainloop()
