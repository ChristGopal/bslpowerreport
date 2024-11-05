import streamlit as st
import pandas as pd
st.title("Power Report apps")
df = pd.read_csv('Entegris_PowerCons.csv')
timestamp_column_name = ' Timestamp'
df['Timestamp'] = pd.to_datetime(df[timestamp_column_name])
df.set_index('Timestamp', inplace=True)
column_names = df.columns.tolist()
 
col1, col2 = st.columns(2)

with col1:
    st.checkbox(column_names[1])
    st.checkbox(column_names[2])
    st.checkbox(column_names[3])
    st.checkbox(column_names[4])
    st.checkbox(column_names[5])
    st.checkbox(column_names[6])
  
with col2:
    Period_Selection = st.radio(
        "Select Your Meter Asset",
        ["D", "W","M","Y",],
        index=None,
    )

st.write("You selected:", Period_Selection )
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)")

