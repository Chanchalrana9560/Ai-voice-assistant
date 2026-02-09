import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os


# pip install pocketphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "Your_API_KEY"


def speak_old(text):
  engine.say(text)
  engine.runAndWait()

def speak(text):
 tts = gTTS(text)
 tts.save('hello.mp3')

 # Initialize Pygame mixer
 pygame.mixer.init()
 # Load the MP3 file
 pygame.mixer.music.load('hello.mp3')
 # Play the MP3 file
 pygame.mixer.music.play()

 # Keep the progran running untill the music stops playing
 while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(10)  
 pygame.mixer.music.unload()       
 os.remove("hello.mp3")
 

def aiProcess(command):
   client = OpenAI(api_key="Your_API_KEY"),

   completion = client.chat.completions.create(
   model="gpt-4o-mini",
   messages=[
        {"role": "system", "content": "You are a virtual assistant skilled in general tasks like Alexa and Google Cloud. Give short responses"},
        {"role": "user", "content": "command"}
    ]
   )

   return completion.choices[0].message.content

def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif  "open youtube" in c.lower():
      webbrowser.open("https://youtube.com")   
   elif  "open facebook" in c.lower():
      webbrowser.open("https://facebook.com") 
   elif  "open linkedin" in c.lower():
      webbrowser.open("https://linkedin.com")       

   elif c.lower().startswith("play"):
     song = c.lower().split(" ")[1]
     link = musicLibrary.music[song]   
     webbrowser.open(link)

   elif "news" in c.lower():
      r = requests.get(f"Your_API_KEYs")

      if r.status_code == 200:
         # Parse the JSON response
         data = r.json()

         # Extract the articles
         articles = data.get('articles', [])

         # Print the headlines
         for article in articles:
            speak(article['title'])

   else:
      # Let OpenAI handle the request
      output = aiProcess(c)
      speak(output)
               


if __name__ == "__main__":
  speak("Initializing Mj....")
  while True:
    # Listen for the wake word "Mj"
    # obtain audio from the microphone

    r = sr.Recognizer() 
 
    print("recognizing...")
    try:
        with sr.Microphone() as source: 
         print("Listening...")
         audio = r.listen(source, timeout=10, phrase_time_limit=8)
        word = r.recognize_google(audio, language="en-IN")  
        if(word.lower() == "Mj"):
          speak("Ya")
          # Listen for command
          with sr.Microphone() as source: 
             print("Mj Active....")
             audio = r.listen(source)
             command = r.recognize_google(audio) 

             processCommand(command)

    except Exception as e:
      print("Error; {0}".format(e))        