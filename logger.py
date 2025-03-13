# Import time module
import time

# Create debug file if one doesn't exist
def log_to_file(log_data):
  with open('debug_log.txt', 'a') as file:
    # Write to debug file using set format and passed-in data
    file.write("{} - {}\n".format(time.strftime('%Y-%m-%d %H:%M:%S'), str(log_data)))
  # Print output to console
  print("Debug output: {}".format(str(log_data)))