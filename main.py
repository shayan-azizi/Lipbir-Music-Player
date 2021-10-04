from tkinter import *
import pygame

root = Tk()
root.title("Lipbir - Music Player")
root.geometry("500x300")

# Init pygame mixer
pygame.mixer.init()

# Create Playlist
song_box = Listbox(root, bg = "lightblue", fg = "black", width = 60)
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
play_button = Button(controls_frame, image =play_btn_img, borderwidth = 0)
pause_button = Button(controls_frame, image =pause_btn_img, borderwidth = 0)
stop_button = Button(controls_frame, image =stop_btn_img, borderwidth = 0)

back_button.grid()
forward_button.grid()
play_button.grid() 
pause_button.grid()
stop_button.grid()

root.mainloop()