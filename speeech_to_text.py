from openai import OpenAI
import tkinter as tk
import pyaudio
import wave
import threading

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

# GUI setup
window = tk.Tk()
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

window.mainloop()
