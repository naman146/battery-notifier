from win10toast import ToastNotifier
from psutil import sensors_battery
import time

toast= ToastNotifier()
battery = sensors_battery()
isPlugged = battery.power_plugged
percentage = battery.percent
isNotifiedLow = False
isNotifiedHigh = False

while(True):
	if isNotifiedHigh == False and isNotifiedLow == False:
		if percentage <=84 and isPlugged == False and isNotifiedLow == False:
			toast.show_toast("Battery Percentage is " + str(percentage) + "% \nConnect the charger now")
			isNotifiedLow = True
		elif percentage >=85 and isPlugged == True and isNotifiedHigh == False:
			toast.show_toast("Battery Percentage is now " + str(percentage) + "%. \nKindly remove the charger")
			isNotifiedHigh = True
	elif isNotifiedLow == True and isPlugged == True:
		isNotifiedLow = False
	elif isNotifiedHigh == True and isPlugged == False:
		isNotifiedHigh = False
	battery = sensors_battery()
	isPlugged = battery.power_plugged
	percentage = battery.percent
	time.sleep(10)
