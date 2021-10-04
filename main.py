from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title("Lipbir - Music Player")
root.iconbitmap("Images/icon.ico")
root.geometry("500x300")
root.resizable(False, False) 

# Add image file
root.config(bg='yellow')

img = PhotoImage(file="Images/bg1.png")
label = Label(
    root,
    image=img
)
label.place(x=0, y=0)



# Init pygame mixer
pygame.mixer.init()

# Add song functions
def add_song (e):
    song = filedialog.askopenfilename(initialdir = "Musics/", title = "Choose A Song", filetypes = (("mp3 Files", "*.mp3"), ("All Files", "*.*")))
    
    song = song.replace("C:/Users/huawei/Documents/GitHub/Lipbir-Music-Player/Musics/", "")
    song = song.replace(".mp3", "")
    
    # Add song to songbox
    song_box.insert(END, song)
    
# Define Play functions
def play (e):
    song = song_box.get(ACTIVE)
    song = f'C:/Users/huawei/Documents/GitHub/Lipbir-Music-Player/Musics/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops= 0)
    
# Define Stop functions
def stop (e):
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)


# Define Paise functions
global paused
paused = False

def pause (e, is_paused):
    global paused
    paused = is_paused
    if paused == True:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True

# Create Playlist
song_box = Listbox(root, bg = "lightblue", fg = "black", width = 60, selectbackground = "gray", selectforeground = "white")
song_box.pack(pady = 20)

# Define player control buttons images
back_btn_img = PhotoImage(file = "Images/back.png")
forward_btn_img = PhotoImage(file = "Images/forward.png")
play_btn_img = PhotoImage(file = "Images/play.png")
pause_btn_img = PhotoImage(file = "Images/pause.png")
stop_btn_img = PhotoImage(file = "Images/stop.png")

# Creatr player control frame
controls_frame = Frame()
controls_frame.pack()


# Create player control buttons
back_button = Button(controls_frame, image =back_btn_img, borderwidth = 0)
forward_button = Button(controls_frame, image =forward_btn_img, borderwidth = 0)
play_button = Button(controls_frame, image =play_btn_img, borderwidth = 0, command =lambda: play(False))
pause_button = Button(controls_frame, image =pause_btn_img, borderwidth = 0, command = lambda: pause(False, paused))
stop_button = Button(controls_frame, image =stop_btn_img, borderwidth = 0, command =lambda: stop(False))

back_button.grid(row = 0, column =1, padx = 7)
forward_button.grid(row = 0, column =3, padx = 7)
play_button.grid(row = 0, column =2, padx = 7) 
pause_button.grid(row = 0, column =0, padx = 7)
stop_button.grid(row = 0, column =5, padx = 7)

# Create Menu
my_menu = Menu(root)
root.config(menu = my_menu)

# Add add Songs menu
add_song_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label = "Add Musics", menu = add_song_menu)
add_song_menu.add_command(label = "Add One Music To Playlist", command = lambda: add_song(False))

# Bindings
root.bind("<Return>", play)
root.bind("<Control-o>", add_song)

root.mainloop()