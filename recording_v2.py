import tkinter as tk
import pyaudio
import wave
import threading

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


# GUI setup
window = tk.Tk()
window.title("Audio Recorder")

recording = False

record_btn = tk.Button(window, text="Hold to Record")
record_btn.grid(row=0, column=0, padx=10, pady=5)  # Using grid instead of pack

# Bind mouse click and release events
record_btn.bind("<ButtonPress-1>", start_recording)
record_btn.bind("<ButtonRelease-1>", stop_recording)

# quit button
quit_button = tk.Button(text='Quit', command=window.quit)
quit_button.grid(row=2, column=0, sticky="ew", padx=10, pady=5)

# Configure the grid rows and columns
window.rowconfigure(0, minsize=200, weight=1)
window.columnconfigure(0, minsize=400, weight=1)

window.mainloop()
