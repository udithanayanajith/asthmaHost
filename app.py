from flask import Flask, request, send_file

import asthmaStage
import barChart

app = Flask(__name__)


@app.route("/stage", methods=["GET"])
def stage():
    json_data = request.get_json()
    stageData = json_data['stage']
    num1 = stageData[0]
    num2 = stageData[1]
    num3 = stageData[2]
    num4 = stageData[3]
    result = asthmaStage.predictData(num1, num2, num3, num4)
    return {"stage": int(result)}


@app.route('/plot', methods=['GET'])
def plot():
    json_data = request.get_json()
    plot_data = json_data['plot'][:4]
    result = barChart.genarateBarChart(plot_data)
    return {"plotData": result}


if __name__ == "__main__":
    app.run(debug=True)
