import streamlit as st
st.title('My WebApp')  # Sets the title of your page
st.header('Data Visualization Section')  # Sets a header for a section
st.subheader('Subsection: Analysis')  # Sets a subheader for a subsection
st.text('This section focuses on data preprocessing.')
st.markdown('**Data**')
import pandas as pd

data = {
    'A': [12, 20, 15, 92, 88, 120, 160, 100, 44, 59, 87, 18],
    'B': ['Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
}
df = pd.DataFrame(data)

st.write(df)
visitor = st.slider('Your visitors', min_value=0, max_value=200)  # Returns the value selected by the user

from sklearn import datasets

# Load the iris dataset
iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Display the DataFrame in Streamlit
show_df = st.checkbox('Show DataFrame')  # Returns True if the user checks the box, False otherwise
if show_df:
    st.dataframe(df)

if st.button('Show me?'):  # Returns True if the user clicks the button
    st.write('Here it is')# Show general information about the dataset
    st.text(df.info())
    st.write(df.describe())


import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import streamlit as st

# Load the iris dataset
iris = datasets.load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Display the DataFrame in Streamlit
st.dataframe(df)

# Show general information about the dataset
st.text(df.info())

# Show statistical information about the dataset
st.write(df.describe())

# Select a feature to display histogram
feature = st.selectbox('Select a feature', df.columns)

# Plot histogram
fig, ax = plt.subplots()
ax.hist(df[feature], bins=20)

# Set the title and labels
ax.set_title(f'Histogram of {feature}')
ax.set_xlabel(feature)
ax.set_ylabel('Frequency')

# Display the plot
st.pyplot(fig)
