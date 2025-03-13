# Import Sense HAT module and logger
from sense_hat import SenseHat
from logger import log_to_file

# Set alias
s = SenseHat()

def calculate_heat_index():
  # Heat index coefficients
  c1 = -8.78469475556
  c2 = 1.61139411
  c3 = 2.33854883889
  c4 = -0.14611605
  c5 = -0.012308094
  c6 = -0.0164248277778
  c7 = 0.002211732
  c8 = 0.00072546
  c9 = -0.000003582
  
  # Get temp and humidity values
  T = s.get_temperature()
  H = s.get_humidity()
  
  # Calculation
  heat_index = (c1 + (c2 * T) + (c3 * H) + (c4 * T * H) + 
                (c5 * T**2) + (c6 * H**2) + (c7 * T**2 * H) + 
                (c8 * T * H**2) + (c9 * T**2 * H**2))
                  
  # Round to 1 d.p.  
  heat_index = round(heat_index, 1)
  
  # Build and output user-facing and debug messages
  feels_like_message = "Feels like: {}C".format(heat_index)
  heat_index_message = "Heat index: {}C".format(heat_index)
  s.show_message(feels_like_message, scroll_speed=0.05)
  log_to_file(heat_index_message)