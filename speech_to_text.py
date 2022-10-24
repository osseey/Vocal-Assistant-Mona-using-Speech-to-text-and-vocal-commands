import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
print(voices[0].id)
engine.setProperty('rate',50)
engine.say("Hello, How are you ?")
engine.runAndWait()

def speak(str):
    print("je suis arrivé ici")
    engine.say(str)
    print("je suis arrivé ici")
    engine.runAndWait()

speak("Hello, What's going on")