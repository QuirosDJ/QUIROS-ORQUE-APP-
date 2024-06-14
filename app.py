import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your data
# For demonstration, we will use the Iris dataset
@st.cache
def load_data():
    return sns.load_dataset('ParisHousing')

df = load_data()

# Title of the Streamlit app
st.title("Paris Housing Visualization")

# Display the data as a table
st.header("Data Table")
st.write(df)

# Pie Chart
st.header("Pie Chart of Species Distribution")
species_count = df['species'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(species_count, labels=species_count.index, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig1)

# Bar Chart
st.header("Bar Chart of Species Distribution")
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x='species', ax=ax2)
st.pyplot(fig2)

# Scatter Plot
st.header("Scatter Plot of Sepal Length vs. Sepal Width")
fig3, ax3 = plt.subplots()
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species', ax=ax3)
st.pyplot(fig3)

# Histogram
st.header("Histogram of Sepal Length")
fig4, ax4 = plt.subplots()
sns.histplot(df['sepal_length'], bins=20, ax=ax4)
st.pyplot(fig4)

# Summary Statistics
st.header("Summary Statistics")
st.write(df.describe())
