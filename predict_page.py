# import streamlit as st
# import pickle
# import numpy as np


# def load_model():
#     with open('saved_steps.pkl', 'rb') as file:
#         loaded_data = pickle.load(file)
#     return loaded_data
    
# loaded_data = load_model()

# regressor_loaded = loaded_data["model"]
# le_country = loaded_data["le_country"]
# le_education = loaded_data["le_education"]

# def show_predict_page():
#     st.title("Software Developer Salary Prediction")

#     st.write("""### We need some information to predict the salary""")


#     countries = (
#         "United States",
#         "India",
#         "United Kingdom",
#         "Germany",
#         "Canada",
#         "Brazil",
#         "France",
#         "Spain",
#         "Australia",
#         "Netherlands",
#         "Poland",
#         "Italy",
#         "Russian Federation",
#         "Sweden",
#     )

#     education = (
#         "Less than a Bachelors",
#         "Bachelor’s degree",
#         "Master’s degree",
#         "Post grad",
#     )

#     country = st.selectbox("Country", countries)
#     education = st.selectbox("Education Level", education)

#     expericence = st.slider("Years of Experience", 0, 50, 3)

#     ok = st.button("Calculate Salary")
#     if ok:
#         X = np.array([[country, education, expericence]])
#         X[:, 0] = le_country.transform(X[:,0])
#         X[:, 1] = le_education.transform(X[:,1])
#         X = X.astype(float)

        
#         salary = regressor_loaded.predict(X)
#         st.subheader(f"The estimated salary is ${salary[0]:.2f}")


import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        loaded_data = pickle.load(file)
    return loaded_data

loaded_data = load_model()
regressor_loaded = loaded_data["model"]
le_country = loaded_data["le_country"]
le_education = loaded_data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")
    st.write("""### Provide the following Information to predict the salary""")

    # Define the available options for countries and education levels
    countries = le_country.classes_
    education_levels = le_education.classes_

    # Create selection widgets for country and education level
    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education_levels)

    experience = st.slider("Years of Experience", 0, 50, 3)

    ok = st.button("Invoke the ML Model to Predict Salary")
    if ok:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:, 0])
        X[:, 1] = le_education.transform(X[:, 1])
        X = X.astype(float)

        salary = regressor_loaded.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")


