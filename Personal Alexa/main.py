import speech_recognition as sr #ok
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

recognizer = sr.Recognizer()
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

def speak(go):
    speaker.say(go)
    speaker.runAndWait()

def command():
    text = ""
    try:
        with sr.Microphone() as source:
            print("Adjusting for ambient noise, please wait...")
            recognizer.adjust_for_ambient_noise(source)
            speak("Listening ...")
            print("Listening...")
            audio = recognizer.listen(source)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            text = text.lower()
            if 'alexa' in text:
                text = text.replace('alexa', '')

    except:
        pass
    return text

def evoke_alexa():
    text = command()  
    print("You said :" + text) 

    if "play" in text:
        song = text.replace("play", '')
        speak("playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
        print("Alexa Replied : Current time is " + time)

    elif 'who is' in text:
        person = text.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print("Alexa's reply : " + info)
        speak(info)

    elif 'joke' in text:
        speak(pyjokes.get_joke())

    else:
        speak('Please say the command again.')

while True:
    evoke_alexa()