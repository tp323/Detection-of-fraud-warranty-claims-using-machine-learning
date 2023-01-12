from flask import Flask, request, jsonify
import pickle
import traceback
import pandas as pd

# Your API definition
app = Flask(__name__)


@app.route('/', methods=['POST'])
def predict():
    if lr:
        try:
            request.headers = {"Content-Type": "application/json"}
            json_ = request.json
            print(json_)
            query = pd.get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns=model_columns, fill_value=0)
            prediction = list(lr.predict(query))
            return jsonify({'prediction': str(prediction)})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Train the model first')
        return 'No model here to use'


if __name__ == '__main__':
    file_name = "saved_model.plk"
    lr = pickle.load(open(file_name, "rb"))  # Load "model.plk"
    print('Model loaded')
    model_columns = pickle.load(open(file_name, "rb"))  # Load "model_columns.plk"
    print('Model columns loaded')
    app.run(debug=True)

