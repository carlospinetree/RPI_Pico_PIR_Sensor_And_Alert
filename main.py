from machine import Pin
from time import sleep

# GLOBAL VARIABLES
LED = Pin(14, Pin.OUT)
PIR_sensor = Pin(13, Pin.IN, Pin.PULL_UP)

# Startup signaling
def ledStartupSignal():
    LED.low()
    
    for i in range(6):
        LED.toggle()
        sleep(0.2)
    
# PIR Interrupt Handler - called when motion is / is not detected (sensor changes state)
def pirSensorInterruptHandler(pin):
   if PIR_sensor.value() == 1:
       print("Motion Detected! -> LED is now ON")
       LED.high()
   else:
       print("No motion detected -> LED is OFF")
       LED.low()
    

# Main
def main():
    print("Program starting...")
    ledStartupSignal()    
    PIR_sensor.irq(trigger=Pin.IRQ_FALLING|Pin.IRQ_RISING, handler=pirSensorInterruptHandler)
    print("Program initialized")


main()