from gtts import gTTS
import os
# ceazione di un assistente vocale 
import speech_recognition as sr 
from gtts import gTTS
import os

# inizialiizazione del riconoscimento vocale
recognizer= sr.Recognizer()

# Acquisizione audio nel microfono
with sr.Microphone() as source:
    print("Di qualcosa...")
    audio= recognizer.listen(source)
try:
    # Trascrizione del parlato in tetso
    testo= recognizer.recognize_google(audio,language= "it-IT")
    print(f"Hai detto:{testo}")
    
    # rispotsa vocale generata
    risposta= f"Hai detto:{testo}"
    tts= gTTS(text= risposta,lang= "it")
    tts.save("risposta.mp3")
    os.system("start risposta.mp3")
except:
    print("Non ho capito")
