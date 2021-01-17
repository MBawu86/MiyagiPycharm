import speech_recognition as sr
from gtts import gTTS
import wikipedia
import os
import datetime
import warnings
import calendar
import random

#ignore warning messages
warnings.filterwarnings('ignore')

#mic audio to str
def micAudio():
    mic = sr.Microphone(device_index = 3)
    #recognizer object / record audio
    r = sr.Recognizer()

    #open mic and record
    with sr.Microphone() as source:
        print('What knowledge do you require, kodomo?')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    #speech recognition
    data = " "
    #try block
    try:
        data = r.recognize_google(audio)
        print ('You said: '+data )
        print(r.recognize_google(audio))
    #handle errors
    except sr.UnknownValueError:
        print('Speak clearly, Kodomo')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error '+e)

    return data

    #va str > audio
def miyagi(text):
    print('text')
    #convert str > audio
    talkMiyagi = gTTS(text = text, lang = 'en', slow = True)

    #save converted audio to file
    talkMiyagi.save('miyagi_talks.mp3')
    #play file
    os.system('open miyagi_talks.mp3')


text = 'This is a test'
miyagi(text)
micAudio()







