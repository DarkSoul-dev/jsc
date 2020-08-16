import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia 
#import win32com.client

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)

	# if hour>=0 and hour<12:
	# 	speak("Good Morning!")
	  
	#   elif hour>=12 and hour<18:
	#   	speak("Good Afternon!")

	#   else:
	#   		speak("Good Evening!")

	#  speak("I am Jarvis Sir. Please tell me how may help you")

	if__name__=="__main__":
		speak("DarkSoul is evil")



