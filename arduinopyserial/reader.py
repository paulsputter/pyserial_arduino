#
# This is the best I can do so far to avoid sychronization miseries with
# Python not getting the number being sent by Arduino.
#



import serial
import sys
import time

ser = serial.Serial('COM4', baudrate = 9600, timeout = 2)
time.sleep(1) # Wait for arduino. Not sure why this is needed, but it is.

def getValues():
  arduinoData = ser.readline().decode().strip()
  return arduinoData
#counter = 0
lastValue = 0
while 1:
  sensorValue = getValues()
  #print(sensorValue)
  if(sensorValue.isnumeric()):
      sensorValue = int(sensorValue)
      #if(sensorValue != lastValue):
         #lastValue = sensorValue
      if(sensorValue == 1):
            print("ON")
      else:
            print("OFF")

 # sys.stdout.flush() # This helps if you're running from cygwin
