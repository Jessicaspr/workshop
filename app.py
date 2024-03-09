# import streamlit as st
# from src.inference import get_prediction

# #Initialise session state variable
# if 'input_features' not in st.session_state:
#     st.session_state['input_features'] = {}

# def app_sidebar():
#     st.sidebar.header('Loan Details')
#     emp_length_options = ['< 1 year','1 year','2 years','3 years','4 years','5 years',
#                           '6 years','7 years','8 years','9 years','10+ years']
#     emp_length = st.sidebar.selectbox("Employment Length", emp_length_options)
#     int_rate = st.sidebar.slider('Loan Interest Rate', 5, 40, 10, 1)
#     annual_inc = st.sidebar.text_input("Annual Income '000s", placeholder="in '000s")
#     fico_range_high = st.sidebar.slider('FICO Upper Boundary', 600, 800, 700, 50)
#     loan_amnt = st.sidebar.text_input('Loan Amount')
#     def get_input_features():
#         input_features = {'emp_length': emp_length,
#                           'int_rate': int_rate,
#                           'annual_inc': int(annual_inc)*1000,
#                           'fico_range_high': fico_range_high,
#                           'loan_amnt': int(loan_amnt)
#                          }
#         return input_features
#     sdb_col1, sdb_col2 = st.sidebar.columns(2)
#     with sdb_col1:
#         predict_button = st.sidebar.button("Assess", key="predict")
#     with sdb_col2:
#         reset_button = st.sidebar.button("Reset", key="clear")
#     if predict_button:
#         st.session_state['input_features'] = get_input_features()
#     if reset_button:
#         st.session_state['input_features'] = {}
#     return None

# def app_body():
#     title = '<p style="font-family:arial, sans-serif; color:Black; font-size: 40px;"><b> Welcome to DSSI Loan Assessment</b></p>'
#     st.markdown(title, unsafe_allow_html=True)
#     default_msg = '**System assessment says:** {}'
#     if st.session_state['input_features']:
#         assessment = get_prediction(emp_length=st.session_state['input_features']['emp_length'],
#                                     int_rate=st.session_state['input_features']['int_rate'],
#                                     annual_inc=st.session_state['input_features']['annual_inc'],
#                                     fico_range_high=st.session_state['input_features']['fico_range_high'],
#                                     loan_amnt=st.session_state['input_features']['loan_amnt'])
#         if assessment.lower() == 'yes':
#             st.success(default_msg.format('Approved'))
#         else:
#             st.warning(default_msg.format('Rejected'))
#     return None

# def main():
#     app_sidebar()
#     app_body()
#     return None

# if __name__ == "__main__":
#     main()

import streamlit as st
from src.inference import get_prediction

# Initialize session state variable
if 'input_features' not in st.session_state:
    st.session_state['input_features'] = {}

def app_sidebar():
    st.sidebar.header('User Details for Income Prediction')

    # Numeric features
    age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=30, step=1)
    fnlwgt = st.sidebar.number_input("FNLWGT", min_value=10000, max_value=1000000, value=100000, step=10000)
    education_num = st.sidebar.number_input("Education Number", min_value=1, max_value=20, value=10, step=1)
    capital_gain = st.sidebar.number_input("Capital Gain", min_value=0, max_value=100000, value=0, step=500)
    capital_loss = st.sidebar.number_input("Capital Loss", min_value=0, max_value=100000, value=0, step=500)
    hours_per_week = st.sidebar.number_input("Hours per Week", min_value=1, max_value=100, value=40, step=1)

    # Categorical features
    workclass_options = ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay', 'Never-worked']
    education_options = ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']
    marital_status_options = ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse']
    occupation_options = ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces']
    relationship_options = ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']
    race_options = ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']
    sex_options = ['Female', 'Male']
    native_country_options = ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands']

    workclass = st.sidebar.selectbox("Workclass", workclass_options)
    education = st.sidebar.selectbox("Education", education_options)
    marital_status = st.sidebar.selectbox("Marital Status", marital_status_options)
    occupation = st.sidebar.selectbox("Occupation", occupation_options)
    relationship = st.sidebar.selectbox("Relationship", relationship_options)
    race = st.sidebar.selectbox("Race", race_options)
    sex = st.sidebar.selectbox("Sex", sex_options)
    native_country = st.sidebar.selectbox("Native Country", native_country_options, index=native_country_options.index('United-States'))

    def get_input_features():
        input_features = {
            'age': age,
            'workclass': workclass,
            'fnlwgt': fnlwgt,
            'education': education,
            'education_num': education_num,
            'marital_status': marital_status,
            'occupation': occupation,
            'relationship': relationship,
            'race': race,
            'sex': sex,
            'capital_gain': capital_gain,
            'capital_loss': capital_loss,
            'hours_per_week': hours_per_week,
            'native_country': native_country
        }
        return input_features

    sdb_col1, sdb_col2 = st.sidebar.columns(2)
    with sdb_col1:
        predict_button = st.sidebar.button("Predict", key="predict")
    with sdb_col2:
        reset_button = st.sidebar.button("Reset", key="clear")
    
    if predict_button:
        st.session_state['input_features'] = get_input_features()
    if reset_button:
        st.session_state['input_features'] = {}

def app_body():
    title = '<p style="font-family:arial, sans-serif; color:Black; font-size: 40px;"><b>Welcome to Income Prediction App</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    default_msg = '**Prediction:** Your income is likely {}'
    
    if st.session_state['input_features']:
        assessment = get_prediction(**st.session_state['input_features'])
        if assessment.lower() == '>50k':
            st.success(default_msg.format('above 50K'))
        else:
            st.warning(default_msg.format('below or equal to 50K'))

def main():
    app_sidebar()
    app_body()

if __name__ == "__main__":
    main()
