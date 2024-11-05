import streamlit as st
import pandas as pd

df = pd.read_csv('Entegris_PowerCons.csv')
df[' Timestamp'] = pd.to_datetime(df[' Timestamp'])
df = df.set_index(' Timestamp')
weekly_sum = df[['DENT_MTR1','DENT_MTR2','DENT_MTR3','MDP01', 'MDP02', 'MDP03']].resample('M').sum()
st.title("🎈 BSL Power Report apps")
st.line_chart(weekly_sum)
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
