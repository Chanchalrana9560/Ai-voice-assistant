import speech_recognition as sr

def processCommand(cmd):
    print("You said:", cmd)

try:
    r = sr.Recognizer()
    print("Mj Active....")

    with sr.Microphone() as source:
        audio = r.listen(source)
        command = r.recognize_google(audio)

    processCommand(command)

except Exception as e:
    print("Error:", e)