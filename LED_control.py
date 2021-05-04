from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

led1 = LED(14)
led2 = LED(15)
led3 = LED(18)

box = Tk()
box.title("LED control")
Font = tkinter.font.Font(family = "Helvetica", size = 10)

def led1Control():
    if led1.is_lit:
        led1.off()
        button1["text"] = "Turn LED on"
        
    else:
        led1.on()
        button1["text"] = "Turn LED off"
        

def led2Control():
    if led2.is_lit:
        led2.off()
        button2["text"] = "Turn LED on"
        
    else:
        led2.on()
        button2["text"] = "Turn LED off"
        

def led3Control():
    if led3.is_lit:
        led3.off()
        button3["text"] = "Turn LED on"
        
    else:
        led3.on()
        button3["text"] = "Turn LED off"

button1 = Button(box, text = "Toggle green LED", font = Font, command = led1Control, bg="green", height = 1, width = 30)
button1.grid(row=0, column=1)

button2 = Button(box, text = "Toggle red LED", font = Font, command = led2Control, bg="red", height = 1, width = 30)
button2.grid(row=1, column=1)

button3 = Button(box, text = "Toggle yellow LED", font = Font, command = led3Control, bg="yellow", height = 1, width = 30)
button3.grid(row=2, column=1)
