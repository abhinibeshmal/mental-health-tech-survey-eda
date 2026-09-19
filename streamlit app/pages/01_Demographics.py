import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Demographics")

st.divider()

df = pd.read_csv("cleaned_survey.csv")

# Chart 1 - Age
st.subheader("Age Distribution")
fig, ax = plt.subplots()
sns.histplot(df["Age"], bins=30, kde=True, ax=ax)
st.pyplot(fig)

st.divider()

# Chart 2 - Gender
st.subheader("Gender Distribution")
fig, ax = plt.subplots()
sns.countplot(data=df, x="Gender", ax=ax)
st.pyplot(fig)

st.divider()

# Chart 3 - Top 10 Countries
st.subheader("Top 10 Countries by Respondent Count")
top_countries = df["Country"].value_counts().head(10)
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=top_countries.values, y=top_countries.index, ax=ax)
st.pyplot(fig)

st.divider()