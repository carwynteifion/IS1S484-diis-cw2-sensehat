# Import Sense Hat API and logger
from sense_hat import SenseHat
from logger import log_to_file

# set alias
s = SenseHat()

def calculate_dew_point():
  # Get temperature and humidity values
  t = s.get_temperature()
  h = s.get_humidity()
  
  # Calculate the dew point and round to 1 decimal place
  dew_point = t - ((100 - h) / 5)
  dew_point = round(dew_point, 1)
  
  # Build message to show to user and write to logger
  dew_point_message = "Dew Point: {}C".format(dew_point)
  s.show_message(dew_point_message, scroll_speed=0.05)
  log_to_file(dew_point_message)