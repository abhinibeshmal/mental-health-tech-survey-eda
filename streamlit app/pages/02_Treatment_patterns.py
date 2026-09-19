import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Treatment Overview")

st.divider()

df = pd.read_csv("cleaned_survey.csv")

# Chart 1 - Treatment Distribution
st.subheader("Have Respondents Sought Treatment?")
fig, ax = plt.subplots()
sns.countplot(data=df, x="treatment", ax=ax)
st.pyplot(fig)

st.divider()

# Chart 2 - Family History vs Treatment
st.subheader("Family History vs Treatment")
fig, ax = plt.subplots()
sns.countplot(data=df, x="family_history", hue="treatment", ax=ax)
st.pyplot(fig)

st.divider()

# Chart 3 - Work Interference
st.subheader("Work Interference Levels")
fig, ax = plt.subplots()
order = df["work_interfere"].value_counts().index
sns.countplot(data=df, x="work_interfere", order=order, ax=ax)
st.pyplot(fig)

st.divider()