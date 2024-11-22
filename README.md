

# ML_Project: Cybersecurity Attack Outcome Prediction

## Overview
This project predicts the outcome of a cybersecurity attack (Success or Failure) using a machine learning model. The web integration allows users to input attack details through a user-friendly interface and get predictions based on trained machine learning models.

The deployed application can be accessed here: [ML_Project: Cybersecurity Attack Outcome Prediction](https://ml-project-o9y8.onrender.com)

---

## Features
- **Machine Learning Training:** The `ML_Project_2.ipynb` file trains multiple models (Random Forest, Gradient Boosting, XGBoost, and Decision Tree) and selects the best-performing model based on accuracy and F1-score.
- **Compressed Model Deployment:** The best model is compressed using Joblib to minimize file size and optimize deployment.
- **Web Integration:** A Flask-based web application allows users to input features and get predictions.
- **Error Handling:** Integrated error handling to manage invalid inputs and unexpected scenarios gracefully.
- **User-Friendly Interface:** Frontend interface built using HTML, CSS, and JavaScript for seamless user interaction.
- **Optimized Deployment:** Deployment size and runtime are optimized for the Render free tier by compressing files and efficiently handling resources.

---

## Technologies Used
- **Machine Learning:**
  - Python (Pandas, Scikit-learn, XGBoost)
- **Web Integration:**
  - Flask (Python)
  - HTML, CSS, JavaScript
- **Deployment:**
  - Render (Web hosting platform)
  - GitHub (Version control and repository hosting)
- **Utilities:**
  - Gdown for file download from Google Drive (with alternative fallback solutions implemented)
  - Joblib for model compression

---

## How It Works
1. **Data Preprocessing:**
   - Data is preprocessed in the `ML_Project_2.ipynb` notebook, where irrelevant columns are removed, and categorical variables are encoded.
   - Interaction features and scaled numeric features are created to improve the performance of machine learning models.

2. **Model Training:**
   - The project trains multiple machine learning models (Gradient Boosting, Random Forest, XGBoost, and Decision Tree).
   - The best-performing model is selected and compressed using Joblib for optimized deployment.

3. **Web Application:**
   - A Flask-based backend serves the machine learning model and processes user inputs.
   - The application accepts input features and returns a prediction with probabilities for "Success" and "Failure."

4. **Deployment:**
   - The application is deployed on Render and optimized to fit the free-tier resource constraints.

---

## Live Application
Access the live application here: [ML_Project on Render](https://ml-project-o9y8.onrender.com)

---

## Directory Structure
```
ML_Project/
├── model_training/
│   ├── ML_Project_2.ipynb  # Jupyter notebook for data preprocessing and model training
│   ├── cybersecurity_large_synthesized_data.csv  # Input dataset
├── web_integration/
│   ├── backend/
│   │   ├── app.py  # Flask application
│   │   ├── model/
│   │   │   ├── compressed_model.pkl  # Compressed trained model
│   │   │   ├── features_list.pkl  # List of feature columns
│   │   ├── dataset/
│   │   │   ├── cybersecurity_large_synthesized_data.csv  # Input dataset for testing
│   ├── static/  # Frontend assets
│   │   ├── script.js
│   │   ├── style.css
│   ├── templates/
│       ├── index.html  # Web interface for input and prediction
├── requirements.txt  # Dependencies
├── README.md  # Project documentation
```

---

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/Solomon-hkr/ML_Project.git
   cd ML_Project
   ```

2. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application locally:
   ```
   python web_integration/backend/app.py
   ```

4. Access the application locally at `http://127.0.0.1:5000`.

---

## Updates and Enhancements
- Compressed the best-performing model (`compressed_model.pkl`) using Joblib to reduce deployment size.
- Implemented efficient file handling to ensure compatibility with Render's free-tier constraints.
- Integrated error handling for improved user experience during input validation and processing.
- Deployment link added to README for quick access.

