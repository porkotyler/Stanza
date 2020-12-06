#!/usr/bin/python3
import os
import pygame
from Tkinter import *

root = Tk()
root.minsize(600,300)


listofsongs = []
v = StringVar()
songLabel = Label(root,textvariable=v,width=35)

index = 0

def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stop(event):
    pygame.mixer.music.pause()
    v.set("-- Pause --")

def play(event):
    if index > 0:
        pygame.mixer.music.unpause()
        updatelabel()
    else:
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
        updatelabel()

def updatelabel():
    global index
    global songname
    v.set(listofsongs[index])

directory = "C:\Music"
os.chdir(directory)
for files in os.listdir(directory):
	if files.endswith(".mp3"):
		listofsongs.append(files)
		print(files)

	pygame.mixer.init()
	pygame.mixer.music.load(listofsongs[0])
	pygame.mixer.music.play()

label = Label(root,text="Music Player")
label.pack()

listbox = Listbox(root)
listbox.pack()

listofsongs.reverse()

for items in listofsongs:
    listbox.insert(0,items)

listofsongs.reverse()

nextButton = Button(root,text="Next Song")
nextButton.pack()

previousButton = Button(root,text="Previous Song")
previousButton.pack()

stopButton = Button(root,text="Stop")
stopButton.pack()

playbutton = Button(root,text="Play")
playbutton.pack()

playbutton.bind("<Button-1>",play)
nextButton.bind("<Button-1>",nextsong)
previousButton.bind("<Button-1>",prevsong)
stopButton.bind("<Button-1>",stop)

songLabel.pack()

root.mainloop()