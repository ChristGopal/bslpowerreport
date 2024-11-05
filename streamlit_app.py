import streamlit as st
import pandas as pd

df = pd.read_csv('Entegris_PowerCons.csv')
st.title("🎈 My new BSL Power Report apps")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
