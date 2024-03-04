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



# IMPORTS END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!








# TEXT TO SPEECH FUNCTION DEFINITIONS ---------- START  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




def get_text():
    text = txt_edit.get(1.0, END)
    list_of_char = ["\n", "“", "”", "***", "–", "&", "/", "’", "‘", "—", "-", "\—", "\-", "\-", "•", "·", "°", "¶", "\u202f", "\u2212"]

    pattern = '[' + ''.join(list_of_char) + ']'
    # Remove characters matched by pattern
    mod_string = re.sub(pattern, '', text)
    text = mod_string
    create_file(text)

# create_speech() # can be called independently, needs text file!
def create_file(text):  # cant write to file with newlines, newlines completely ignored and don't write to file,
    # STILL converting directly from IDE
    with open("default.txt", "w+") as file:
        # text = input() # testing
        file.write(text)
        file.close()  # redundant?
        create_speech("default.txt")

# gets text, and passes it to create file
def create_speech(text_file):
    i = 1
    file = open(text_file, "r", encoding='utf-8').read().replace("\n", " ").replace("–", "dash")
    # quotes = re.findall(r'" [^"$]* "', file)
    name = "default{}.mp3".format(i)
    speech = gTTS(text=file, lang="en", slow=False)
    speech.save(name)
    # os.startfile("C:/Users/Charles/PycharmProjects/Text-To-Speech-Orig-v2")
    playsound("C:\\Users\\Charles\\PycharmProjects\\Text-To-Speech-Orig-v2\\"+name)
    delete_file(name)


def makeit(txt):
    client = OpenAI()
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=txt
    )
    response.stream_to_file(speech_file_path)
    x = 5  # number of secibds to wait before executing final code block
    print("Audio Playback Beginning in {} Second(s)".format(x))
    time.sleep(x)

def playit():
    pygame.mixer.init()
    pygame.mixer.music.load("speech.mp3")
    pygame.mixer.music.play()
    # Wait for the music to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)  # You can adjust the sleep time to control the loop frequency
    # The program will continue here after the music finishes
    print("Audio playback finished.")


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



# TEXT TO SPEECH FUNCTIONS DEFINITIONS ---------- END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




# SPEECH TO TEXT FUNCTIONS
# SPEECH TO TEXT FUNCTIONS DEFINITIONS ---------- START  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# SPEECH TO TEXT FUNCTIONS DEFINITIONS ---------- END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!







# JARVIS FUNCTIONS DEFINITIONS
# JARVIS FUNCTIONS DEFINITIONS ---------- START  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# JARVIS FUNCTIONS DEFINITIONS ---------- END  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!














def setup_text_to_speech_mode():
    clear_window()
    # Add widgets for Text to Speech mode
    label = tk.Label(window, text="Text to Speech Mode")
    label.grid(row=1, column=0, columnspan=2, sticky="ew")
    # ... Add other widgets specific to Text to Speech mode ...

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

    txt_edit.grid(row=0, column=1, sticky="nsew")
    fr_buttons.grid(row=0, column=0, sticky="ns")


def setup_speech_to_text_mode():
    clear_window()
    # Add widgets for Speech to Text mode
    label = tk.Label(window, text="Speech to Text Mode")
    label.grid(row=1, column=0, columnspan=2, sticky="ew")
    # ... Add other widgets specific to Speech to Text mode ...

def setup_jarvis_mode():
    clear_window()
    # Add widgets for Jarvis mode
    label = tk.Label(window, text="Jarvis Mode")
    label.grid(row=1, column=0, columnspan=2, sticky="ew")
    # ... Add other widgets specific to Jarvis mode ...

def clear_window():
    for widget in window.winfo_children():
        if widget != mode_menu:  # Keep the dropdown menu
            widget.grid_forget()

def switch_mode(*args):
    mode = mode_var.get()
    if mode == 'Text to Speech':
        setup_text_to_speech_mode()
    elif mode == 'Speech to Text':
        setup_speech_to_text_mode()
    elif mode == 'Jarvis Mode':
        setup_jarvis_mode()

window = tk.Tk()
window.title("Multi-Mode App")
# Main window grid configuration
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Dropdown menu for mode selection
modes = ['Text to Speech', 'Speech to Text', 'Jarvis Mode']
mode_var = tk.StringVar(window)
mode_var.set('Select Mode')  # Default value
mode_var.trace('w', switch_mode)
mode_menu = tk.OptionMenu(window, mode_var, *modes)
mode_menu.grid(row=6, column=0, sticky="ew")

# Text edit area and button frame
txt_edit = tk.Text(window)
fr_buttons = tk.Frame(window)


window.mainloop()