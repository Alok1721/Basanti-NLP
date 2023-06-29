import speech_recognition as sr
from gtts import gTTS
import playsound

# Speech to Text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I'm listening...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="en-US")
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
    except sr.RequestError as e:
        print("Sorry, there was an issue with the speech recognition service. {0}".format(e))

# Text to Speech
def speak(text):
    tts = gTTS(text=text, lang="en")
    tts.save("output.mp3")
    playsound.playsound("output.mp3")

# Main program
query = listen()
speak(query)

print("Session ended.")
