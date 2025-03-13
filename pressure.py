# Import Sense HAT module and logger
from sense_hat import SenseHat
from logger import log_to_file

# Set alias
s = SenseHat()

def display_pressure():
  # Get pressure, assign to variable, round to 1 d.p.
  pressure = s.get_pressure()
  pressure = round(pressure, 1)
  # Build message, output to user and log
  pressure_message = "Pressure: {}mb".format(pressure)
  s.show_message(pressure_message, scroll_speed=0.05)
  log_to_file(pressure_message)