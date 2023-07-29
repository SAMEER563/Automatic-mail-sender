import smtplib
import speech_recognition as sr
from email.message import EmailMessage
import pyttsx3

listenser = sr.Recognizer()
tts = pyttsx3.Engine()

def talking_tom(text):
    tts.say(text)
    tts.runAndWait()



def mic():
    with sr.Microphone() as source:
        
        print ("program is listening....")
        voice = listenser.listen(source)
        data = listenser.recognize_google(voice)
        print (data)
        return data.lower()
    
dict = {"jojo":"shakyasam563@gmail.com"}   

def send_mail(receiver, subject,body):
        
    server =smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    # server.login("","")
    server.login("abhishekkumarbaghel5804@gmail.com","jwihdrwqrjtyehbt")
    email = EmailMessage()
    email["From"] = "abhishekkumarbaghel5804@gmail.com"
    email["To"] = receiver
    email["subject"] = subject
    email.set_content(body)
    server.send_message(email)
    
    
def main_poc():
    
    talking_tom("TO WHO DO YOU WANT TO SEND THIS EMAIL?")
    name = mic()
    receiver = dict[name]
    talking_tom("SPEAK THE SUBJECT OF THE EMAIL")
    subject = mic()
    talking_tom("SPEAK THE MESSAGE OF THE EMAIL")
    body = mic()
    send_mail(receiver,subject,body)
    print ("your email has been sent !!")
        
main_poc()