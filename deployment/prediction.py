#------------------------------------------------
# Phase 1 - Milestone 2
# Name: Verren Monica
# Batch: RMT - 038
# Model Deployment - Prediction Page
#------------------------------------------------

# Import Libraries
import streamlit as st
import pickle
import pandas as pd
from PIL import Image

# Model Loading
with open('bestModel.pkl', 'rb') as modelFile:
  bestModel = pickle.load(modelFile)

def run():
    """This function is the main entry point for running the webapps."""

    # Diplay Image
    image = Image.open('banner.png')
    st.image(image)

    # Display Title
    st.title('Loan Approval Forecast Form')
    st.write("Kindly fill in the form to receive applicant's prediction.")

    # Create form for user input 
    with st.form(key='formLoanApproval'):

        # Applicant's personal information section
        st.write("**Applicant's Personal Information**")
        # Input age
        age = st.number_input('Age', min_value=20, max_value=150, value=20, step=1, 
                            help="Provide the applicant's age. Valid range: 20 to 150.")
        # Select gender
        gender = st.selectbox('Gender', ('male','female'), index=0, 
                            help="Select the applicant's gender: male or female.")
        # Select highest education level
        education = st.selectbox('Highest Education Level', ('High School', 'Associate', 'Bachelor','Master','Doctorate'), index=0, 
                            help="Select the applicant's highest education level, from High School to Doctorate.")
        # Input annual income
        income = st.number_input('Annual Income in USD (USD Dollar)',min_value=0, max_value=1000000000, value=0, 
                            help="Input applicant's annual income.")
        # Input years of employee experience
        empExp = st.number_input('Years of Employee Experience', min_value=0, max_value=200, value=0, step=1,
                            help="Enter the number of years the applicant has been employed.")
        # Select home ownership status
        homeOwn = st.selectbox('Home Ownership Status', ('MORTGAGE','OWN', 'RENT','OTHER'), index=0, 
                            help="Select the applicant's home ownership status.")
        
        st.markdown('---')
        
        # Applicant's loan details section
        st.write("**Applicant's Loan Details**")
        # Input loan amount requested
        loanAmount = st.number_input('Loan Amount Requested in USD (USD Dollar)', min_value=0, max_value=10000000000, value=0, 
                            help="Input applicant's amount of loan requested.")
        # Select loan intention
        intent = st.selectbox('Loan Intention', ('DEBTCONSOLIDATION','EDUCATION','HOME IMPROVEMENT','MEDICAL','PERSONAL','VENTURE'), 
                            help="Select applicant's loan intention.")
        # Input interest rate
        intRate = st.number_input('Loan Interest Rate Requested (%)',min_value=0.0, value=0.0, step=0.01, 
                            help="Input applicant's loan interest rate requested.")
        # Input loan percentage of income
        loanPctIncome = st.number_input('Loan Percentage of Income (enter as decimal, e.g., 0.20 for 20%)',min_value=0.0, max_value=1.0, value=0.0, step=0.01, 
                            help="Input applicant's loan amount as percentage of annual income (enter as decimal, e.g., 0.20 for 20%).")
        # Input credit history length
        creditHistLen = st.number_input('Length of Credit History in Years', min_value=0, max_value=200, value=0, step=1,
                            help="Enter the length of credit history in years.")
        # Input credit score
        creditScore = st.number_input('Credit Score',min_value=300, max_value=850, 
                            help="Input applicant's credit score. Valid range: 300 to 850.")
        # Select previous default 
        prevDefault = st.selectbox('Previous Defaults Loan on File',('Yes','No'),
                            help="Indicates whether the applicant has any previous loan defaults in their financial record.")
        
        # Predict button
        submitted = st.form_submit_button('Predict')

    # Display applicant's data summary
    st.write("## Applicant's Data Summary")
    # Organize applicant's data to a dictionary
    dataInf = {
            'age': age,
            'gender': gender,
            'education': education,
            'income': income,
            'empExp':empExp,
            'homeOwnership':homeOwn,
            'loanAmount':loanAmount,
            'loanIntent':intent,
            'intRate':intRate,
            'loanPctIncome':loanPctIncome,
            'creditHistLen':creditHistLen,
            'creditScore': creditScore,
            'prevDefault': prevDefault
            }
    # Convert to dataframe
    dataInf =pd.DataFrame([dataInf])
    # Display applicants data 
    st.dataframe(dataInf)

    # Display loan status prediction result
    st.write("### Applicant's Loan Status:")
    if submitted:
        # Predict and display result based on input data
        pred = bestModel.predict(dataInf)
        if pred == 0:
            st.write("## Rejected")
        elif pred == 1:
            st.write("## Approved")
            

if __name__ =='__main__':
    run()  