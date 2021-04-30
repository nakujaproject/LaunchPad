from flask import Flask, render_template, request, json, jsonify
import numpy as np

app = Flask(__name__)

# propulsion task bar
propulsionProgress = 0

# propulsion number of tasks
propulsionNumTasks = 6

# propulsion task list
propulsionTaskList = [""] * propulsionNumTasks

# airframe task bar
airframeProgress = 0

# airframe number of tasks
airframeNumTasks = 10

# airframe task list
airframeTaskList = [""] * airframeNumTasks

# avionics task bar
avionicsProgress = 0

# avionics number of tasks
avionicsNumTasks = 6

# avionics task list
avionicsTaskList = [""] * avionicsNumTasks

avionics_check = 0

# team go status
goStatus = np.zeros(3)


@app.route("/")
def index():

    templateData = {
        'propulsionPercentage': propulsionProgress,
        'airframePercentage': airframeProgress,
        'avionicsPercentage': avionicsProgress,
    }
    return render_template('index.html', **templateData)


@app.route("/propulsion")
def groupIndex():
    templateData = {
        'propulsionPercentage': propulsionProgress,
        'propulsionTask1': propulsionTaskList[0],
        'propulsionTask2': propulsionTaskList[1],
        'propulsionTask3': propulsionTaskList[2],
        'propulsionTask4': propulsionTaskList[3],
        'propulsionTask5': propulsionTaskList[4],
        'propulsionTask6': propulsionTaskList[5],
        'propulsionWarnings': "None",
    }
    return render_template('propulsion.html', **templateData)


@app.route("/airframe")
def airframegroupIndex():
    templateData = {
        'airframePercentage': airframeProgress,
        'airframeTask1': airframeTaskList[0],
        'airframeTask2': airframeTaskList[1],
        'airframeTask3': airframeTaskList[2],
        'airframeTask4': airframeTaskList[3],
        'airframeTask5': airframeTaskList[4],
        'airframeTask6': airframeTaskList[5],
        'airframeTask7': airframeTaskList[6],
        'airframeTask8': airframeTaskList[7],
        'airframeTask9': airframeTaskList[8],
        'airframeTask10': airframeTaskList[9],
        'airframeWarnings': "None",
    }
    return render_template('airframe.html', **templateData)


@app.route("/avionics")
def avionicsgroupIndex():
    templateData = {
        'avionicsPercentage': avionicsProgress,
        'avionicsTask1': avionicsTaskList[0],
        'avionicsTask2': avionicsTaskList[1],
        'avionicsTask3': avionicsTaskList[2],
        'avionicsTask4': avionicsTaskList[3],
        'avionicsTask5': avionicsTaskList[4],
        'avionicsTask6': avionicsTaskList[5],
        'avionicsWarnings': "None",
    }
    return render_template('Avionics.html', **templateData)


@app.route("/propulsion/Task/<taskNum>")
def propulsionTasks(taskNum):
    global propulsionProgress, propulsionTaskList
    # complete a task and check it
    taskNum = int(taskNum)
    if propulsionTaskList[taskNum - 1] == "":
        propulsionTaskList[taskNum - 1] = "checked"
    # remove task if unchecked
    else:
        propulsionTaskList[taskNum - 1] = ""

    propulsionProgress = propulsionTaskList.count(
        "checked") / propulsionNumTasks * 100
    templateData = {
        'propulsionPercentage': propulsionProgress,
        'propulsionTask1': propulsionTaskList[0],
        'propulsionTask2': propulsionTaskList[1],
        'propulsionTask3': propulsionTaskList[2],
        'propulsionTask4': propulsionTaskList[3],
        'propulsionTask5': propulsionTaskList[4],
        'propulsionTask6': propulsionTaskList[5],
        'propulsionWarnings': "None",
    }
    return render_template('propulsion.html', **templateData)


@app.route("/airframe/Task/<taskNum>")
def airframeTasks(taskNum):
    global airframeProgress, airframeTaskList
    # complete a task and check it
    taskNum = int(taskNum)
    if airframeTaskList[taskNum - 1] == "":
        airframeTaskList[taskNum - 1] = "checked"
    # remove task if unchecked
    else:
        airframeTaskList[taskNum - 1] = ""

    airframeProgress = airframeTaskList.count(
        "checked") / airframeNumTasks * 100
    templateData = {
        'airframePercentage': airframeProgress,
        'airframeTask1': airframeTaskList[0],
        'airframeTask2': airframeTaskList[1],
        'airframeTask3': airframeTaskList[2],
        'airframeTask4': airframeTaskList[3],
        'airframeTask5': airframeTaskList[4],
        'airframeTask6': airframeTaskList[5],
        'airframeTask7': airframeTaskList[6],
        'airframeTask8': airframeTaskList[7],
        'airframeTask9': airframeTaskList[8],
        'airframeTask10': airframeTaskList[9],
        'airframeWarnings': "None",
    }
    return render_template('airframe.html', **templateData)


@app.route("/avionics/Task/<taskNum>")
def avionicsTasks(taskNum):
    global avionicsProgress, avionicsTaskList
    # complete a task and check it
    taskNum = int(taskNum)
    if avionicsTaskList[taskNum - 1] == "":
        avionicsTaskList[taskNum - 1] = "checked"
    # remove task if unchecked
    else:
        avionicsTaskList[taskNum - 1] = ""

    avionicsProgress = avionicsTaskList.count(
        "checked") / avionicsNumTasks * 100
    templateData = {
        'avionicsPercentage': avionicsProgress,
        'avionicsTask1': avionicsTaskList[0],
        'avionicsTask2': avionicsTaskList[1],
        'avionicsTask3': avionicsTaskList[2],
        'avionicsTask4': avionicsTaskList[3],
        'avionicsTask5': avionicsTaskList[4],
        'avionicsTask6': avionicsTaskList[5],
        'avionicsWarnings': "None",
    }
    return render_template('Avionics.html', **templateData)


@app.route("/propulsion/<action>")
def propulsionActions(action):
    global propulsionProgress, propulsionTaskList, goStatus
    if action == "abort":
        propulsionProgress = 0
        propulsionTaskList = [""] * propulsionNumTasks
        warnings = "None"
    elif action == "go":
        if propulsionProgress == 100:
            goStatus[0] = 1
            warnings = "None"
        else:
            # print out warnings
            warnings = "incomplete tasks"

    templateData = {
        'propulsionPercentage': propulsionProgress,
        'propulsionTask1': propulsionTaskList[0],
        'propulsionTask2': propulsionTaskList[1],
        'propulsionTask3': propulsionTaskList[2],
        'propulsionTask4': propulsionTaskList[3],
        'propulsionTask5': propulsionTaskList[4],
        'propulsionTask6': propulsionTaskList[5],
        'propulsionWarnings': warnings,
    }
    return render_template('propulsion.html', **templateData)


@app.route("/airframe/<action>")
def airframeActions(action):
    global airframeProgress, airframeTaskList, goStatus
    if action == "abort":
        airframeProgress = 0
        airframeTaskList = [""] * airframeNumTasks
        warnings = "None"
    elif action == "go":
        if airframeProgress == 100:
            goStatus[0] = 1
            warnings = "None"
        else:
            # print out warnings
            warnings = "incomplete tasks"

    templateData = {
        'airframePercentage': airframeProgress,
        'airframeTask1': airframeTaskList[0],
        'airframeTask2': airframeTaskList[1],
        'airframeTask3': airframeTaskList[2],
        'airframeTask4': airframeTaskList[3],
        'airframeTask5': airframeTaskList[4],
        'airframeTask6': airframeTaskList[5],
        'airframeTask7': airframeTaskList[6],
        'airframeTask8': airframeTaskList[7],
        'airframeTask9': airframeTaskList[8],
        'airframeTask10': airframeTaskList[9],
        'airframeWarnings': warnings,
    }
    return render_template('airframe.html', **templateData)


@app.route("/avionics/<action>")
def avionicsActions(action):
    global avionicsProgress, avionicsTaskList, goStatus
    if action == "abort":
        avionicsProgress = 0
        avionicsTaskList = [""] * avionicsNumTasks
        warnings = "None"
    elif action == "go":
        if avionicsProgress == 100:
            goStatus[0] = 1
            warnings = "None"
        else:
            # print out warnings
            warnings = "incomplete tasks"

    templateData = {
        'avionicsPercentage': avionicsProgress,
        'avionicsTask1': avionicsTaskList[0],
        'avionicsTask2': avionicsTaskList[1],
        'avionicsTask3': avionicsTaskList[2],
        'avionicsTask4': avionicsTaskList[3],
        'avionicsTask5': avionicsTaskList[4],
        'avionicsTask6': avionicsTaskList[5],
        'avionicsWarnings': warnings,
    }
    return render_template('Avionics.html', **templateData)


@app.route('/avionics/start-logging', methods=['GET'])
def get_tasks():
    response = {
        "status": avionics_check
    }
    return jsonify(response)


@app.route('/avionics/init-done', methods=['POST'])
def avionics_init_done():
    request_data = json.loads(request.data)
    print(request_data)
    status = request_data['status']
    if status == "Done":
        response = {
            "status": "Success"
        }
    else:
        response = {
            "status": "Failed"
        }
    return jsonify(response)


@app.route("/avionics/start-logging/status/<statusNum>")
def avionicsStartLogging(statusNum):
    global avionics_check
    # complete a task and check it
    statusNum = int(statusNum)
    avionics_check = statusNum
    print(avionics_check)
    templateData = {
        'propulsionPercentage': propulsionProgress,
        'airframePercentage': airframeProgress,
        'avionicsPercentage': avionicsProgress,
    }
    return render_template('index.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
