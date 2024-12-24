#------------------------------------------------
# Phase 1 - Milestone 2
# Name: Verren Monica
# Batch: RMT - 038
# Model Deployment - EDA Page
#------------------------------------------------

# Import Libraries
import streamlit as st
import pandas as pd
import seaborn as sns
from PIL import Image
import matplotlib.pyplot as plt

def run():
    """This function is the main entry point for running the webapps."""

    # Display image
    image = Image.open('banner.png')
    st.image(image)

    # Make header
    st.header('Loan Approval - Exploratory Data Analysis')
    
    # Add text
    st.write('by **Verren Monica**\n\n*Hacktiv8 - Full Time Data Science - Batch RMT-038 - Milestone Project*')
    st.write('')
    st.write('This page contains the Exploratory Data Analysis (EDA) of the loan approval dataset.\n\nLoan Status Dataset:')

    # Display DataFrame
    data = pd.read_csv('loandataset.csv')
    st.dataframe(data)
    st.write('Dataset source: [click here](https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data)')


    # Make Sub-Header
    st.subheader('Applicants Demographics Analysis')
    st.write('''
             This section analyzes the demographics of applicants, including age, gender, highest education level, 
             and home ownership status, to better understand their characteristics.
             ''')

    # Visualize age distribution
    st.write('#### Applicants Age Distribution')
    fig = plt.figure(figsize=(15,5))
    sns.histplot(data['person_age'], bins=50, kde=True)
    plt.title('Age Distribution')
    st.pyplot(fig)

    # Count statistic descriptive person_age column
    meanAge = data['person_age'].mean()
    medianAge = data['person_age'].median()
    modeAge = data['person_age'].mode()
    maxAge = data['person_age'].max()
    minAge =data['person_age'].min()
    skewAge = data['person_age'].skew()
    kurtosisAge = data['person_age'].kurtosis()
    
    # Display statistic descriptive result and the analysis 
    st.write(f"Mean Age: {meanAge:.2f}")
    st.write(f"Median Age: {medianAge:.2f}")
    st.write(f"Mode Age: {modeAge[0]:.2f}")
    st.write(f"Min Age: {minAge}")
    st.write(f"Max Age: {maxAge}")
    st.write(f"Skewness Age: {skewAge:.2f}")
    st.write(f"Kurtosis Age: {kurtosisAge:.2f}")
    st.write("""
            From the statistical analysis above, the following information is obtained:

            - The youngest applicant is 20 years old, and the oldest applicant is 144 years old.
            - The average age of applicants overall is approximately 27-28 years.
            - Many applicants are 23 years old, as indicated by the mode value.
            - The age data is skewed and extreme, as seen from the skewness value.
            - From the kurtosis value, it is known that the distribution shape is leptokurtic (having a sharper peak than a normal distribution) and there is a possibility of extreme values (outliers).
            - The age of 144 years, which is the maximum value, is almost certainly an outlier because it is nearly impossible for someone to be that old.
            """)

    # Visualize gender percentage
    st.write('#### Applicants Gender Percentage')
    gender = data.groupby('person_gender')['person_gender'].value_counts().reset_index()
    fig = plt.figure(figsize=(5,5))
    plt.pie(x=gender['count'], labels=gender['person_gender'], autopct='%1.2f%%')
    st.pyplot(fig)
    # Display gender percentage analysis
    st.write("""
            From the calculation of gender data and the visualization above, it is found that 55.2% of the applicants are male, and 44.8% are female. 
            The following is an analysis of the applicants' highest education levels.
            """)

    # Visualize highest education level
    st.write('#### Applicants Highest Education Level')
    education = data.groupby('person_education')['person_education'].value_counts().sort_values(ascending=False).reset_index()
    fig, ax = plt.subplots(figsize=(15,5)) 
    ax.bar(education['person_education'], education['count'])
    plt.title('Aplicant Highest Education Level')
    plt.xticks(rotation=0) 
    st.pyplot(fig)
    # Display highest education level analysis
    st.write("""
            From the analysis above, it is observed that the majority of applicants have a bachelor's degree as their highest education level, while the lowest number of applicants have a doctorate.
            """)


    # Visualize home ownership percentage
    st.write('#### Applicants Home Ownership')
    person_home_ownership = data.groupby('person_home_ownership')['person_home_ownership'].value_counts().reset_index()
    fig = plt.figure(figsize=(5,5))
    plt.pie(x=person_home_ownership['count'], labels=person_home_ownership['person_home_ownership'], autopct='%1.2f%%')
    st.pyplot(fig)    
    # Display home ownership analysis
    st.write("""
            From the visualization above, it is found that 52.10% of applicants have a home ownership status of rent, 41.09% mortgage, 6.56% own, and 0.26% other. 
            The other category likely refers to applicants who do not yet own a home, live with family, or do not have a permanent residence.\n
            """)

    # Make Sub-Header
    st.subheader('Applicants Average Income & Average Loan Amount Requested based on Age Groups')
    st.write('''
            This section provides an analysis of the average income and average loan amount requested by applicants across different age groups. 
            The age groups are categorized to better understand how income levels and loan requests vary by age, offering valuable insights into the financial behaviors of each group.
            The age groups are classified according to the WHO age classification as follows:

            - 15-24 years: Adolescents
            - 25-44 years: Adults
            - 45-59 years: Middle age
            - 60-74 years: Elderly
            - 75 years and above: Senior\n
            
            Source: [WHO Age Classification](https://www.ilmu.co.id/klasifikasi-usia-menurut-who-pdf)
            ''')
    # Loop and condition for age category
    ageCat = []
    for i in data['person_age']:
        if  15 <= i <= 24 :
            ageCat.append('Adolescents')
        elif 25 <= i <= 44:
            ageCat.append('Adults')
        elif 45 <= i <= 59:
            ageCat.append('Middle Age')
        elif 60 <= i <= 74:
            ageCat.append('Elderly')
        elif i >= 75 :
            ageCat.append('Senior')
    data['ageCategory'] = ageCat

    # Make radio button to show Average Income and Average Loan Amount 
    select = st.radio('Select Data to Visualize:', ('Average Income','Average Loan Amount Requested'))
    fig,ax = plt.subplots(figsize=(15,5))
    
    # Display visualization and analysis based on selected radio button
    if select == 'Average Income':
        incomeAvg = data.groupby('ageCategory')['person_income'].mean().sort_values(ascending=False).reset_index()
        ax.bar(incomeAvg['ageCategory'], incomeAvg['person_income'])
        plt.title('Aplicants Average Income by Age Category')
        plt.xticks(rotation=0) 
        st.pyplot(fig)
        st.write("""
                From the analysis above, it is found that customers in the Senior age group have the highest income, amounting to $1,617,362. 
                This may be because the applicants are retirees with high pensions or business owners with substantial passive income.
                """)
        empExp = data.groupby('ageCategory')['person_emp_exp'].mean().sort_values(ascending=False).reset_index()
        dataInf =pd.DataFrame(empExp)
        st.dataframe(dataInf)
        st.write("""
                From the mean calculations above, it is found that the Senior age group has the longest average work experience. 
                This suggests that applicants in this category are more likely to have higher incomes.
                """) 

    elif select == 'Average Loan Amount Requested':
        loanAvg = data.groupby('ageCategory')['loan_amnt'].mean().sort_values(ascending=False).reset_index()
        ax.bar(loanAvg['ageCategory'], loanAvg['loan_amnt'])
        plt.title('Aplicants Average Loan Amount Requested by Age Category')
        plt.xticks(rotation=0) 
        st.pyplot(fig)
        st.write("""
                The highest average loan amount is requested by applicants in the Elderly age category (60-74 years). 
                For other age categories, the average loan amount is relatively similar, ranging between 9,000 dollars and 10,000 dollars.
                 """)

    # Make Sub-Header
    st.subheader('Applicants Loan Purposes')
    st.write('''
            This section analyzes the most common loan purposes submitted by applicants to gain a better understanding of their primary needs.
            ''')
    
    # Visualize loan purposes and the analysis
    loanIntent = data.groupby('loan_intent')['loan_intent'].value_counts().sort_values(ascending=False).reset_index()
    fig,ax = plt.subplots(figsize=(15,5))
    ax.bar(loanIntent['loan_intent'], loanIntent['count'])
    plt.title('Aplicants Loan Purposes')
    plt.xticks(rotation=0) 
    st.pyplot(fig)    
    st.write("From the analysis above, it is found that the majority of loan purposes are for education (school) and medical (health) needs.")

    # Make Sub-Header
    st.subheader('Percentage Approved vs Rejected')
    st.write('''
            This section analyzes the total number of applicant statuses, both rejected and accepted, 
            from the dataset to provide an overview of data balance, which can aid in the modeling process.
            ''')
    
    # Visualize loan status and the analysis
    status = data.groupby('loan_status')['loan_status'].value_counts().reset_index()
    fig = plt.figure(figsize=(5,5))
    plt.pie(x=status['count'], labels=['Rejected', 'Accepted'], autopct='%1.2f%%')
    st.pyplot(fig)
    st.write('''
            From the entire dataset, 77.78% of the data corresponds to rejected loans, while 22.22% corresponds to accepted loans.
            Therefore, data balancing will be performed during the feature engineering process in model preparation to ensure the model learns from a more balanced dataset 
            (not overly focused on rejected data) and produces accurate predictions.
             ''')    

    # Make Sub-Header
    st.subheader('Numerical Columns Correlation')
    st.write('''
            This section analyzes the correlations between numerical columns to gain a better understanding of the relationships among the numerical variables.
            ''')
    
    # List numerical column
    cols = ['person_age','person_income','person_emp_exp', 'loan_amnt','loan_int_rate','loan_percent_income','cb_person_cred_hist_length','credit_score']
    # Count correlation value
    correlationMatrix = data[cols].corr()

    # Visualize correlation matrix and the analysis
    fig = plt.figure(figsize=(15,10))
    sns.heatmap(correlationMatrix, annot=True, cmap='coolwarm')
    plt.title('Numerical Columns Correlation')
    st.pyplot(fig)
    st.write("""
            From the visualization above, the following information is obtained:
            - The person_age column shows a strong positive correlation with person_emp_exp, meaning that as the applicant gets older, their work experience also tends to increase. \n\n
            - The person_age column is also strongly positively correlated with cb_person_cred_hist_len, meaning that older applicants tend to have had credit for a longer period. This suggests that older applicants are likely to have more credit experience and, consequently, may demonstrate better and more mature financial behavior, especially in managing credit.
            - The person_emp_exp column shows a strong positive correlation with cb_person_cred_hist_len, indicating that the longer the applicant's work experience, the longer they have had a credit history.
            - The loan_amnt column shows a strong positive correlation with loan_percent_income, meaning that the higher the loan amount requested, the higher the percentage of the loan amount relative to the applicant's income.
            """)


if __name__ =='__main__':
    run()