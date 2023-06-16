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
if st.button('Show me?'):  # Returns True if the user clicks the button
    st.write('HEre it is')
show_df = st.checkbox('Show DataFrame')  # Returns True if the user checks the box, False otherwise
if show_df:
    st.write(df)
st.dataframe(df)

st.write(df['visitor'].describe())

# Add Successful column
df['Successful'] = df['visitor'].apply(lambda x: 'Yes' if x >= 60 else 'No')

# Display DataFrame in Streamlit
st.dataframe(df)

# Filter DataFrame
success_df = df[df['Successful'] == 'Yes']

# Display filtered DataFrame in Streamlit
st.dataframe(success_df)
