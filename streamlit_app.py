import streamlit as st
import pandas as pd
st.title("Electrical Power Consumption Reports")
st.image("substation.gif")
df = pd.read_csv('Entegris_PowerCons.csv')
timestamp_column_name = ' Timestamp'
df['Timestamp'] = pd.to_datetime(df[timestamp_column_name])
df.set_index('Timestamp', inplace=True)
column_names = df.columns.tolist()
col1, col2 = st.columns(2)

# Using "with" notation
with st.sidebar:
   Meter_Selection = st.radio(
        "Select Your Meter Asset",
        [column_names[1],column_names[2],column_names[3],
         column_names[4],column_names[5],column_names[6]],
        index=0,
    )
 
with st.sidebar:
    Period_Selection = st.radio(
        "Select Your Meter Period",
        ["D", "W","MS","Q","Y",],
        index=0,
    )
cons1 = df[Meter_Selection].resample(Period_Selection).agg(['sum', 'min', 'max'])
st.bar_chart(cons1)
st.table(cons1)


st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)")

