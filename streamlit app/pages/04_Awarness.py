import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Awareness")

st.divider()

df = pd.read_csv("cleaned_survey.csv")

# Chart 1 - Care Options Awareness
st.subheader("Awareness of Mental Health Care Options")
fig, ax = plt.subplots()
sns.countplot(data=df, x="care_options", ax=ax)
st.pyplot(fig)

st.divider()

# Chart 2 - Wellness Program vs Treatment
st.subheader("Wellness Program Discussion vs Treatment Sought")
fig, ax = plt.subplots()
sns.countplot(data=df, x="wellness_program", hue="treatment", ax=ax)
st.pyplot(fig)

st.divider()

# Chart 3 - Anonymity vs Treatment
st.subheader("Anonymity Protection vs Treatment Sought")
fig, ax = plt.subplots()
sns.countplot(data=df, x="anonymity", hue="treatment", ax=ax)
st.pyplot(fig)

st.divider()