import tkinter as tk
import webbrowser

def open_graven_channel():
    webbrowser.open_new("http://youtube.com/gravenilvectuto")

# here we personalize the caracteristics of the window
window = tk.Tk() #create a window with Tk()
window.title("Brunel")  #to put a title on the window
window.geometry("720x480")  #to set the dimensions of the window
window.minsize(480,360) # to set the minimal dimensions of the window(minsize(x,y))
#window.iconbitmap()
window.config(background = 'black')

frame = tk.Frame(window, bg = '#41B77F',bd= 1, relief='sunken')
#frame = tk.Frame(window, bg = '#41B77F')


# add text
label_title = tk.Label(frame, text = 'Welcome to the Interface', font = ('Times New Roman', 30), bg= 'black', fg= 'white' )
#label_title.pack(side= 'left')#the text will be at the left side of the window
label_title.pack()#the text will be at the center of the window
#label_title.pack()

#add a second text
label_subtitle = tk.Label(frame, text = 'Hello everyone', font = ('Times New Roman', 25), bg= '#41B77F', fg= 'white' )
label_subtitle.pack()

# add button
yt_button = tk.Button(frame, text = "Open YOUTUBE", font= ('Times New Roman',25), bg= 'white', fg='#41B77F', command= open_graven_channel)
yt_button.pack(pady= 25, fill='x')


frame.pack(expand='YES')


window.mainloop() #run the window