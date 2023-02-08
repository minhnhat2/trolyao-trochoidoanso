import pyttsx3
import datetime
from typing import Text
import sys
import ctypes
from random import randint
import json
import re
import turtle
from random import randint, choice   
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import perf_counter, strftime
from gtts import gTTS, tts
import speech_recognition as sr
from gtts import gTTS 
import webbrowser as wb
import os
import cv2
import pyautogui
import wikipedia
from webdriver_manager.chrome import ChromeDriverManager
import playsound
import nltk
from nltk.chat.util import Chat, reflections

nhat=pyttsx3.init()
voice=nhat.getProperty('voices')
nhat.setProperty('voice',voice[1].id) #void[0].id là nam ngược lại là nữ

def speak(audio):
    print('Nhat: ' + audio)
    nhat.say(audio)
    nhat.runAndWait()
speak("Hello , i am the botchat created by Minh Nhat and i will answer all question you can ")

def time(): 
    Time=datetime.datetime.now().strftime("Now is a %I: %M : %p") #I giờ , M phút , p buổi
    speak(Time)

def welcome():
    hour=datetime.datetime.now().hour
    if hour >=6 and hour < 12:
        speak("Hi  ,Good morning my friend")
    elif hour >=12 and hour < 18:
        speak("Hi ,Good afternoon my friend")
    if hour >=18 and hour < 24:
        speak("Hi , Good night my friend")
    speak("How can i help you ? ")

def search_wikipedia(query):
    # Tìm kiếm và đọc nội dung của một bài viết trên Wikipedia với từ khóa query
    try:
        page = wikipedia.page(query)
        content = page.content
        speak(content)
    except wikipedia.exceptions.DisambiguationError as e:
        # Xử lý lỗi trong trường hợp từ khóa query không chính xác
        print(e.options)

def command():
    c = sr.Recognizer()
    count = 0
    while True:
        with sr.Microphone() as source:
            c.pause_threshold = 2
            audio = c.listen(source)
        try:
            query = c.recognize_google(audio, language='en')
            print("Me: " + query)
            return query
        except sr.UnknownValueError:
            count += 1
            if count > 1:
                speak("I'm sorry, I didn't understand your question. Please type it out for me.")
                query = input("Your order is: ")
                return query
            else:
                speak("I'm sorry, I didn't understand your question. Please repeat it.")



if __name__=="__main__":
    welcome()
    while True:
        query=command().lower()
        if "open google"in query:
            speak("What should i search boss ? ")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        if "mở google"in query:
            speak("What should i search boss ? ")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        if "open youtube"in query:
            speak("What should i search boss ? ")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        if "mở youtube"in query:
            speak("What should i search boss ? ")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "open video"in query:
            meme=r"C:\Users\Le Minh Nhat\Downloads\Anh Da Đen - Facebook.mp4"
            os.startfile(meme)
        elif "mở video"in query:
            meme=r"C:\Users\Le Minh Nhat\Downloads\Anh Da Đen - Facebook.mp4"
            os.startfile(meme)
        elif "time" in query:
            time()
        elif "mấy giờ" in query:
            time()
        elif "chào" in query:
            speak("Hi,i can hear you , how can i help you ?")
        elif "hi" in query:
            speak("Hi,i can hear you , how can i help you ?")
        elif "hello" in query:
            speak("Hi,i can hear you , how can i help you ?")
        elif "hi my friend" in query:
            speak("Hi,i can hear you , how can i help you ?")
        elif "hello my friend " in query:
            speak("Hi,i can hear you , how can i help you ?")
        elif "your name" in query:
            speak("My name is Minh Nhat and i am is a chatbot was created by Nhat")
        elif "tên bạn" in query:
            speak("My name is Minh Nhat and i am is a chatbot was created by Nhat")
        elif "where're you from" in query:
            speak("I'm from Ho Chi Minh city , i was created by Minh Nhat")
        elif "đến từ đâu" in query:
            speak("I'm from Ho Chi Minh city , i was created by Minh Nhat")
        elif "where are you from" in query:
            speak("I'm from Ho Chi Minh city , i was created by Minh Nhat")
        elif "where're from" in query:
            speak("I'm from Ho Chi Minh city , i was created by Minh Nhat")
        elif "where from" in query:
            speak("I'm from Ho Chi Minh city , i was created by Minh Nhat")
        elif "where create" in query:
            speak("I'm from Ho Chi Minh city , i was created by Minh Nhat")
        elif "i want know" in query:
            speak("What should i search boss ? ")
            search=command().lower()
            search_wikipedia(query)
        elif "tìm hiểu về" in query:
            speak("What should i search boss ? ")
            search=command().lower()
            search_wikipedia(query)
        elif "how old are you" in query:
            speak("I'm one year old and my created was twenty one")
        elif "bao nhiêu tuổi" in query:
            speak("I'm one year old and my created was twenty one")
        elif "how old " in query:
            speak("I'm one year old and my created was twenty one")
        elif "you stupid" in query:
            speak("No,i think you are stupid")
        elif "you are stupid" in query:
            speak("No,i think you are stupid")
        elif "you're stupid" in query:
            speak("No,i think you are stupid")
        elif "good night" in query:
            speak("how can i help you")
        elif "good morning" in query:
            speak("how can i help you")
        elif "good everning" in query:
            speak("how can i help you")
        elif "do you speak " in query:
            speak("No, i only speak English , beacause my created so fool and don't know how to help me speak Vietnamese or more language")
        elif "game" in query:
            speak("click Start or F5 to play game")
            game=r"C:\Users\Le Minh Nhat\Pictures\PythonApplication4\PythonApplication4.sln"
            os.startfile(game)
        elif "play game" in query:
            speak("click Start or F5 to play game")
            game=r"C:\Users\Le Minh Nhat\Pictures\PythonApplication4\PythonApplication4.sln"
            os.startfile(game)
        elif "music" in query:
            music=r"C:\Users\Le Minh Nhat\Downloads\[Vietsub+TikTok] Lan Đình Tự - Châu Kiệt Luân -- 蘭亭序 - 周杰倫.mp4"
            os.startfile(music)
        elif "hear music" in query:
            music=r"C:\Users\Le Minh Nhat\Downloads\[Vietsub+TikTok] Lan Đình Tự - Châu Kiệt Luân -- 蘭亭序 - 周杰倫.mp4"
            os.startfile(music)
        elif "nghe nhạc" in query:
            music=r"C:\Users\Le Minh Nhat\Downloads\[Vietsub+TikTok] Lan Đình Tự - Châu Kiệt Luân -- 蘭亭序 - 周杰倫.mp4"
            os.startfile(music)
        elif "how are you" in query:
            speak("I'm fine , thanks for question !!!")
        elif "facebook"in query:
            speak("Are you sure ,i think you will have more time to use it ? ")
            search=command().lower()
            url=f"https://www.facebook.com/"
            wb.get().open(url)
        elif "word" in query:
            word=r"C:\Users\Le Minh Nhat\Desktop\Word.lnk"
            os.startfile(word)
        elif "excel" in query:
            excel=r"C:\Users\Le Minh Nhat\Desktop\Excel.lnk"
            os.startfile(excel)
        elif "visual" in query:
            visual=r"C:\Users\Le Minh Nhat\Desktop\Visual Studio 2022.lnk"
            os.startfile(visual)
        elif "code" in query:
            visual=r"C:\Users\Le Minh Nhat\Desktop\Visual Studio 2022.lnk"
            os.startfile(visual)
        elif "favorite footbool" in query:
            speak("My favorite footbool team is Manchester United")
            football_club=r"C:\Users\Le Minh Nhat\Downloads\M.U.png"
            os.startfile(football_club)
        elif "câu lạc bộ yêu thích" in query:
            speak("My favorite footbool team is Manchester United")
            football_club=r"C:\Users\Le Minh Nhat\Downloads\M.U.png"
            os.startfile(football_club)
        elif "tell me" in query:  #wiki
            search=command().lower()
            search_wikipedia(query)
        elif "image"in query:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cv2.imshow("Camera", frame)
            cv2.waitKey(0)
            cap.release()
        elif "chụp ảnh"in query:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cv2.imshow("Camera", frame)
            cv2.waitKey(0)
            cap.release()
        elif "picture"in query:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cv2.imshow("Camera", frame)
            cv2.waitKey(0)
            cap.release()
        elif "photo"in query:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cv2.imshow("Camera", frame)
            cv2.waitKey(0)
            cap.release()
        elif "who is stupid"in query:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cv2.imshow("Camera", frame)
            cv2.waitKey(0)
            cap.release()
        elif "who stupid"in query:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            cv2.imshow("Camera", frame)
            cv2.waitKey(0)
            cap.release()
        elif "sad"in query:
            speak("I sympathize with you, Do you need me any help to be more comfortable ?")
        elif "bored"in query:
            speak("I sympathize with you, Do you need me any help to be more comfortable ?")
        elif "happy"in query:
            speak("Great, i like that,Do you need me any help today?")
        elif "vui"in query:
            speak("Great, i like that,Do you need me any help today?")
        elif "bad"in query:
            speak("I sympathize with you, Do you need me any help to be more comfortable ?")
        elif "good"in query:
            speak("Great, i like that,Do you need me any help today?")
        elif "greet"in query:
            speak("Great, i like that,Do you need me any help today?")
        elif "story"in query:
            speak("Yes,Here I will tell you a story. A disappointed wife about her husband or working late, so confided to you. She advised: Instead of hooking him, say sweet words and welcome him with a kiss. Maybe he will change. That night, the husband returned late, his wife hurriedly opened the door, helped him into the room, covered cold towels and took off his shoes. While squeezing, the wife whispered in her husband's ear: I love, it's too late, let's go to sleep. The husband was dull and answered: Yes, that's fine. Anyway, my wife's wife and children do not forgive ... . HaHaHaHa")
        elif "stories"in query:
            speak("Yes,Here I will tell you a story. A disappointed wife about her husband or working late, so confided to you. She advised: Instead of hooking him, say sweet words and welcome him with a kiss. Maybe he will change. That night, the husband returned late, his wife hurriedly opened the door, helped him into the room, covered cold towels and took off his shoes. While squeezing, the wife whispered in her husband's ear: I love, it's too late, let's go to sleep. The husband was dull and answered: Yes, that's fine. Anyway, my wife's wife and children do not forgive ... . HaHaHaHa")
        elif "comedy"in query:
            speak("Yes,Here I will tell you a story. A disappointed wife about her husband or working late, so confided to you. She advised: Instead of hooking him, say sweet words and welcome him with a kiss. Maybe he will change. That night, the husband returned late, his wife hurriedly opened the door, helped him into the room, covered cold towels and took off his shoes. While squeezing, the wife whispered in her husband's ear: I love, it's too late, let's go to sleep. The husband was dull and answered: Yes, that's fine. Anyway, my wife's wife and children do not forgive ... . HaHaHaHa")
        elif "other comedy"in query:
            speak("Yes,Here I will tell you a story.Two blonde girls gossiped about giving gifts ... Last time I told my boyfriend that girls love to keep the items given. As a result, the next day I was given a diamond ring. Have you tried to learn this way? This way I used it. As a result, the next day I was given preservatives.HaHaHaHaHa")
        elif "other story"in query:
            speak("Yes,Here I will tell you a story.Two blonde girls gossiped about giving gifts ... Last time I told my boyfriend that girls love to keep the items given. As a result, the next day I was given a diamond ring. Have you tried to learn this way? This way I used it. As a result, the next day I was given preservatives.HaHaHaHaHa")
        elif "other stories"in query:
            speak("Yes,Here I will tell you a story.Two blonde girls gossiped about giving gifts ... Last time I told my boyfriend that girls love to keep the items given. As a result, the next day I was given a diamond ring. Have you tried to learn this way? This way I used it. As a result, the next day I was given preservatives.HaHaHaHaha")
        if "open map"in query:
            speak("What should i search boss ? ")
            search=command().lower()
            url=f"https://www.google.com/maps/place/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on map')
        if "where"in query:
            speak("What should i search boss ? ")
            search=command().lower()
            url=f"https://www.google.com/maps/place/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on map')
        if "location"in query:
            speak("What should i search boss ? ")
            search=command().lower()
            url=f"https://www.google.com/maps/place/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on map')
        if "địa điểm"in query:
            speak("What should i search boss ? ")
            search=command().lower()
            url=f"https://www.google.com/maps/place/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on map')
        elif "hear"in query:
            speak("Yes, i am listening")
        elif"open zalo"in query:
            zalo=r"C:\Users\Le Minh Nhat\Desktop\Zalo.lnk"
            os.startfile(zalo)
        elif "wiki" in query:  #wiki
            speak("What should i search boss ? ")
            search=command().lower()
            search_wikipedia(query)
        elif "wikipedia" in query:  #wiki
            speak("What should i search boss ? ")
            search=command().lower()
            search_wikipedia(query)
        elif "i don't know" in query:  #wiki
            speak("What do you not understand? ")
            search=command().lower()
            search_wikipedia(query)
        elif "i don't no" in query:  #wiki
            speak("What do you not understand? ")
            search=command().lower()
            search_wikipedia(query)
        elif "open newpaper"in query:
            search=command().lower()
            url=f"https://vnexpress.net/"
            wb.get().open(url)
            speak(f'Here is newpaper')
        elif "happy birthday"in query:
            speak("Happy Birtday my boss, I LOVE YOU")
            for i in range(1,45):
                print('')
            s=''
            for i in range(1,1000):
                count = randint(1,100)
                while (count > 0):
                    s+=' '
                    count-=1
                if (i % 10 ==0):
                    print(s + 'Happy Birtday')
                else:
                    print(s + '*')

                s=''
        elif "happy new year"in query:
            width = 700
            height = 500
            S = turtle.Screen()
            S.setup(width, height)
            S.bgcolor('black')
            S.title("Fireworks")
            colors = ['red', 'green', 'yellow', 'gold', 'pink', 'cyan', 'white', 'orange','violet', 'coral']
            class Fireworks:
                def __init__(self, radius):
                    self.T = turtle.Pen()
                    self.T.speed(0)
                    self.T.color(choice(colors))
                    self.T.hideturtle()
                    self.T.up()
                    self.T.setposition(randint(-250, 250), randint(0, 200))
                    self.T.down()
                    self.radius = radius
                def update(self):
                    self.T.forward(self.radius)
                    self.T.backward(self.radius)
                    self.T.left(10)
                def clean(self):
                    self.T.clear()
                    self.T.color(choice(colors))
                    self.T.up()
                    self.T.setposition(randint(-250, 250), randint(0, 200))
                    self.T.down()
            T1 = Fireworks(randint(10, 100))
            T2 = Fireworks(randint(10, 100))
            T3 = Fireworks(randint(10, 100))
            T4 = Fireworks(randint(10, 100))
            T5 = Fireworks(randint(10, 100))
            T = turtle.Pen()
            T.sety(-150)
            T.color('gold')
            T.write('Happy New Year 2023!', align='center', font=(None, 50))
            T.hideturtle()
            while True:
                for i in range(36):
                    T1.update()
                    T2.update()
                    T3.update()
                    T4.update()
                    T5.update()
                T1.clearn()
                T2.clearn()
                T3.clearn()
                T4.clearn()
                T5.clearn()
        elif "picture new year"in query:
            width = 700
            height = 500
            S = turtle.Screen()
            S.setup(width, height)
            S.bgcolor('black')
            S.title("Fireworks")
            colors = ['red', 'green', 'yellow', 'gold', 'pink', 'cyan', 'white', 'orange','violet', 'coral']
            class Fireworks:
                def __init__(self, radius):
                    self.T = turtle.Pen()
                    self.T.speed(0)
                    self.T.color(choice(colors))
                    self.T.hideturtle()
                    self.T.up()
                    self.T.setposition(randint(-250, 250), randint(0, 200))
                    self.T.down()
                    self.radius = radius
                def update(self):
                    self.T.forward(self.radius)
                    self.T.backward(self.radius)
                    self.T.left(10)
                def clean(self):
                    self.T.clear()
                    self.T.color(choice(colors))
                    self.T.up()
                    self.T.setposition(randint(-250, 250), randint(0, 200))
                    self.T.down()
            T1 = Fireworks(randint(10, 100))
            T2 = Fireworks(randint(10, 100))
            T3 = Fireworks(randint(10, 100))
            T4 = Fireworks(randint(10, 100))
            T5 = Fireworks(randint(10, 100))
            T = turtle.Pen()
            T.sety(-150)
            T.color('gold')
            T.write('Happy New Year 2023!', align='center', font=(None, 50))
            T.hideturtle()
            while True:
                for i in range(36):
                    T1.update()
                    T2.update()
                    T3.update()
                    T4.update()
                    T5.update()
                T1.clearn()
                T2.clearn()
                T3.clearn()
                T4.clearn()
                T5.clearn()
       
