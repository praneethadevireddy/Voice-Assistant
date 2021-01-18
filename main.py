import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.say('Good Morning, this is Alexa! How can I help you today?')
engine.runAndWait()
#with sr.Microphone() as source:
 #   voice = listener.listen(source)
  #  name = listener.recognize_google(voice)
   # name = name4.lower()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('How can I help you?')
            voice = listener.listen(source)
            comand = listener.recognize_google(voice)
            comand = comand.lower()
            if 'alexa' in comand:
                comand=comand.replace('alexa','')
                print(comand)
    except:
        print('What?')
    return comand
def run_alexa():
    command=take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('Okay'+'playing'+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('Okay'+'Current time is'+ time)
    elif 'who is' or 'what is' in command:
        if 'who is' in command:
            person=command.replace('who is','')
            info=wikipedia.summary(person,10)
            print('Okay'+info)
            talk('Okay'+info)
        elif 'what is' in command:
            person=command.replace('what is','')
            info=wikipedia.summary(person,1)
            talk('Okay'+person)
    elif 'tell me about' in command:
        person=command.replace('tell me about','')
        info=wikipedia.summary(person,10)
        talk(person)
run_alexa()
