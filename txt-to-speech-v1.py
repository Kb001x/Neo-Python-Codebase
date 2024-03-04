from pathlib import Path
from openai import OpenAI
import pygame.mixer
import time


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


x = """
    I’ve been noticing this agenda lately with Netflix. For now, I’ll refer to it all as transhumanism. It’s the idea that we as humans will one day transcend all limitations and become ‘more’ than just human through technology.
    If you really think about it makes sense right? God made us in his image (according to the Christian god) and gave us carte blanche over this realm and all its creatures. Meaning we get to eat kill animals to eat there meat, build things, spread out and inhabit the earth. It says so in the books of Genesis, Leviticus, and Romans. So, all of gods other creatures serve us, right? It seems logical to infer that similarly to how our children grow into adults, our species are the children of god, will grow into adult gods?
    I experimented with this idea a lot in high school. The idea that religious beliefs hinder progress. As though progress where the only indication of our value as a species. But that was my teenage brain at the time. I’d like to formally apologize to all those whom I’ve hurt while living in that state of hyper intellectual elitism.  
    It’s an easy trap to fall into. After all, Slavery was legal at one point. The Holocaust was legal in Germany at the time and colonialism was not only legal but just at the time. Legality is a matter of Power, not justice. I failed to make the distinction between Legality and morality and how they influence notions of justice. Without a strict moral code and the discipline to follow it. Legality becomes fluid, enabling the notion of justice to change with the times. 
    But I digress I originally started writing this peace because the scene where one astronaut has his house broken into by a gang of Zealous anti-robot miscreants and I was so upset because A) it really felt like Netflix has some sort of transhumanist agenda because the guy got his family killed because he was a robot at the time. I felt like they were setting up the premise that technological advancement = good, dogma = bad. But the writers did a good job of subverting my expectations. I guess I’m really sick and tired of this transhumanist BS and got ultra triggered, far too quickly! B) the episode was riddled with plot holes, if the plot had a profile pic it would be an agoraphobes worst nightmare. C) Well, there is no C I just wanted to have multiple grievances but was a bit more satisfied with the plot when it ended than when it was only half done so…
    Bye Bye, Thanks for watching. Peace!
    """

makeit(x)
playit()
