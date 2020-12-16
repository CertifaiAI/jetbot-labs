import RPi.GPIO as GPIO
import time

GPIO.setmode("GPIO.BOARD") #Raspi board GPIO pin number

GPIO.setup(12, GPIO.OUT) #Board pin 12, BCM pin 18

#Initial state for LEDs:
print("Testing GPIO pin12 out, Press CTRL+C to exit")

    try:
        while True:
        print("Set GPIO 12 HIGH")
        GPIO.output(12, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(12, GPIO.LOW)
        time.sleep(1)

    except KeyboardInterrupt:
        print("Keyboard interrupt")

    except:
        print("some error")

    finally:
        print("clean up")
        GPIO.cleanup() #clean up all GPIO
