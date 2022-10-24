import speech_recognition as sr
import urllib3
import urllib3.request
import pyttsx3
import pyaudio

vocal= pyttsx3.init()
# on récupère les voix disponibles
voices = vocal.getProperty('voices')
#on sélectionne la voix féminine
vocal.setProperty('voice', voices[1].id)
print("Les voix disponibles sont:\n")
print(voices[0].id,"\n")
print(voices[1].id,"\n")
vocal.setProperty('rate',200)


for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


pyaudio.PyAudio()#.open()

ready = True
#verification de la connextion
def is_internet():
    try:
        url='https://www.google.com'
        http = urllib3.PoolManager()
        response = http.request('GET', url)
        return True
    except urllib3.error.URLError:
        return False

def speech():
    global ready
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        #r.adjust_for_ambient_noise(source)

        print("....")
        audio = r.listen(source)
        print("Reconaissance en cours .... ")
        vocal.say("Reconaissance en cours")
        vocal.runAndWait()
        if is_internet():
            # reconnaissance avec google
            try:
                if r.recognize_google(audio, language='fr-FR') == 'au revoir' or r.recognize_google(audio, language='fr-FR') == 'Au revoir':
                    vocal.say("Au revoir Jojo")
                    vocal.stop()
                    ready = False
                else:
                    print("Vous avez dit : " + r.recognize_google(audio, language='fr-FR'))
                    vocal.say("Vous avez dit : " + r.recognize_google(audio, language='fr-FR'))
                    vocal.runAndWait()
            except sr.UnknownValueError:
                print("Je n'ai pas compris")
                vocal.say("Je n'ai pas compris")
                vocal.runAndWait()
            else:
                pass
                # enregistrement de l'audio
                with open("rec.wav", "wb") as f:
                    f.write(audio.get_wav_data())
                print("Enregistrement de l'audio réussi \n")
                #vocal.say("Enregistrement de l'audio réussi")
                vocal.runAndWait()

if __name__ == "__main__":
    print("Je suis Mona, le modèle de reconnaissance vocale qui vous est présenté aujourd'hui.Dîtes quelque chose s'il-vous-plait")
    vocal.say("Je suis Mona, le modèle de reconnaissance vocale qui vous est présenté aujourd'hui")
    vocal.say("Dîtes quelque chose s'il-vous-plait :")
    vocal.runAndWait()
    while ready:
        speech()