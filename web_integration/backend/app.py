from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np
import os
import gdown

app = Flask(__name__)

# Google Drive file links
model_file_id = "1cHbILti_d1bzLa2k7cL5d2f2Th68AsnW"
features_file_id = "1bAglZ4Mbsu5G2wbzQOpUi2vXKg_6zpPE"
dataset_file_id = "1sDFH0q-zF-3NIK_7pqbfL6BBdYPz9iEE"

# Local paths
model_path = "web_integration/backend/model/model.pkl"
features_list_path = "web_integration/backend/model/features_list.pkl"
dataset_path = "web_integration/backend/dataset/cybersecurity_large_synthesized_data.csv"

# Ensure directories exist
os.makedirs(os.path.dirname(model_path), exist_ok=True)
os.makedirs(os.path.dirname(features_list_path), exist_ok=True)
os.makedirs(os.path.dirname(dataset_path), exist_ok=True)

# Function to download files from Google Drive
def download_file(file_id, dest_path):
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, dest_path, quiet=False)

# Download required files if not already present
if not os.path.exists(model_path):
    print("Downloading model.pkl...")
    download_file(model_file_id, model_path)

if not os.path.exists(features_list_path):
    print("Downloading features_list.pkl...")
    download_file(features_file_id, features_list_path)

if not os.path.exists(dataset_path):
    print("Downloading cybersecurity_large_synthesized_data.csv...")
    download_file(dataset_file_id, dataset_path)

# Load the trained model and features list
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(features_list_path, "rb") as f:
    feature_columns = pickle.load(f)

# Preprocessing function
def preprocess_inputs(inputs):
    inputs["data_duration_interaction"] = inputs["data_compromised_GB"] * inputs["attack_duration_min"]
    inputs["severity_duration_interaction"] = inputs["attack_severity"] * inputs["attack_duration_min"]
    inputs["response_security_ratio"] = inputs["response_time_min"] / (inputs["security_tools_used"] + 1)
    inputs["log_data_compromised_GB"] = np.log1p(inputs["data_compromised_GB"])
    inputs["log_response_time_min"] = np.log1p(inputs["response_time_min"])

    input_df = pd.DataFrame([inputs])
    input_df = input_df[feature_columns]  # Align feature names and order
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
        probabilities = model.predict_proba(features)[0]

        # threshold for "Success"
        threshold = 0.3
        outcome = "Success" if probabilities[1] > threshold else "Failure"
        return jsonify({"result": outcome, "probabilities": probabilities.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)



""" from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the trained model and features list
model_path = "web_integration/backend/model/model.pkl"
features_list_path = "web_integration/backend/model/features_list.pkl"

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(features_list_path, "rb") as f:
    feature_columns = pickle.load(f)

def preprocess_inputs(inputs):
    inputs["data_duration_interaction"] = inputs["data_compromised_GB"] * inputs["attack_duration_min"]
    inputs["severity_duration_interaction"] = inputs["attack_severity"] * inputs["attack_duration_min"]
    inputs["response_security_ratio"] = inputs["response_time_min"] / (inputs["security_tools_used"] + 1)
    inputs["log_data_compromised_GB"] = np.log1p(inputs["data_compromised_GB"])
    inputs["log_response_time_min"] = np.log1p(inputs["response_time_min"])

    input_df = pd.DataFrame([inputs])
    input_df = input_df[feature_columns]  # Align feature names and order
    return input_df


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        features = preprocess_inputs(data)
        probabilities = model.predict_proba(features)[0]

        # Adjust threshold for "Success"
        threshold = 0.4  # Adjust this value as needed
        outcome = "Success" if probabilities[1] > threshold else "Failure"
        return jsonify({"result": outcome, "probabilities": probabilities.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 400





if __name__ == "__main__":
    app.run(debug=True)



 """