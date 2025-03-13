# Import Sense HAT module, logger and dew point calculator
from sense_hat import SenseHat
from logger import log_to_file
from dew_point import calculate_dew_point

# Set alias
s = SenseHat()

def display_humidity():
  # Get humidity, assign to variable, round to 1 d.p.
  humidity = s.get_humidity()
  humidity = round(humidity, 1)
  # Build message, output to user and log
  humidity_message = "Humidity: {}%".format(humidity)
  s.show_message(humidity_message, scroll_speed=0.05)
  log_to_file(humidity_message)
  # Run dew point calculator
  calculate_dew_point()