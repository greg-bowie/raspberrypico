import picodisplay as display
import machine
import utime

# Initial Setup - these must be done for any features to work
width = display.get_width()
height = display.get_height()
display_buffer = bytearray(width * height * 2)  # 2-bytes per pixel (RGB565)
display.init(display_buffer)

# Check the LED actually works
display.set_led(51, 153, 255) # set the LED to a blue shade
display.set_backlight(1.0)

# Define pen colours
black = display.create_pen(0, 0, 0)
white = display.create_pen(255,255,255)
green = display.create_pen(102, 255, 102)
display.set_pen(black)

# Now loop and handle button presses
while True:
    # Do buttons
    if display.is_pressed(display.BUTTON_A):
        # Display the temperature

        # Clear the display and set to black
        display.set_pen(black)
        display.set_backlight(1)
        display.set_led(0, 255, 0)
        display.clear()
        display.update()
        
        # Get the temperature
        sensor_temp = machine.ADC(4)
        conversion_factor = 3.3 / (65535)
        reading = sensor_temp.read_u16() * conversion_factor
        temperature = (27 - (reading - 0.706) / 0.001721)
        tempStr = "Temp = {:.{}f}".format(temperature, 2)
        
        # Update the display
        display.set_pen(white)
        display.text(tempStr, 0, 0, 240, 4)
        display.update()
        utime.sleep(2)
    if display.is_pressed(display.BUTTON_B):
        # Display uptime
        
        # Clear the display and set to black
        display.set_pen(black)
        display.set_backlight(1)
        display.set_led(0, 0, 255)
        display.clear()
        display.update()
        
        # Get the uptimetime
        nowtime = utime.time()
        year, month, monthday, hour, minute, second, weekday, yearday = utime.localtime(nowtime)
        current_time = "Uptime={hours}:{mins}:{seconds}".format(hours=hour, mins=minute, seconds=second)
        
        # Update the display
        display.set_pen(white)
        display.text("Pico Uptime:", 0, 0, 240, 4)
        display.text("{hours} hrs, {mins} mins, {secs} s".format(hours=hour, mins=minute, secs=second), 0, 30, 240, 2)
        display.update()
        utime.sleep(2)
    if display.is_pressed(display.BUTTON_X):
        # Pretend to close down
        display.set_led(0, 0, 0)
        display.set_backlight(0)
    if display.is_pressed(display.BUTTON_Y):
        # Some more ideas needed!
        display.set_led(255, 0, 0)

