from flask import Flask, jsonify, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/prediction")
def show_prediction():
    # Add code here to retrieve the prediction results
    # You can pass the prediction results as variables to the template
    prediction = "Sample Prediction"  # Replace with actual prediction
    return render_template('prediction.html', prediction=prediction)

@app.route("/predict", methods=["POST"])
def predict():
    api_key = 'sk-8f61dd0d176bda0fb8316e47e42e72e0'
    headers = {
        'Authorization': 'Bearer ' + api_key,
        'Content-Type': 'application/json'
    }

    # Prepare the request payload
    payload = {
        "specification_hash": "e7cde6129663dcd2ba4d4e4389858a1a064b527b14b842961b83ff0d00459b44",
        "config": {
            "MODEL": {
                "provider_id": "openai",
                "model_id": "gpt-3.5-turbo-0301",
                "use_cache": True
            },
            "DATASOURCE": {
                "data_sources": [
                    {
                        "workspace_id": "14e72d2aff",
                        "data_source_id": "copy"
                    }
                ],
                "top_k": 8,
                "filter": {
                    "tags": None,
                    "timestamp": None
                },
                "use_cache": False
            }
        },
        "blocking": True,
        "inputs": [
            {
                "business": "outreach"
            }
        ]
    }

    # Make the request to the external API
    response = requests.post('https://dust.tt/api/v1/w/14e72d2aff/apps/0947e95c90/runs', json=payload, headers=headers)
    

    # Extract the prediction value from the response
    prediction_data = response.json()
    print(prediction_data)  # Print the response data for debugging

    # Replace "prediction" with the actual key holding the prediction in the response
    prediction = prediction_data.get("sk-8f61dd0d176bda0fb8316e47e42e72e0", "Sample Prediction")

    # Redirect to the prediction page
    return redirect(url_for('show_prediction', prediction=prediction))

if __name__ == '__main__':
    app.run(port=5000)
