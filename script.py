#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from collections import defaultdict
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import speech_recognition as sr
from gtts import gTTS
import pyaudio
import os

r = sr.Recognizer()

################################################################################
def speak(text): # SPEAK THE GIVEN TEXT (IN THE ARGUMENT)

    tts = gTTS(text=text, lang='hi')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")
################################################################################


##############################################################################################################
def voice_input(): # OBTAIN THE VOICE INPUT FROM SOURCE AND RETURN THE TEXT USING GOOGLE VOICE RECOGNITION API

    print ("voice_fun_opened")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    print r.recognize_google(audio)
    return r.recognize_google(audio)
###############################################################################################################

voice_input()




################################################################################################################################
speak('Hello Welcome to this app. I am your voice assistant. I am just starting your app in few second. please wait. Thank you')

#SELENIUM SETUP
chromedriver = 'C:\webdrivers'  # YOUR CHROMEDRIVER PATH COMES IN HERE
browser=webdriver.Chrome(chromedriver)
browser.maximize_window()
browser.get("https://www.google.com/gmail/")   # URL OF GMAIL

speak('Here you go. Gmail is opened now')
################################################################################################################################






############################################################################################################################
#KEEP GETTING THE USERNAME FROM USER UNTILL IT IS CORRECT.
speak('Please Tell me your username')

while(1):
    gmail_username = voice_input()
    speak('Your username is' + gmail_username +". Do you want to continue or do you want to tell me your username again")
    Confirm = voice_input()
    if "again" in Confirm:
        speak('allright. Please tell me your username again')
        continue

    if "correct" in Confirm:
        break;

gmail_username.replace(" ","")
print gmail_username
username = browser.find_elements_by_xpath('//*[@id="identifierId"]')
username[0].send_keys(gmail_username)
##############################################################################################################################





#####################################################################################################################
# CLICKING ON NEXT BUTTON
Next = browser.find_elements_by_xpath('//*[@id="identifierNext"]/content')
Next[0].click()
WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
######################################################################################################################




##############################################################################################################################
#KEEP GETTING THE PASSWORD FROM THE USER UNTILL IT IS CORRECT
while(1):
    speak('Now tell me your password')
    gmail_password = voice_input()
    password = browser.find_elements_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
    password[0].send_keys(gmail_password)
    speak('Your password is' + gmail_password +". Do you want to continue or do you want to tell me your password again")
    break
##############################################################################################################################



# NOW CLICKING ON THE NEXT BUTTON TO CONTINUE TO LOGIN
browser.find_elements_by_xpath('//*[@id="passwordNext"]/content')[0].click()
WebDriverWait(browser,135).until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":i8"]/div/div')))




try:
    audio = voice_input()
    print audio
    if(str(audio)=='compose mail'):
        browser.find_elements_by_xpath('//*[@id=":i8"]/div/div')[0].click()
        WebDriverWait(browser,15).until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":125"]')))
        print "to whom??"
        audio = voice_input()
        print audio
        if(str(audio)=='default'):
            browser.find_elements_by_xpath('//*[@id=":12w"]')[0].send_keys('kumarshubham238@gmail.com')
            browser.find_elements_by_xpath('//*[@id=":12f"]')[0].send_keys('Automated mail send by voice')
            audio = voice_input()
            print audio
            browser.find_elements_by_xpath('//*[@id=":13g"]')[0].send_keys(str(audio))
            browser.find_elements_by_xpath('//*[@id=":125"]')[0].click()

except:
    print("Could not request results from Google Speech Recognition service")
