import streamlit as st
import pandas as pd
import plotly.express as px
st.title("🎈 BSL Power Report apps")
meter_sel = st.radio(
    ["DENT-MTR1", "DENT-MTR2","DENT-MTR3","MDP-MTR1","MDP-MTR2","MDP-MTR2",],
    index=None,
)
period_sel = st.radio(
    ["D", "W","M","Y",],
    index=None,
)
df = pd.read_csv('Entegris_PowerCons.csv')
df[' Timestamp'] = pd.to_datetime(df[' Timestamp'])
df = df.set_index(' Timestamp')
weekly_sum = df[['DENT_MTR1','DENT_MTR2','DENT_MTR3','MDP01', 'MDP02', 'MDP03']].resample(period_sel).sum()
consumption_1 = DENT_MTR_DC.reset_index()  # Reset index
fig = px.bar (consumption_1, x='Timestamp', y=DENT_MTR_DC)
fig.show()

