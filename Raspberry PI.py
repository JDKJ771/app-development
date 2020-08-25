from picamera import PiCamera
import datetime
import time
import SpeachRecognition
import pygame
import gtts
import google
import audyo
from gpiozero import button
###Camera commands
camera = Picamera()

camera.start_preview()
camera.dislplay

###GPIO Pins
button = Button(2)

if button.is_pressed:
      camera.capture("home/pi/desktop")

###Virtual assistant Start
