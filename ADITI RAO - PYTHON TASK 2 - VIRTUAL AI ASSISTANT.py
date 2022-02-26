#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Aditi Rao - 8850646668 - Python task 2 

# AI Voice Based Virtual Assistant

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
from datetime import date

engine=pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices [1].id)
recognizer=sr.Recognizer()

def engine_talk(text):
    engine.say(text)
    engine.runAndWait()
    
def run_virtualassist():
    
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,duration=1)
        print('\n')
        print("Now you may speak")
        engine_talk('Now you may speak ')
        recordedaudio=recognizer.listen(source)
    
    try:
        command=recognizer.recognize_google(recordedaudio,language='en-us')
        command = command.lower()
        if 'virtual assistant' in command :
                command = command.replace('virtual assistant', '')
                print('you said'+command)
        else:
            print('you said : '+command)
   
        if 'hello' in command :
            print('hello how may i assist you ??')
            engine_talk('hello, how may i assist you ??')
           
        elif 'who are you' in command :
                print('I am your virtual AI voice assistant ')
                engine_talk('I am your virtual AI voice assistant . how may i assist you ?')
            
        elif 'can you do' in command :
                print('''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map, open different websites like 
                    instagram, youtube,gmail, git hub, stack overflow and searches on google.How may i help you ?''')
                engine_talk('''i can play songs on youtube , tell you a joke, search on wikipedia, tell date and time,find your location, locate area on map,
                    open different websites like insta gram, youtube,gmail,  and searches on google. How may i help you ?''')
                    
        elif 'play' in command:
                song = command.replace('play', '')
                print('Playing' +song)
                engine_talk('Playing' +song)
                pywhatkit.playonyt(song)
            
        elif 'date and time' in command :
                today = date.today()
                time = datetime.datetime.now().strftime('%I:%M %p')
                
                d2 = today.strftime("%B %d, %Y")
                print("Today's Date is ", d2, ' time right now  is', time)
                engine_talk('Today is : '+ d2)
                engine_talk('and time right now is '+ time)   

        elif 'time and date' in command :
                    today = date.today()
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    # Textual month, day and year
                    d2 = today.strftime("%B %d, %Y")
                    print("Today's Date is ", d2, 'Time right now is', time)
                    engine_talk( 'Time right now is '+ time)
                    engine_talk('and Today is : '+ d2)


        elif 'time' in command:
                        time = datetime.datetime.now().strftime('%I:%M %p')
                        print('The time right now is' +time)
                        engine_talk('The time right now is ')
                        engine_talk(time)
                        
        elif 'date' in command:
                        today = date.today()
                        print("Today's date:", today)
                        # Textual month, day and year
                        d2 = today.strftime("%B %d, %Y")
                        print("Today's Date is ", d2)
                        engine_talk('Todays date is')
                        engine_talk(d2)
                        
                        
        elif 'give me information regarding' in command:
                        name = command.replace('give me information regarding' , '')
                        info = wikipedia.summary(name, 1)
                        print(info)
                        engine_talk(info)
                    
        elif 'wikipedia' in command:
                        name = command.replace('wikipedia' , '')
                        info = wikipedia.summary(name, 1)
                        print(info)
                        engine_talk(info)
                    
        elif 'what is' in command:
                        name = command.replace('what is ' , '')
                        info = wikipedia.summary(name, 1)
                        print(info)
                        engine_talk(info)
                    
        elif 'who is ' in command:
                        name = command.replace('who is' , '')
                        info = wikipedia.summary(name, 1)
                        print(info)
                        engine_talk(info)
                    
        elif 'what is ' in command :
                        search = 'https://www.google.com/search?q='+command
                        print(' This is what i found on the internet..')
                        engine_talk('searching..This is what i found on the internet..')
                        webbrowser.open(search)
                        
        elif 'joke' in command:
                        _joke = pyjokes.get_joke()
                        print(_joke)
                        engine_talk(_joke)
                    
        elif 'search' in command :
                        search = 'https://www.google.com/search?q='+command
                        engine_talk('searching... ')
                        webbrowser.open(search)

        elif "my location" in command:
                            url = "https://www.google.com/maps/search/Where+am+I+?/"
                            webbrowser.get().open(url)
                            engine_talk("You are located here, as per Google maps")

        elif 'locate ' in command :
                                engine_talk('finding ...')
                                loc = command.replace('locate', '')
                                if 'on map' in loc :
                                    loc= loc.replace('on map',' ')
                                    url = 'https://google.nl/maps/place/'+loc+'/&amp;'
                                    webbrowser.get().open(url)
                                    print('This is the location of '+loc)
                                    engine_talk('This is the location of '+loc)

        elif 'location of' in command :
                                    engine_talk('finding ...')
                                    loc = command.replace('find location of', '')
                                    url = 'https://google.nl/maps/place/'+loc+'/&amp;'
                                    webbrowser.get().open(url)
                                    print('This is the location of '+loc)
                                    engine_talk('This is the location of '+loc)

        elif 'where is ' in command :
                                        engine_talk('finding ...')
                                        loc = command.replace('where is', '')
                                        url = 'https://google.nl/maps/place/'+loc+'/&amp;'
                                        webbrowser.get().open(url)
                                        print('This is the location of '+loc)
                                        engine_talk('This is the location of '+loc)

        elif 'facebook' in command :
                                            search = 'https://www.facebook.com/'
                                            engine_talk('opening facebook')
                                            webbrowser.open(search)

        elif 'open twitter' in command :
                                                search = 'https://twitter.com/i/flow/login'
                                                engine_talk('opening twitter')
                                                webbrowser.open(search)

        elif 'open netflix' in command :
                            search = 'https://www.netflix.com/in/'
                            engine_talk('opening netflix')
                            webbrowser.open(search)
                            
        elif 'open google meet' in command :
                        search = 'https://meet.google.com/'
                        engine_talk('opening google meet')
                        webbrowser.open(search)

        elif 'open google' in command :
                        print('opening google ...')
                        engine_talk('opening google..')
                        webbrowser.open_new('https://www.google.co.in/')
                        
                        
        elif 'gmail' in command :
                        print('opening gmail ...')
                        engine_talk('opening gmail..')
                        webbrowser.open_new('https://mail.google.com/')
                    
        elif 'open youtube' in command :
                        print('opening you tube ...')
                        engine_talk('opening you tube..')
                        webbrowser.open_new('https://www.youtube.com/')
                    
        elif 'open instagram' in command :
                        print('opening instagram ...')
                        engine_talk('opening insta gram...')
                        webbrowser.open_new('https://www.instagram.com/')
                                       
        elif 'bye' in command:
                        print('good bye, have a nice day !!')
                        engine_talk('good bye, have a nice day !!')
                        sys.exit()

        elif 'thank you' in command :
            print("your welcome")
            engine_talk('your welcome')
                    
        elif 'stop' in command:
                        print('good bye, have a nice day !!')
                        engine_talk('good bye, have a nice day !!')
                        sys.exit()
                        
        else:
                        print(' Here is what i found on the internet..')
                        engine_talk('Here is what i found on the internet..')
                        search = 'https://www.google.com/search?q='+command
                        webbrowser.open(search)
            
    except Exception as ex:
        print(ex)
                
print('Getting rid of background noise... Please be patient.')
engine_talk('Getting rid of background noise... Please be patient.')
print('\n')
print("Hello, I am your virtual AI assistant. how may i assist you ?")
engine_talk ("Hello I am your virtual AI assistant how may i assist you ?")
while True:
    run_virtualassist()


# In[ ]:




