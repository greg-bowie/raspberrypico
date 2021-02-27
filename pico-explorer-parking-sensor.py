# pico parking sensor example using the Pico Explorer

from machine import Pin
from utime import sleep_us, ticks_us, sleep
import picoexplorer as explorer

# setup display
width = explorer.get_width()
height = explorer.get_height()

display_buffer = bytearray(width*height*2)
explorer.init(display_buffer)

explorer.set_audio_pin(0)
audio_tone = 0
explorer.set_tone(audio_tone)

# set-up sensor
trig=Pin(3, Pin.OUT)
echo=Pin(2, Pin.IN)


# Function to calculate the distance travelled by the sensor
# and return the distance in centimetres.
def calc_cm(echo, trig):
    ## a 10 us signal to trig starts the internal ranging program of the sensor.
    trig.low()
    sleep_us(2)
    trig.high()
    sleep_us(10)
    trig.low()
    ## echo pin is set high when the first pulses are sent out, so wait for the echo to go high
    while echo.value() == 0:
        pass
    ## Now record the time, then wait until the echo pin goes low, which means the echo has been received.
    t1 = ticks_us()
    while echo.value() == 1:
        pass
    # Record the time again, as the echo has been received
    t2 = ticks_us()
    ## Calulate time difference.
    ## Speed of sound is approx 340m/s, which is 0.034 cm/us
    ## But the sound has traveled twice the distance, so need to / 2
    ## s = t * v
    ## s = (t2-t1) * 0.034 / 2
    ## s = (t2-t1) * 0.017 which is approximately
    cm = (t2 - t1) / 58.0
    return cm

# Start the loop.
while True:
    explorer.set_pen(120,40,60)
    explorer.clear()
    
    # retrieve the sensor distance calculation
    cm = calc_cm(echo, trig)
    # output to console for debugging
    explorer.set_pen(255, 255, 255)
    explorer.text(str(cm), 20, 20, 100)
    print(cm)
    # if less than 30 cms, then flash the on-board LED
    if cm < 30:
        audio_tone = 0
        explorer.text("*", 20, 40, 100)
    # if less than 15 cms, then also flash the yellow LED
    if cm < 15:
        explorer.text("***", 20, 40, 100)
        audio_tone = 300
    # if less than 5 cms, then also flash the red LED
    if cm < 5:
        explorer.text("*****", 20, 40, 100)
        audio_tone = 600
        
    explorer.set_tone(audio_tone)
    explorer.update()
        