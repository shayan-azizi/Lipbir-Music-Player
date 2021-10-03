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


root.mainloop()