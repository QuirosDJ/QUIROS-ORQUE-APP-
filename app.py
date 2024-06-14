import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your custom data
@st.cache_data
def load_data():
    return pd.read_csv('ParisHousing.csv')

df = load_data()

# Title of the Streamlit app
st.title("Paris Housing Visualization")

# Display the data as a table
st.header("Data Table")
st.write(df)

# Pie Chart
st.header("Pie Chart of a Selected Column")
# Replace 'column_name' with the appropriate column from your dataset
column_name = 'your_column_name'
if column_name in df.columns:
    column_count = df[column_name].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(column_count, labels=column_count.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)
else:
    st.write(f"Column '{column_name}' not found in the dataset.")

# Bar Chart
st.header("Bar Chart of a Selected Column")
# Replace 'column_name' with the appropriate column from your dataset
if column_name in df.columns:
    fig2, ax2 = plt.subplots()
    sns.countplot(data=df, x=column_name, ax=ax2)
    st.pyplot(fig2)
else:
    st.write(f"Column '{column_name}' not found in the dataset.")

# Scatter Plot
st.header("Scatter Plot of Two Selected Columns")
# Replace 'x_column' and 'y_column' with appropriate columns from your dataset
x_column = 'your_x_column'
y_column = 'your_y_column'
if x_column in df.columns and y_column in df.columns:
    fig3, ax3 = plt.subplots()
    sns.scatterplot(data=df, x=x_column, y=y_column, hue=column_name, ax=ax3)
    st.pyplot(fig3)
else:
    st.write(f"Columns '{x_column}' or '{y_column}' not found in the dataset.")

# Histogram
st.header("Histogram of a Selected Column")
# Replace 'column_name' with the appropriate column from your dataset
if column_name in df.columns:
    fig4, ax4 = plt.subplots()
    sns.histplot(df[column_name], bins=20, ax=ax4)
    st.pyplot(fig4)
else:
    st.write(f"Column '{column_name}' not found in the dataset.")

# Summary Statistics
st.header("Summary Statistics")
st.write(df.describe())
