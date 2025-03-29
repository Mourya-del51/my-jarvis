import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification 
import pyautogui
import wikipedia
import pywhatkit as pwk
import user_config
import smtplib,ssl

engine = pyttsx3.init()
#voice
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",175)

def speak(command):
    engine.say(command)
    engine.runAndWait()
def command():
    content = " "
    while content == " ":
# obtain audio from the microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

    # recognize speech using Google Speech Recognition
        try:
            content= r.recognize_google(audio, language='en-in')
            print("you said............ " + content)
        except Exception as e:
            print("Please try again....")

    return content 

def main_process():
    while True:
        request = command().lower()
        if "hello" in request:
            speak("welcome, how can i help you.")
        elif "play music" in request:
            speak("playing music...")
            song = random.randint(1,5)
            if song  == 1:
                webbrowser.open("https://www.youtube.com/watch?v=K-Ts-NFR62o&list=RDK-Ts-NFR62o&start_radio=1")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=BLlTFapgvOo")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=O-I1VniQcvA")
            elif song == 4:
                webbrowser.open("https://www.youtube.com/watch?v=nNfHn4Jlc1M&list=RDMM&start_radio=1&rv=O-I1VniQcvA")
            elif song == 5:
                webbrowser.open("https://www.youtube.com/watch?v=CUFLws2mdqU")   
        elif "what is time" in request:   
                now_time = datetime.datetime.now().strftime("%H:%M")
                speak("current time is " + str(now_time))
        elif "what is date" in request:
                now_time = datetime.datetime.now().strftime("%d:%m")
                speak("date is " + str(now_time))
        elif "new task" in request:
                task = request.replace("new task","")
                task = task.strip()
                if task != "":
                     speak("adding task : "+ task)

                     with open ("todo.txt", "a") as file:
                          file.write(task + "\n")
        elif "speak task" in request:
            with open ("todo.txt", "r") as file:
                        speak("work we have to do today is : " + file.read())

                        
        elif "show work" in request:
            with open ("todo.txt", "r") as file:
                 task = file.read()
                 notification.notify(
                 title = " Today work",
                 message = task
            )

        elif "open youtube" in request:
            webbrowser.open("www.youtube.com") 


        elif "open" in request:
             query = request.replace("open","")
             pyautogui.press("super")
             pyautogui.typewrite(query)
             pyautogui.sleep(2)
             pyautogui.press("enter")

        elif "screenshort" in request:
             im1 = pyautogui.screenshot()
             im1.save("my_screenshot.png")
             speak("screenshort saved as im1.png")


        elif "wikipedia" in request:
             request = request.replace("jarvis","")
             request = request.replace("search wikipedia","")
             result = wikipedia.summary(request, sentences=2)
             speak(result)

        elif "search google" in request:
             request = request.replace("jarvis","")
             request = request.replace("search wikipedia","")
             webbrowser.open("https://www.google.com/search?q="+request)

        elif "send whatsapp" in request:
             pwk.sendwhatmsg("+8889240248", "Hi, how are you", 9, 52,30)
             speak("massage sent")

        # elif "send email" in request:
        #      pwk.send_mail("ashishmourya9755@gmail.com", user_config.gamil_password, "hello", "hello, how are you", "ashishmourya6263@gmail.com")
        #      speak("email sent")
        elif "send email" in request:
             s = smtplib.SMTP("smtp.gamil.com",587)
             s.starttls()
             s.login("ashishmourya6263@gmail.com",user_config.gmail_password)
             message ="""
                hello 
                |
                |
                |
                ->
                thankyou for understanding me:

                """
             s.sendmail("ashishmourya6263@gmail.com","ashishmourya9755@gmail.com", message)
             s.quit()
             speak("sent email successfully :")


             
main_process()   