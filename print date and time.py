# Print Date and Time
import datetime

now = datetime.datetime.now()
print("Current date and time is: ")
print(now.strftime("%d-%m-%y %H:%M:%S"))