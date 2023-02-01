import nltk
import datetime
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import pyttsx3
from urllib.request import urlopen
import pywhatkit
import requests #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import urllib3
import wikipedia #pip install wikipedia
import webbrowser
import json
import os
import smtplib
import pywhatkit
import pyjokes
import pyaudio
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('referone700@gmail.com', 'SGZNBWJN')
    server.sendmail('referone700@gmail.com', to, content)
    server.close()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am spyder Sir. Please tell me how may I help you")



engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


recognizer = sr.Recognizer()
speak("Hello, Iam Spider an chatbot here to help you with your emotions.")
speak("So how was your day today??")

sum = 0
while sum == 0:      
    with sr.Microphone() as source:
        print("clearing background noise ....")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print('Waiting for your message....')
        recordedaudio = recognizer.listen(source)
        recordedaudio.pause_threshold = 1
        print("done recording...")
        try:
            print('Printing the message...')
            text = recognizer.recognize_google(recordedaudio, language='en-US')
            print("your message :{}".format(text))

        except Exception as ex:
            text = "OPPs"
            sum = 1
            speak("Didn't Catch that")
        if  recordedaudio == 'end':
            sum = 1
        break
 

paragraph = text

sent = nltk.sent_tokenize(paragraph)

word = nltk.word_tokenize(paragraph)
lematizer = WordNetLemmatizer()

stemmer = PorterStemmer()

# data cleaning
corpus = []
for i in range(len(sent)):
    review = re.sub('[^a-zA-Z]', ' ', sent[i])
    review = review.lower()
    review = review.split()
    review = [lematizer.lemmatize(word) for word in review if word not in set(stopwords.words('english'))]
    sent[i] = ' '.join(review)
    corpus.append(review)



sentence = [str(corpus)]
analyser = SentimentIntensityAnalyzer()
for i in sentence:
    v = analyser.polarity_scores(i)
    new_value = max(v, key=v.get)
    print(new_value)
    print(v)
if new_value == 'neg':
    speak('You seem to be sad today')
    speak(pyjokes.get_joke())
else: 
    speak(pyjokes.get_joke())
