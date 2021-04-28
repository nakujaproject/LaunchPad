from flask import Flask, render_template, request
import time

app = Flask(__name__)

propulsionProgress = 0

@app.route("/")
def index():

	templateData = {
      'propulsionPercentage' : propulsionProgress,
      }
	return render_template('index.html', **templateData)
	

@app.route("/propulsion")
def propulsionIndex():
    templateData = {
        'propulsionPercentage' : propulsionProgress,
    }
    return render_template('propulsion.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)