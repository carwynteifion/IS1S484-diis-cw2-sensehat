# Importing Sense HAT module, time module and function scripts
from sense_hat import SenseHat
from dt_display import display_date_time
from brightness import adjust_brightness
from temp import display_temperature
from humidity import display_humidity
from pressure import display_pressure
from seismic_monitor import monitor_seismic_activity
from extreme_temp_monitor import monitor_extreme_temp
import time

# Set alias
s = SenseHat()

# Startup message
s.show_message("Ready!", scroll_speed=0.05)

# Main function
def main():
  # Declare last function for function cycling
  last_function = None
  while True:
    # Initialise background functions
    # These will trigger on change in motion and temperature
    monitor_seismic_activity()
    monitor_extreme_temp()
    # Joystick event handler
    for event in s.stick.get_events():
      # Function cycling between pressure, humidity and temp
      # If up button is pressed
      if event.direction == "up" and event.action == "pressed":
        if last_function == "pressure":
          display_humidity()
          # Set last function to the one that just ran
          last_function = "humidity"
        elif last_function == "humidity":
          display_temperature()
          last_function = "temp"
        else:
          display_pressure()
          last_function = "pressure"
      # Function cycling the other way
      # If down button is pressed
      if event.direction == "down" and event.action == "pressed":
        if last_function == "temp":
          display_humidity()
          last_function = "humidity"
        elif last_function == "humidity":
          display_pressure()
          last_function = "pressure"
        else:
          display_temperature()
          last_function = "temp"
      # If left button is pressed, lower brightness
      if event.direction == "left" and event.action == "pressed":
        adjust_brightness(True)
      # If right button is pressed, raise brightness
      if event.direction == "right" and event.action == "pressed":
        adjust_brightness(False)
      # If centre button is clicked, display date and time
      if event.direction == "middle" and event.action == "pressed":
        display_date_time()
        
# main() will only execute when run directly
if __name__ == "__main__":
  main()