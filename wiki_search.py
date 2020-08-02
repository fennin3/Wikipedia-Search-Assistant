

# importing libraries
import speech_recognition as sr
import pyttsx3
import wikipedia
import time


i = 0
# Functions of the program

def talkback(y):
    
    talk = pyttsx3.init()
    rate = talk.getProperty('rate')
    talk.setProperty('rate', rate-10)
    voices = talk.getProperty('voices')
    talk.setProperty('voice', voices[i].id)
    talk.say(y)
    talk.runAndWait()

def speech_to_text():
    r = sr.Recognizer()
    mic = sr.Microphone()
    user_input=""
        
    with mic as source:
        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold= True
        audio = r.listen(source)

    try:
            #converting request from user to text
        user_input = r.recognize_google(audio)
        return user_input
            
    except sr.UnknownValueError:
        talkback("Sorry i don't get you, can you come again")          
            
    except sr.RequestError:
            # Connection/ request error handling
        print("Sorry it seems you are offline.")


def wiki(x):
    #tokenized = word_tokenize(x)
    talkback("A second boss")
    tokenized = x.split()  
    try:

        x =wikipedia.summary(tokenized, sentences=2)
        print(x)
        talkback(x)
    except ConnectionError:
        talkback("Sorry I'm having a problem connecting")
    except Exception as e:
        print(e)


print("")
print("[...] Starting Program...")
time.sleep(1)
print("[...] System Booted...")
time.sleep(1)
print("")
print("Speak now..")

while True:

    user_input = speech_to_text()
    
    if str(user_input).lower() == "quit":
        break
    else:
        if user_input is not None:
            wiki(user_input)
    
        user_input= ""