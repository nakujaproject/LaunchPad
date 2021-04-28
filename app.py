from flask import Flask, render_template, request

app = Flask(__name__)

#propulsion task bar
propulsionProgress = 0

#propulsion number of tasks
propulsionNumTasks = 6

#propulsion task list
propulsionTaskList = [""] * propulsionNumTasks

@app.route("/")
def index():

	templateData = {
      'propulsionPercentage' : propulsionProgress,
      }
	return render_template('index.html', **templateData)
	

@app.route("/<group>")
def groupIndex(group):
    if group == "propulsion" :
        templateData = {
            'propulsionPercentage' : propulsionProgress,
            'propulsionTask1' : propulsionTaskList[0],
            'propulsionTask2' : propulsionTaskList[1],
            'propulsionTask3' : propulsionTaskList[2],
            'propulsionTask4' : propulsionTaskList[3],
            'propulsionTask5' : propulsionTaskList[4],
            'propulsionTask6' : propulsionTaskList[5],
        }
        return render_template('propulsion.html', **templateData)

@app.route("/<group>/<task>/<taskNum>")
def propulsionTasks(group, task, taskNum):
    # complete a task and check it
    taskNum = int(taskNum)
    if propulsionTaskList[taskNum - 1] == "":
        propulsionTaskList[taskNum - 1] = "checked"
    # remove task if unchecked
    else:
        propulsionTaskList[taskNum - 1] = 0
    templateData = {
            'propulsionPercentage' : propulsionProgress,
            'propulsionTask1' : propulsionTaskList[0],
            'propulsionTask2' : propulsionTaskList[1],
            'propulsionTask3' : propulsionTaskList[2],
            'propulsionTask4' : propulsionTaskList[3],
            'propulsionTask5' : propulsionTaskList[4],
            'propulsionTask6' : propulsionTaskList[5],
        }
    return render_template('propulsion.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)