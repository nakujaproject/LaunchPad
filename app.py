#import RPi.GPIO as GPIO
from flask import Flask, render_template, request
#from modules.ignition import *
import time

app = Flask(__name__)

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

#define actuators GPIOs
ledRed = 19

#initialize GPIO status variables
ledRedSts = 0

# Define led pins as output
#GPIO.setup(ledRed, GPIO.OUT)   

# turn leds OFF 
#GPIO.output(ledRed, GPIO.LOW)

testNum = 0

#ignitionThreads = []

@app.route("/")
def index():
	global testNum
	# Read GPIO Status
	#ledRedSts = GPIO.input(ledRed)

	templateData = {
      'ledRed'  : ledRedSts,
	  'testNum' : testNum,
      }
	return render_template('index.html', **templateData)
	

@app.route("/propulsion")
def propulsionIndex():
    templateData = {
        'propulsionPercentage' : 10,
    }
    return render_template('propulsion.html', **templateData)

# The function below is executed when someone requests a URL with the actuator name and action in it:
@app.route("/<deviceName>/<action>")
def action(deviceName, action):
	global testNum
	if deviceName == 'ledRed':
		actuator = ledRed
   
	if action == "on":
		t1 = Ignition(actuator)
		ignitionThreads.append(t1)
		ignitionThreads[testNum].start()
		ignitionThreads[testNum].stop()
		testNum = testNum + 1
	
	if action == "off":
		GPIO.output(actuator, GPIO.LOW)
		     
	ledRedSts = GPIO.input(ledRed)
   
	templateData = {
      'ledRed'  : ledRedSts,
	  'testNum' : testNum,
	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)