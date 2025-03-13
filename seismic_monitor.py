# Import Sense HAT module, logger and time module
from sense_hat import SenseHat
from logger import log_to_file
import time

# Set alias
s = SenseHat()

# Define colours using rgb values
red = (255, 0, 0)
white = (255, 255, 255)
nothing = (0, 0, 0)

# Continuously monitors changes in accelerometer axes
# Triggers alert if total value is larger than set value
def monitor_seismic_activity():
  # Gets raw x-, y- and z-axis accelerometer data
  x, y, z = s.get_accelerometer_raw().values()
  # Total absolute values of x, y and z
  total = abs(x) + abs(y) + abs(z)
  # Value can be changed to amend seismometer sensitivity
  if total > 1.1:
    alert()
    # Log sensor data if activity detected
    sensor_data = {'x': x, 'y': y, 'z': z}
    log_to_file(sensor_data)
    # Wait for 10 seconds before continuing to monitor
    time.sleep(10)
  
def alert():
  # Flash warning image
  count = 0
  while count < 3:
    s.set_pixels(draw_warning())
    time.sleep(0.5)
    s.clear()
    time.sleep(0.5)
    count += 1
  # Display warning message in red
  s.show_message("Warning! Seismic activity!", text_colour=[255, 0, 0], scroll_speed=0.04)
  # Clear screen
  s.clear()
        
# Exclamation mark with red square border
def draw_warning():
  R = red
  W = white
  O = nothing
  warning = [
    R, R, R, R, R, R, R, R,
    R, O, O, W, W, O, O, R,
    R, O, O, W, W, O, O, R,
    R, O, O, W, W, O, O, R,
    R, O, O, O, O, O, O, R,
    R, O, O, O, O, O, O, R,
    R, O, O, W, W, O, O, R,
    R, R, R, R, R, R, R, R
  ]
  return warning