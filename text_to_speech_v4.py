import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkinter import filedialog, messagebox
from tkinter import *
from gtts import gTTS
from playsound import playsound
import re
import os
from pathlib import Path
import pygame.mixer
import time
from openai import OpenAI
import tkinter as tk
import pyaudio
import wave
import threading

# ... (Other imports)

# ----------------- Utility Function Definitions Start ----------------- #


client = OpenAI()


def speech_to_text(filename):
    audio_file = open(filename, "rb")
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        response_format="text"
    )
    print(transcript)


# Audio recording parameters
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100


# Function to handle audio recording
def record_audio():
    global recording
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Start Recording")

    frames = []

    while recording:
        data = stream.read(CHUNK)
        frames.append(data)

    print("Stop Recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open("output.wav", 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))


# Start recording
def start_recording(event):
    global recording
    recording = True
    threading.Thread(target=record_audio).start()


# Stop recording
def stop_recording(event):
    global recording
    recording = False
    get_transcripts()
    update_transcripts()


def get_transcripts():
    return speech_to_text("output.wav")


def update_transcripts():
    transcript = get_transcripts()
    if transcript is None:
        transcript = "No transcript available."
    transcript_box.insert(tk.END, transcript + '\n')




# Speech to text functions start!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




def get_text():
    text = txt_edit.get(1.0, END)
    list_of_char = ["\n", "“", "”", "***", "–", "&", "/", "’", "‘", "—", "-", "\—", "\-", "\-", "•", "·", "°", "¶",
                    "\u202f", "\u2212"]

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
    playsound("C:\\Users\\Karl\\PycharmProjects\\jarvis\\" + name)
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


# ... (Other utility functions like create_file, create_speech, etc.)

# ----------------- Utility Function Definitions End ------------------- #

# ----------------- Mode Setup Functions Start ----------------- #

def setup_text_to_speech_mode():
    # Set up the GUI for Text to Speech mode
    clear_window()
    window.title("Text-to-Speech Mode")
    # ... (Add specific widgets for this mode)

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
    # text area and frame for buttons
    txt_edit.grid(row=0, column=1, sticky="nsew")
    fr_buttons.grid(row=0, column=0, sticky="ns")


def setup_speech_to_text_mode():
    # Set up the GUI for Speech to Text mode
    clear_window()
    window.title("Speech to Text Mode")
    # ... (Add specific widgets for this mode)
    window.title("Audio Recorder")

    recording = False

    record_btn = tk.Button(window, text="Hold to Record")
    record_btn.grid(row=0, column=0, padx=10, pady=5)  # Using grid instead of pack

    # Bind mouse click and release events
    record_btn.bind("<ButtonPress-1>", start_recording)
    record_btn.bind("<ButtonRelease-1>", stop_recording)

    # Text box for displaying transcripts
    transcript_box = tk.Text(window, height=10, width=50)
    transcript_box.grid(row=1, column=0, padx=10, pady=10)

    # Button to update transcripts (for demonstration)
    update_btn = tk.Button(window, text="Update Transcripts", command=update_transcripts)
    update_btn.grid(row=2, column=0, padx=10, pady=10)

    # quit button
    quit_button = tk.Button(text='Quit', command=window.quit)
    quit_button.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

    # Configure the grid rows and columns
    window.rowconfigure(0, minsize=200, weight=1)
    window.columnconfigure(0, minsize=400, weight=1)


def setup_jarvis_mode():
    # Set up the GUI for Jarvis mode
    clear_window()
    window.title("Jarvis Mode")
    # ... (Add specific widgets for this mode)


def clear_window():
    # Clear the window of widgets except for the mode menu
    for widget in window.winfo_children():
        if widget != mode_menu:
            widget.grid_forget()


# ----------------- Mode Setup Functions End ------------------- #

# ----------------- GUI Layout and Initialization Start ----------------- #
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

# Configure main window grid
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Dropdown menu for mode selection
modes = ['Text to Speech', 'Speech to Text', 'Jarvis Mode']
mode_var = tk.StringVar(window)
mode_var.set('Select Mode')  # Default value
mode_var.trace('w', switch_mode)
mode_menu = tk.OptionMenu(window, mode_var, *modes)
mode_menu.grid(row=1, column=0, columnspan=2, sticky="ew")

# Text editor area definitions
txt_edit = tk.Text(window)

# Frame for buttons
fr_buttons = tk.Frame(window)

# ----------------- GUI Layout and Initialization End ------------------- #

window.mainloop()
