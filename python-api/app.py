from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model
with open("../model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    input_data = [[
        data["Attendance"],
        data["Test_Marks"],
        data["Assignment_Marks"],
        data["Practical_Marks"]
    ]]

    prediction = model.predict(input_data)

    return jsonify({
        "predicted_marks": float(prediction[0][0])
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)