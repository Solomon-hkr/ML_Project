from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import os
import gdown
import joblib
import pickle

app = Flask(__name__)

# Google Drive file links
compressed_model_file_id = "1aTasO_fXRXqMbIM-NRV2MqedSwkW9h35"
features_file_id = "1bAglZ4Mbsu5G2wbzQOpUi2vXKg_6zpPE"

# Local paths
compressed_model_path = "web_integration/backend/model/compressed_model.pkl"
features_list_path = "web_integration/backend/model/features_list.pkl"

# Ensure directories exist
os.makedirs(os.path.dirname(compressed_model_path), exist_ok=True)
os.makedirs(os.path.dirname(features_list_path), exist_ok=True)

# Function to download files from Google Drive
def download_file(file_id, dest_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, dest_path, quiet=False)

# Download required files if not already present
if not os.path.exists(compressed_model_path):
    print("Downloading compressed_model.pkl...")
    download_file(compressed_model_file_id, compressed_model_path)

if not os.path.exists(features_list_path):
    print("Downloading features_list.pkl...")
    download_file(features_file_id, features_list_path)

# Lazy model loader to reduce memory usage
def load_model():
    if not hasattr(load_model, "cached_model"):
        with open(compressed_model_path, "rb") as f:
            load_model.cached_model = joblib.load(f)
    return load_model.cached_model

# Load the features list
with open(features_list_path, "rb") as f:
    feature_columns = pickle.load(f)

# Preprocessing function
def preprocess_inputs(inputs):
    # Only calculate features that are necessary for the model
    inputs["data_duration_interaction"] = inputs["data_compromised_GB"] * inputs["attack_duration_min"]
    inputs["severity_duration_interaction"] = inputs["attack_severity"] * inputs["attack_duration_min"]
    inputs["log_data_compromised_GB"] = np.log1p(inputs["data_compromised_GB"])
    inputs["log_response_time_min"] = np.log1p(inputs["response_time_min"])

    # Align feature names and order
    input_df = pd.DataFrame([inputs])[feature_columns]
    return input_df

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        features = preprocess_inputs(data)
        model = load_model()  # Load the model only when needed
        probabilities = model.predict_proba(features)[0]

        # threshold for "Success"
        threshold = 0.3
        outcome = "Success" if probabilities[1] > threshold else "Failure"
        return jsonify({"result": outcome, "probabilities": probabilities.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

