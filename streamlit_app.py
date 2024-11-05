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
   Meter_Selection = st.radio(
        "Select Your Meter Asset",
        [column_names[1],column_names[2],column_names[3],
         column_names[4],column_names[5],column_names[6]],
        index=None,
    )
  
with col2:
    Period_Selection = st.radio(
        "Select Your Meter Period",
        ["D", "W","M","Y",],
        index=None,
    )
st.write("You selected:", Meter_Selection, Period_Selection )
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)")

