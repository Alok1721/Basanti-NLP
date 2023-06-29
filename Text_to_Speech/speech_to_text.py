#speech to text
import speech_recognition as s
ss=s.Recognizer()
print("i am listing you...................")
with s.Microphone() as m:
    audio=ss.listen(m)
    query=ss.recognize_google(audio,language='eng-in')
    print(query)
print("session ended")
    
