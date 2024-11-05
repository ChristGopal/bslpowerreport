import streamlit as st
import pandas as pd
st.title("🎈 BSL Power Report apps")
genre = st.radio(
    "Select Your Meter Asset",
    ["D-Meter1", "***Drama***", "Documentary :movie_camera:"],
    index=None,
)

st.write("You selected:", genre)
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)")

