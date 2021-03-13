import os
os.system('echo Welcome Harish | festival --tts')
from gpiozero import Button
import pytesseract
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import re

camera = PiCamera()
rawCapture = PiRGBArray(camera)
button = Button(2)

os.system('echo Initilization sucessful, press the button to start reading | festival --tts')
while True:
    if button.is_pressed:
        os.system('echo button pressed | festival --tts')
        camera.capture(rawCapture, format="bgr")
		frame = rawCapture.array
        raw_text = pytesseract.image_to_string(frame, config='')
        #print(repr(raw_text))
        text = re.sub('[^a-zA-Z]', ' ', raw_text)
        if text == '   ':
            text = 'No text found'
        os.system('echo ' + text + ' | festival --tts')
        os.system('echo End of reading. Press the button again to try another | festival --tts')