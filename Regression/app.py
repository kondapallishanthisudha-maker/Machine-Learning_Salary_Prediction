import streamlit as st
import pickle 
import numpy as np

# Load the trained model from the pickle file 
model = pickle.load(open(r"C:\Users\shant\OneDrive\Desktop\Machine Learning\Regression\linear_regression_model.pkl","rb"))

# Set the title of the streamlit app
st.title("Salary Prediction App")
# Descrpiton of the app
st.write("This app predicts the salary of an employee based on their years of experience using a simple liner regression model.")

# Add input widget for user to enter years of experience
years_of_experience = st.number_input("Enter years of experience:", min_value=0.0, max_value=50.0, step=0.1)

# when button is clicked, make prediction and display the result
if st.button("Predict Salary"):
    # Make prediction using the trained model
    experience_input = np.array([[years_of_experience]])
    prediction = model.predict(experience_input)

    # Display the result
    st.success(f"The predicted salary for {years_of_experience} years of experience is: ${prediction[0]:,.2f}")
    
    # Display information about the model
    st.write("The model was trained using a dataset of salaries and years of experience.buit model by shanthi")

