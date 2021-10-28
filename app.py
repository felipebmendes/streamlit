import streamlit as st
from pycarol import Carol, Apps, Storage

carol = Carol()
storage =  Storage(carol)
_settings = Apps(carol).get_settings()

# Add title on the page
st.title("Streamlit sample")

if _settings:
    st.write(f"Settings:")
    for key, value in _settings.items():
        st.write(f"{key} -> {value}")
else:
    st.write(f"App without settings.")

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)