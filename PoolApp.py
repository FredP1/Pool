import streamlit as st
import pandas as pd
import numpy as np

st.title('PO Post Raiders Pool Results')


@st.cache_data
def load_data(nrows, DATE_COLUMN, DATA_URL):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN],infer_datetime_format=True)
    return data

# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000, 'date',"./PoolTeamResults.csv")
# # Notify the reader that the data was successfully loaded.
# data_load_state.text("Data Loaded.")

st.subheader('Points across the season')

# st.subheader('Raw data')
# st.write(data)

# hist_values = np.histogram(
#     data[DATE_COLUMN].dt.day, bins=18, range=(0,18))[0]

hist_value = np.cumsum(
    data
)

st.line_chart(hist_value, y='points')


@st.cache_data
def load_data2(nrows, DATA_URL):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data
# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data2 = load_data2(10000,"./PoolTeamPoints.csv")
# # Notify the reader that the data was successfully loaded.
# data_load_state.text("Data Loaded.")

data2['lost'] = (data2['played'] - data2['won'])

st.subheader('Points Per Player')
st.bar_chart(data2, x='player', y='points')

st.subheader('Win/Lost')
st.bar_chart(data2, x='player', y=['won','lost'])