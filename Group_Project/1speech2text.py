#This code to process the speech recognition part of the project
#was found in the following youtube video
#https://www.youtube.com/watch?v=K_WbsFrPUCk&list=LLGwLLP-jq-Dm-1I1sNzSG3g&index=2&t=0s

import speech_recognition as sr

def speech2text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            text = "ERROR"
    return text
