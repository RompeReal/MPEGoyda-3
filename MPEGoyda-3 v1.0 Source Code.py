# MPEGoyda-3 by RompeReal (https://github.com/RompeReal https://t.me/FactorialOf8) CC-BY-NC
# Supported audio formats / Поддерживаемые аудио-форматы
# mp3, aac, ogg, flac, alac, aiff, dsd, mqa, m4a

import os
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import pygame

pygame.mixer.init()

musicfiles = []
currentfile_index = -1
is_paused = False

def update_track_label():
    playing.config(text=f"Сейчас играет: {musicfiles[currentfile_index].split('/')[-1]}")

def play(index):
    global currentfile_index, is_paused
    if musicfiles and index < len(musicfiles):
        currentfile_index = index
        pygame.mixer.music.load(musicfiles[currentfile_index])
        pygame.mixer.music.play()
        is_paused = False
        update_track_label()

def stop():
    pygame.mixer.music.stop()

def toggle_playback():
    global is_paused
    if is_paused:
        pygame.mixer.music.unpause()
        is_paused = False
        playpause_button.config(text="       Пауза       ")
    else:
        pygame.mixer.music.pause()
        is_paused = True
        playpause_button.config(text="  Возобновить  ")

def load():
    global musicfiles, currentfile_index
    musicfiles = []
    directory = filedialog.askdirectory()
    if directory:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(('.mp3', '.aac', '.ogg', '.flac', '.alac', '.aiff', '.dsd', '.mqa', '.m4a')):
                    musicfiles.append(os.path.join(root, file))
        if musicfiles:
            play(0)

def next_track():
    global currentfile_index
    if musicfiles:
        currentfile_index = (currentfile_index + 1) % len(musicfiles)
        play(currentfile_index)

def previous_track():
    global currentfile_index
    if musicfiles:
        currentfile_index = (currentfile_index - 1) % len(musicfiles)
        play(currentfile_index)

root = tk.Tk()
root.title("MPEGoyda-3")
root.configure(bg='#202020')

logo = Image.open("\\Downloads\\MPEGoyda-3_logo202020.jpg")
logoimage = ImageTk.PhotoImage(logo)
logolabel = tk.Label(image=logoimage)
logolabel.pack()

loadbutton = tk.Button(root, text="♪Выберите папку♪", command=load)
loadbutton.pack(pady=20)
if currentfile_index:=-1:
	cfi="""(выберите путь с файлами)
Если аудиофайлы находятся не в одной папке
с файлом кода, подождите около 20 секунд.
Надеюсь, я исправлю это :') )"""
else:
	cfi=currentfile_index
playing = tk.Label(root, text=f"Сейчас играет: {cfi}", fg='#FFFFFF', bg='#202020')
playing.pack()
previousbutton = tk.Button(root, text=" Предыдущий ", command=previous_track)
previousbutton.pack(pady=20)
playpause_button = tk.Button(root, text="       Пауза       ", command=toggle_playback)
playpause_button.pack(pady=20)
nextbutton = tk.Button(root, text="  Следующий  ", command=next_track)
nextbutton.pack(pady=20)
stopbutton = tk.Button(root, text="        Стоп         ", command=stop)
stopbutton.pack(pady=20)
musicfiles = []
root.mainloop()
