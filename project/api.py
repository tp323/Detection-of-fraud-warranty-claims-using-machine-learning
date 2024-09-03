from flask import Flask, request, jsonify
import traceback
import pandas as pd
import pickle
from flask_cors import CORS

# API definition
app = Flask(__name__)

# Configure CORS to allow requests from any origin
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# The function should return None or end without a return statement.
@app.route('/', methods=['POST'])
def predict():
    if lr:
        try:
            json_ = request.json
            print(json_)
            df = pd.DataFrame.from_dict(json_, orient="index").T
            prediction = lr.predict(df)[0]
            print(prediction)

            return jsonify({'prediction': str(prediction)})
        except Exception:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Train the model first')
        return 'No model here to use'

# Remove `Access-Control-Allow-Private-Network` header after every request, if present
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow all origins
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')

    # Ensure the `Access-Control-Allow-Private-Network` header is not set
    if 'Access-Control-Allow-Private-Network' in response.headers:
        del response.headers['Access-Control-Allow-Private-Network']

    return response

if __name__ == '__main__':
    with open("model.pkl", "rb") as file:
        lr = pickle.load(file)
        print(lr)
    app.run(debug=True)
