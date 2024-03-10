import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkinter import filedialog, messagebox
from tkinter import *
from gtts import gTTS
from playsound import playsound
import re
import os
from pathlib import Path
from openai import OpenAI
import pygame.mixer
import time


def get_text():
    text = txt_edit.get(1.0, END)
    list_of_char = ["\n", "“", "”", "***", "–", "&", "/", "’", "‘", "—", "-", "\—", "\-", "\-", "•", "·", "°", "¶",
                    "\u202f", "\u2212"]

    pattern = '[' + ''.join(list_of_char) + ']'
    # Remove characters matched by pattern
    mod_string = re.sub(pattern, '', text)
    text = mod_string
    makeit(text)




def makeit(txt):
    x = 1  # number of seconds to wait before executing final code block
    print("Audio Playback Beginning in {} Second(s)".format(x))
    client = OpenAI()
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=txt
    )
    response.stream_to_file(speech_file_path)

    # Estimate the duration of the sound file
    file_size_in_bytes = os.path.getsize("speech.mp3")
    # This is an assumption; you'll need to adjust this based on your actual audio files
    bitrate_in_kbps = 160  # Typical bitrate for MP3 files, adjust as necessary
    duration_in_seconds = file_size_in_bytes / (bitrate_in_kbps * 128)
    print("Playback Initiated")
    print("Audio Playback Ending in {} Second(s)".format(duration_in_seconds))
    #time.sleep(x)
    pygame.mixer.init()
    pygame.mixer.music.unload()
    pygame.mixer.music.load("speech.mp3")
    pygame.mixer.music.play()
    time.sleep(duration_in_seconds+2) # sleep timer, otherwise audio ends abruptly
    pygame.mixer.music.unload()

    print("playback completed")


# create_file() # will auto call create speech!
def clear():
    txt_edit.delete(1.0, END)


def paste():
    print("it worked!")
    txt_edit.insert(1.0, window.clipboard_get())


def delete_file(filename):
    os.remove(filename)


def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text to Speech v2.5a- {filepath}")


def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")


# clear powers the clear button

# GUI DEFINITIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
window = tk.Tk()
window.title("Text-to-Speech App v3.00 uses Open AI TTS")
# set the row and column configurations.
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
# four widgets, text box, the frame, and the open and save buttons.


txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)

# define buttons and frames!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)
clear_button = Button(fr_buttons, text="Clear All Text", command=clear)
get_text_button = Button(fr_buttons, text="Read it to me!", command=get_text)
quit_button = Button(fr_buttons, text='Quit', command=window.quit)
paste_button = Button(fr_buttons, text="Paste", command=paste)

# ship it to screen!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
paste_button.grid(row=0, column=0, sticky="ew", padx=10, pady=5)
get_text_button.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
clear_button.grid(row=2, column=0, sticky="ew", padx=10, pady=10)
btn_open.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
btn_save.grid(row=4, column=0, sticky="ew", padx=10, pady=5)
quit_button.grid(row=5, column=0, sticky="ew", padx=10, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# SPIN IT UP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
window.mainloop()
