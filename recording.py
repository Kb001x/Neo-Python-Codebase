import wave
import sys
import pyaudio


# seconds = Recording Time
# filename = name of the output audio file
def recording(seconds, filename):
    # Set constants for the audio properties
    CHUNK = 1024  # Number of audio frames per buffer
    FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
    CHANNELS = 1 if sys.platform == 'darwin' else 2  # Mono for macOS, Stereo for other OS
    RATE = 44100  # Sample rate (samples per second)
    RECORD_SECONDS = seconds  # Duration of recording

    # Open a .wav file in write mode ('wb' stands for write binary)
    with wave.open(filename, 'wb') as wf:
        p = pyaudio.PyAudio()  # Create an instance of PyAudio

        # Set the parameters for the .wav file
        wf.setnchannels(CHANNELS)  # Number of channels
        wf.setsampwidth(p.get_sample_size(FORMAT))  # Width of samples
        wf.setframerate(RATE)  # Frame rate

        # Open an audio stream for recording
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True)

        print('Recording...')
        # Record audio in chunks for the specified duration
        for _ in range(0, RATE // CHUNK * RECORD_SECONDS):
            wf.writeframes(stream.read(CHUNK))  # Read data from the stream and write to the file
        print('Done')

        # Close the stream and terminate PyAudio
        stream.close()
        p.terminate()

recording(10, 'hello.wav')
