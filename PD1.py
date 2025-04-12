from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict')
def predict():
    arg1 = float(request.args.get("arg1", "0"))
    arg2 = float(request.args.get("arg2", "0"))

    prediction = 1 if (arg1 + arg2) > 5.8 else 0

    response = {
        "prediction": prediction,
        "features": {
            "arg1": arg1,
            "arg2": arg2
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run()
