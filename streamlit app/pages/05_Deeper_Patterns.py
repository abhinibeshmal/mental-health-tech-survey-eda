import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

st.title("Deeper Patterns")

st.divider()

df = pd.read_csv("cleaned_survey.csv")

# Chart 1 - Ease of Taking Leave
st.subheader("Ease of Taking Medical Leave for Mental Health")
order = ['Very easy', 'Somewhat easy', "Don't know", 'Somewhat difficult', 'Very difficult']
fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(data=df, x="leave", order=order, ax=ax)
plt.xticks(rotation=20)
st.pyplot(fig)

st.divider()

# Chart 2 - Correlation Heatmap
st.subheader("Correlation Heatmap (Label-Encoded Variables)")
df_encoded = df.copy()
le = LabelEncoder()
for col in df_encoded.select_dtypes(include="object").columns:
    df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))

fig, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(df_encoded.corr(), cmap="coolwarm", ax=ax)
st.pyplot(fig)

st.divider()

# Chart 3 - Pair Plot
st.subheader("Pair Plot: Age & Year by Treatment")
pair_fig = sns.pairplot(df, vars=["Age", "Year"], hue="treatment")
st.pyplot(pair_fig)

st.divider()