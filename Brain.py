import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

#Create Engine to speakChoose voice using pyttsx3
engine = pyttsx3.init('sapi5') # use inbuild Voices 
voices = engine.getProperty('voices')
#print(voices) 
engine.setProperty('voice',voices[0].id) 
def speak(audio):
    engine.say(audio)
    engine.runAndWait() #

#pre-voice
def wishMe():
    hour = int(datetime.datetime.now().hour) # Zero se 24 hour tak mil jayega
    if hour >= 0 and hour <12:
        speak("Good Morning sir")
        speak("I am your personal assistant, How may I help you?")

    elif hour >=12 and hour <18:
        speak("Good Afternoon Sir")

    else: speak("Good Evening sir")

#Listening
def takeCmd():
    '''1) install SpeechRecognation
       2) it take microphone input from user and return sring output '''
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source) #Listen user audio
#Try Except
    try:
        print("...Recognizing...")
        query =r.recognize_google(audio , language='en-in' ) # Using google to recognize audio
        print(f"User Said: {query}\n")

    except Exception as e:
        speak("Say that again please....")
        return "None" #Koi problem ajay to
    return query  #return speach in sting from


if __name__ == "__main__":
    speak("Hello Sir, How are you?")
    wishMe()
    
    while True:
        query = takeCmd().lower()

        #LOGIC TO EXECUTE THE TASK BASED ON QUERY
        if 'wikipedia' in query:
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia ")
            speak(results)
        
        elif 'open youtube' in query:
            #Open Youtube using webbrowser module
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            #Open Youtube using webbrowser module
            webbrowser.open("google.com")

        elif 'open linkedin' in query:
            #Open Youtube using webbrowser module
            webbrowser.open("linkedin.com")

        elif 'open email' in query:
            #Open Youtube using webbrowser module
            webbrowser.open("mail.google.com")

        #____________Spotify______________
        elif 'spotify' in query:
            speak("Sure, I'll open Spotify for you.")
            webbrowser.open("https://open.spotify.com")

        elif 'play song' in query:
            speak("Sure, please tell me the name of the song you'd like to play on Spotify.")
            song_query = takeCmd().lower()  # Listen for the song name
            if song_query != 'none':
                speak(f"Searching for {song_query} on Spotify.")
                # You can construct a Spotify search URL based on the user's query and open it in the web browser.
                search_url = f"https://open.spotify.com/search/{song_query}"
                webbrowser.open(search_url)

        #______________________
        elif 'send email' in query:
            speak("Processing")
            
        elif 'stop' in query or 'exit' in query:
            speak("Goodbye, Sir.")
            break

        
    takeCmd()