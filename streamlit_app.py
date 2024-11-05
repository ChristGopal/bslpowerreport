import streamlit as st
import pandas as pd
st.title("Power Report apps")
df = pd.read_csv('Entegris_PowerCons.csv')
timestamp_column_name = ' Timestamp'
df['Timestamp'] = pd.to_datetime(df[timestamp_column_name])
df.set_index('Timestamp', inplace=True)

column_names = df.columns.tolist()
for i, column_name in enumerate(column_names):
    st.write(f"Index: {i}, Column Name: {column_name}")
    st.write(f"Index: {i}")

col1, col2 = st.columns(2)

with col1:
    st.checkbox("DENT_MTR1")
    st.checkbox("DENT_MTR2")
    st.checkbox("DENT_MTR3")
    st.checkbox("MDP01")
    st.checkbox("MDP02")
    st.checkbox("MDP03")
  
with col2:
    Period_Selection = st.radio(
        "Select Your Meter Asset",
        ["D", "W","M","Y",],
        index=None,
    )

st.write("You selected:", Period_Selection )
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)")

