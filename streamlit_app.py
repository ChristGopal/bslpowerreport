import streamlit as st
import pandas as pd
st.title("Electrical Power Consumption Reports")
#st.image("substation.gif")
df = pd.read_csv('Entegris_PowerCons.csv')
timestamp_column_name = ' Timestamp'
df['Timestamp'] = pd.to_datetime(df[timestamp_column_name])
df.set_index('Timestamp', inplace=True)
column_names = df.columns.tolist()
col1, col2 = st.columns(2)

# Using "with" notation
with st.sidebar:
   st.logo("logo123.png")
   Meter_Selection = st.radio(
        "Select Your Meter Asset",
        [column_names[1],column_names[2],column_names[3],
         column_names[4],column_names[5],column_names[6]],
        index=1,
    )
  
with st.sidebar:
    Period_Selection = st.radio(
        "Select Your Meter Period",
        ["D", "W","MS","Q","Y",],
        index=1,
    )


cons1 = df[Meter_Selection].resample(Period_Selection).agg(['sum', 'min', 'max'])
max_consumption = cons1.max() 
max_consumption_date = cons1[cons1 == max_consumption].index[0]  
min_consumption = cons1.min() 
min_consumption_date = cons1[cons1 == min_consumption].index[0]  
st.metric(label="Max Of The", value=max_consumption, delta=max_consumption_date)
st.bar_chart(cons1)
st.table(cons1)


st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)")

