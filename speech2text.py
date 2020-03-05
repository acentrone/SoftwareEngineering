#The base code to process the speech recognition part of the project
#was found in the following youtube video
#https://www.youtube.com/watch?v=K_WbsFrPUCk&list=LLGwLLP-jq-Dm-1I1sNzSG3g&index=2&t=0s

#additional changes and options have been added on top of what was found
#in the youtube video however.

import speech_recognition as sr

def speech2text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #listens for half a second to ambient noise to adjust
        #microphone levels so that we don't pick any of that up
        r.adjust_for_ambient_noise(source, duration = 0.25)
        #how long there is silence before it registers that you're
        #done talking
        r.pause_threshold = 0.5
        #start recording audio. If microphone doesn't pick up
        #anything above the ambient noise for 1.5 seconds then it
        #will throw an exception
        audio = r.listen(source, timeout = 1.5)
        try:
            dict = r.recognize_google(audio, show_all = True)
            #see commit comment from Keifer on 3-5-2020 to see
            #the format that dict is in due to the show_all
            #option being true
            text = dict['alternative'][0]
        except:
            text = "ERROR"

    return text