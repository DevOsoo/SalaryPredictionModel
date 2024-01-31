# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# def shorten_categories(categories, cutoff):
#     categorical_map = {}
#     for i in range(len(categories)):
#         if categories.values[i] >= cutoff:
#             categorical_map[categories.index[i]] = categories.index[i]
#         else:
#             categorical_map[categories.index[i]] = 'Other'
#     return categorical_map


# def clean_experience(x):
#     if x ==  'More than 50 years':
#         return 50
#     if x == 'Less than 1 year':
#         return 0.5
#     return float(x)


# def clean_education(x):
#     if 'Bachelor’s degree' in x:
#         return 'Bachelor’s degree'
#     if 'Master’s degree' in x:
#         return 'Master’s degree'
#     if 'Professional degree' in x or 'Other doctoral' in x:
#         return 'Post grad'
#     return 'Less than a Bachelors'


# @st.cache_resource
# def load_data():
#     df = pd.read_csv("survey_results_public.csv")
#     df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "CompTotal"]]
#     df = df[df["CompTotal"].notnull()]
#     df = df.dropna()
#     df = df[df["Employment"] == "Employed full-time"]
#     df = df.drop("Employment", axis=1)

#     country_map = shorten_categories(df.Country.value_counts(), 400)
#     df["Country"] = df["Country"].map(country_map)
#     df = df[df["CompTotal"] <= 250000]
#     df = df[df["CompTotal"] >= 10000]
#     df = df[df["Country"] != "Other"]

#     df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
#     df["EdLevel"] = df["EdLevel"].apply(clean_education)
#     df = df.rename({"CompTotal": "Salary"}, axis=1)
#     return df

# df = load_data()

# def show_explore_page():
#     st.title("Explore Software Engineer Salaries")

#     st.write(
#         """
#     ### Stack Overflow Developer Survey 2020
#     """
#     )
#     data = df["Country"].value_counts()

#     fig1, ax1 = plt.subplots()
#     ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
#     ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

#     st.write("""#### Number of Data from different countries""")
#     st.pyplot(fig1)
    
#     st.write(
#         """
#     #### Mean Salary Based On Country
#     """
#     )

#     data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
#     st.bar_chart(data)

#     st.write(
#         """
#     #### Mean Salary Based On Experience
#     """
#     )

#     data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
#     st.line_chart(data)


# import streamlit as st
# import pickle
# import numpy as np
# import pandas as pd
# import plotly.express as px

# def load_model():
#     with open('saved_steps.pkl', 'rb') as file:
#         loaded_data = pickle.load(file)
#     return loaded_data

# loaded_data = load_model()

# def show_explore_page():
#     st.title("Data explore")

#     # Load your dataset
#     data = pd.read_csv("survey_results_public.csv")

#     st.write("### Data Points by Country")
#     country_counts = data['Country'].value_counts()
#     fig = px.pie(country_counts, names=country_counts.index, values=country_counts.values)
#     st.plotly_chart(fig)
    
#     st.write("### Mean Salary by Country")
#     mean_salary_by_country = data.groupby('Country')['CompTotal'].mean().reset_index()
#     fig = px.bar(mean_salary_by_country, x='Country', y='CompTotal', title='Mean Salary by Country')
#     st.plotly_chart(fig)
    
#     st.write("### Mean Salary by Years of Experience")
#     mean_salary_by_experience = data.groupby('YearsCodePro')['CompTotal'].mean().reset_index()
#     fig = px.line(mean_salary_by_experience, x='YearsCodePro', y='CompTotal', title='Mean Salary by Years of Experience')
#     st.plotly_chart(fig)

# if __name__ == "__main__":
#     show_explore_page()


# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Load the dataset for visualization
# df = pd.read_csv('survey_results_public.csv')  # Make sure to provide the correct path to your dataset

# def clean_data(df):
#     # Filter out rows with missing Salary values
#     df = df.dropna(subset=['CompTotal'])

#     # Rename the 'CompTotal' column to 'Salary'
#     df = df.rename(columns={'CompTotal': 'Salary'})
    
#     return df

# # Clean the data
# df = clean_data(df)

# def show_explore_page():
#     st.title("Data Visualization")
#     st.write("This page displays visualizations based on the Stackoverflow survey data.")

#     # Pie Chart: Number of Data Points from Different Countries
#     country_counts = df['Country'].value_counts()
#     fig_pie = px.pie(country_counts, names=country_counts.index, values=country_counts.values, title='Data Points by Country')
#     st.plotly_chart(fig_pie)

#     # Bar Chart: Mean Salary by Country
#     mean_salary_by_country = df.groupby('Country')['Salary'].mean().reset_index()
#     fig_bar_country = px.bar(mean_salary_by_country, x='Country', y='Salary', title='Mean Salary by Country')
#     st.plotly_chart(fig_bar_country)

#     # Line Chart: Mean Salary by Experience
#     mean_salary_by_experience = df.groupby('YearsCodePro')['Salary'].mean().reset_index()
#     fig_line_experience = px.line(mean_salary_by_experience, x='YearsCodePro', y='Salary', title='Mean Salary by Experience')
#     st.plotly_chart(fig_line_experience)


import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset for visualization
df = pd.read_csv('survey_results_public.csv')  # Make sure to provide the correct path to your dataset

def clean_data(df):
    # Filter out rows with missing Salary values
    df = df.dropna(subset=['CompTotal'])

    # Rename the 'CompTotal' column to 'Salary'
    df = df.rename(columns={'CompTotal': 'Salary'})

    # Filter out rows with countries other than the ones specified
    countries = ["United States", "India", "United Kingdom", "Germany", "Canada", "Brazil", "France", "Spain", "Australia", "Netherlands", "Poland", "Italy", "Russian Federation", "Sweden"]
    df = df[df['Country'].isin(countries)]

    return df

# Clean the data
df = clean_data(df)

def show_explore_page():
    st.title("Data Visualization")
    st.write("This page displays visualizations based on the Stackoverflow survey data.")

    # Pie Chart: Number of Data Points from Different Countries
    country_counts = df['Country'].value_counts()
    fig_pie = px.pie(country_counts, names=country_counts.index, values=country_counts.values, title='Data Points by Country')
    st.plotly_chart(fig_pie)

    # Bar Chart: Mean Salary by Country
    mean_salary_by_country = df.groupby('Country')['Salary'].mean().reset_index()
    fig_bar_country = px.bar(mean_salary_by_country, x='Country', y='Salary', title='Mean Salary by Country')
    
    # Format the y-axis to show whole numbers
    fig_bar_country.update_yaxes(tickformat=',d')
    
    # Set the range of the y-axis to be between 10000 and 250000
    fig_bar_country.update_yaxes(range=[10000, 250000])
    
    st.plotly_chart(fig_bar_country)

    # Line Chart: Mean Salary by Experience
    mean_salary_by_experience = df.groupby('YearsCodePro')['Salary'].mean().reset_index()
    
    # Rename the 'YearsCodePro' column to 'Years of Experience'
    mean_salary_by_experience = mean_salary_by_experience.rename(columns={'YearsCodePro': 'Years of Experience'})
    
    fig_line_experience = px.line(mean_salary_by_experience, x='Years of Experience', y='Salary', title='Mean Salary by Experience')
    
    # Format the x-axis and y-axis to show whole numbers
    fig_line_experience.update_xaxes(tickformat=',d')
    fig_line_experience.update_yaxes(tickformat=',d')
    
    # Set the range of the y-axis to be between 10000 and 250000
    fig_line_experience.update_yaxes(range=[10000, 250000])
    
    st.plotly_chart(fig_line_experience)

