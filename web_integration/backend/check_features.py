import pickle

# Load the model and features list
model_path = "model/model.pkl"
features_list_path = "model/features_list.pkl"

try:
    with open(model_path, "rb") as model_file:
        model = pickle.load(model_file)
    print("Model loaded successfully!")

    with open(features_list_path, "rb") as features_file:
        features_list = pickle.load(features_file)
    print("Features used for the model:")
    for feature in features_list:
        print(f"- {feature}")
except Exception as e:
    print(f"Error loading model or features: {e}")
