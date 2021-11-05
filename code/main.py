from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
def open_file():
    path = askopenfilename(filetypes=[("JPG images", "*.jpg"), ("GIF image","*.gif"), ("JPEG image","*.jpeg"), ("PNG image","*.png")])
    if not path: return
    load = Image.open(path)
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.place(x=83, y=0)
window = Tk()
window.title("SmallLooker")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
window.mainloop()
