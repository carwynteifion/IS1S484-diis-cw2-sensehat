# Import Sense HAT module
from sense_hat import SenseHat

# Set alias
s = SenseHat()

# Define colours using rgb values  
yellow = (255, 204, 0)
cyan = (0, 255, 255)
nothing = (0, 0, 0)

# Get temperature and round to 1 d.p.
def monitor_extreme_temp():
  temp = s.get_temperature()
  temp = round(temp, 1)
  # Display snowflake if temp is lower than 5C
  if temp < 5:
    s.set_pixels(draw_cold())
  # Display sun if temp is higher than 30C
  elif temp > 30:
    s.set_pixels(draw_hot())
  # Clear screen if temp is not extreme
  else:
    s.clear()

# Snowflake image
def draw_cold():
    C = cyan
    O = nothing
    snowflake = [
        O, O, C, O, O, C, O, O,
        O, O, O, C, C, O, O, O,
        O, O, C, C, C, C, O, O,
        C, C, C, O, O, C, C, C,
        C, C, C, O, O, C, C, C,
        O, O, C, C, C, C, O, O,
        O, O, O, C, C, O, O, O,
        O, O, C, O, O, C, O, O
    ]
    return snowflake

# Sun image
def draw_hot():
    Y = yellow
    O = nothing
    sun = [
        Y, Y, O, Y, Y, O, Y, Y,
        Y, Y, Y, O, O, Y, Y, Y,
        O, Y, Y, Y, Y, Y, Y, O,
        Y, O, Y, Y, Y, Y, O, Y,
        Y, O, Y, Y, Y, Y, O, Y,
        O, Y, Y, Y, Y, Y, Y, O,
        Y, Y, Y, O, O, Y, Y, Y,
        Y, Y, O, Y, Y, O, Y, Y
    ]
    return sun