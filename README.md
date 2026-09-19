\# Mental Health in Tech Survey — EDA \& Dashboard



An exploratory data analysis of a 2014 survey on mental health attitudes and support in the tech workplace, with an interactive Streamlit app to explore the findings.



\## Overview



This project investigates how comfortable tech employees feel discussing mental health at work, how aware they are of available resources, and what factors most strongly predict whether someone seeks treatment — then translates the findings into practical recommendations for employers.



\## Tools \& Libraries



\- \*\*Python\*\* — Pandas, NumPy, Matplotlib, Seaborn, scikit-learn (LabelEncoder)

\- \*\*Streamlit\*\* — Interactive multi-page web app



\## Workflow



1\. \*\*Data Cleaning\*\* — Removed 8 rows with invalid Age values, standardized 40+ inconsistent Gender spellings into Male/Female/Other, handled missing values in `self\_employed` and `work\_interfere`, and dropped low-value columns (`state`, `comments`, raw `Timestamp`) after extracting a `Year` field.

2\. \*\*Exploratory Analysis\*\* — 15 visualizations covering demographics, treatment patterns, workplace policies, and awareness levels, plus a label-encoded correlation heatmap and a pair plot.

3\. \*\*Key Findings\*\* — Treatment-seeking is most strongly associated with having a family history of mental illness and working for an employer that actively provides and discusses mental health benefits. A recurring theme was uncertainty rather than absence — many respondents didn't know whether care options, anonymity protections, or leave policies existed at all.



\## Files



\- `mental\_health\_eda.ipynb` — Full EDA notebook with 15 charts and written insights

\- `survey.csv` — Original raw dataset

\- `cleaned\_survey.csv` — Cleaned dataset used for analysis and the app

\- `Home.py` + `pages/` — Multi-page Streamlit app

\- `requirements.txt` — Python dependencies



\## Running the App



```

pip install -r requirements.txt

streamlit run Home.py

```



\## Dashboard Pages



\- \*\*Demographics\*\* — Age, Gender, Top Countries

\- \*\*Treatment Overview\*\* — Treatment rates, family history, work interference

\- \*\*Workplace Setup\*\* — Company size, remote work, benefits

\- \*\*Awareness\*\* — Care options, wellness programs, anonymity

\- \*\*Deeper Patterns\*\* — Leave policy, correlation heatmap, pair plot



\---



\*\*Author:\*\* Abhinibesh Mal

\[LinkedIn](https://www.linkedin.com/in/abhinibeshmal/) · \[GitHub](https://github.com/abhinibeshmal)

