from tkinter import *
window = Tk()
window.title("Password generator")
window.geometry("480x360")
window.config(background="black")

canvas = Canvas(window, width= 300, height= 300)
canvas.pack(expand='yes')

label_title = Label(canvas,text= "Password", font=("Helvetica",20), fg= "blue")
label_title.pack()


window.mainloop()