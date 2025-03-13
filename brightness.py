# Import Sense HAT module and time module
from sense_hat import SenseHat
import time

# Set alias
s = SenseHat()

# Define colours using rgb values
white = (255, 255, 255)
nothing = (0, 0, 0)

# Set brightness based on param from main function
# Display Hi or Lo image based on setting
def adjust_brightness(low_light):
  if low_light == False:
    s.low_light = False
    s.set_pixels(draw_sun())
  elif low_light == True:
    s.low_light = True
    s.set_pixels(draw_moon())
  # Display image for 3 seconds
  # This ensures image displays long enough in case
  # extreme_temp_monitor images are active at the same time
  time.sleep(3)

# Sun image with "Hi" text
def draw_sun():
  W = white
  O = nothing
  sun = [
    O, O, O, O, O, W, W, O,
    O, O, O, O, W, W, W, W,
    O, O, O, O, W, W, W, W,
    W, O, W, O, O, W, W, O,
    W, O, W, O, W, O, O, O,
    W, W, W, O, O, O, O, O,
    W, O, W, O, W, O, O, O,
    W, O, W, O, W, O, O, O
  ]
  return sun

# Moon image with "Lo" text
def draw_moon():
  W = white
  O = nothing
  moon = [
    O, O, O, O, O, W, W, O,
    O, O, O, O, W, W, O, O,
    O, O, O, O, W, W, O, O,
    W, O, O, O, O, W, W, O,
    W, O, O, O, O, O, O, O,
    W, O, O, O, W, W, W, O,
    W, O, O, O, W, O, W, O,
    W, W, W, O, W, W, W, O
  ]
  return moon