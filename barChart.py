import pickle
import numpy as np

MODEL_FILE = "asthmaPlotModel.pkl"
def genarateBarChart(plotData):

    print(plotData, "Data inside the barchart script")
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)
        y_pred = model.predict(plotData)
        print(y_pred)
        prediction_array = np.array(y_pred)
        prediction_list = prediction_array.tolist()
        print(prediction_list, "pred list")

    return prediction_list
