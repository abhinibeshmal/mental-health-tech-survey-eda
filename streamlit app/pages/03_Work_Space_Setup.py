import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Workplace Setup")

st.divider()

df = pd.read_csv("cleaned_survey.csv")

# Chart 1 - Company Size
st.subheader("Company Size of Respondents")
order = ['1-5', '6-25', '26-100', '100-500', '500-1000', 'More than 1000']
fig, ax = plt.subplots(figsize=(9, 5))
sns.countplot(data=df, x="no_employees", order=order, ax=ax)
plt.xticks(rotation=30)
st.pyplot(fig)

st.divider()

# Chart 2 - Remote Work vs Treatment
st.subheader("Remote Work vs Treatment Sought")
fig, ax = plt.subplots()
sns.countplot(data=df, x="remote_work", hue="treatment", ax=ax)
st.pyplot(fig)

st.divider()

# Chart 3 - Benefits vs Treatment
st.subheader("Employer Benefits vs Treatment Sought")
fig, ax = plt.subplots()
sns.countplot(data=df, x="benefits", hue="treatment", ax=ax)
st.pyplot(fig)

st.divider()