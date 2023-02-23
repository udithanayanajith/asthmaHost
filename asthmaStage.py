import warnings
import pickle

MODEL_FILE = "asthmaModel.pkl"

warnings.filterwarnings("ignore")

def predictData(num1, num2, num3, num4):
    with open(MODEL_FILE, "rb") as f:
        model = pickle.load(f)
        inputs = [num1, num2, num3, num4]
        prediction = model.predict([inputs])[0]
    return prediction
