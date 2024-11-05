import streamlit as st
import pandas as pd
st.title("Power Report apps")
df = pd.read_csv('Entegris_PowerCons.csv')
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
column_names = df.columns.tolist()
st.write(column_names)

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

