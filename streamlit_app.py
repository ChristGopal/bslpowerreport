import streamlit as st
import pandas as pd

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


