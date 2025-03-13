# Import Sense HAT module, logger and heat index calculator
from sense_hat import SenseHat
from logger import log_to_file
from heat_index import calculate_heat_index

# Set alias
s = SenseHat()

def display_temperature():
  # Get temperature, assign to temp, round to 1 d.p.
  temp = s.get_temperature()
  temp = round(temp, 1)
  # Build message, output to user and log  
  temp_message = "Temperature: {}C".format(temp)
  s.show_message(temp_message, scroll_speed=0.05)
  log_to_file(temp_message)
  # Run heat index calculator
  calculate_heat_index()