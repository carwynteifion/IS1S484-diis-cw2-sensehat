# Importing Sense HAT module and datetime module
from sense_hat import SenseHat
import datetime as dt

# Set alias
s = SenseHat()

def display_date_time():
  # Set now to the current date and time
  now = dt.datetime.now()
  
  # Display the current date and time in a defined format
  # Day, date, month, year, hours, minutes, seconds
  current_time = now.strftime("%A, %d %B %Y %H:%M:%S")
  # Output to user
  s.show_message(
    current_time, scroll_speed=0.05, text_colour=[255, 255, 255]
  )