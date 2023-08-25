import streamlit as st
import joblib
import pickle  # Import pickle to save the model

try:
    # Load the pickled model
    model = joblib.load('random_forest_model.pkl')
except Exception as e:
    st.error(f"Error loading the model: {str(e)}")
# Streamlit app header
st.title('Churn Prediction App')

# Input form for user to enter customer data
age = st.number_input('Enter Age', min_value=0, max_value=100)
gender = st.selectbox('Select Gender', ['Male', 'Female'])
location = st.selectbox('Select Location', ['Los Angeles', 'New York', 'Miami', 'Chicago', 'Houston'])
subscription_length = st.number_input('Enter Subscription Length (Months)', min_value=1)
monthly_bill = st.number_input('Enter Monthly Bill', min_value=0.0)
total_usage_gb = st.number_input('Enter Total Usage (GB)', min_value=0)

# Make predictions when a user clicks the "Predict" button
if st.button('Predict Churn'):
    # Prepare the input data for prediction
    input_data = [[age, gender, location, subscription_length, monthly_bill, total_usage_gb]]

    # Make predictions using the loaded model
    prediction = model.predict(input_data)

    # Display the prediction
    if prediction[0] == 0:
        st.success('Prediction: Not Churned')
    else:
        st.error('Prediction: Churned')

