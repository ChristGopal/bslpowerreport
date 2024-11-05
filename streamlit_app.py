import streamlit as st
import pandas as pd
st.title("🎈 BSL Power Report apps")

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled")
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )
Meter_Selection = st.radio(
    "Select Your Meter Asset",
    ["DENT_MTR1", "DENT_MTR2","DENT_MTR3","MDP01","MDP02","MDP03",],
    index=None,
)
Period_Selection = st.radio(
    "Select Your Meter Asset",
    ["D", "W","M","Y",],
    index=None,
)

st.write("You selected:", Meter_Selection, Period_Selection )
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)")

