import streamlit as st
import requests
from pathlib import Path

st.title("Text Clustering Demo")

if st.button("Run Model", type="primary"):
    with st.spinner("Clustering wordt uitgevoerd..."):
        try:
            response = requests.post("http://model:8000/run")

            if response.status_code == 200:
                st.success("Clustering voltooid!")
                st.image("img/clustering.png", caption="Clustering resultaat")
            else:
                st.error(f"Backend error {response.status_code}: {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"Kan backend niet bereiken: {e}")


st.info("Klik op 'Run Model' om de clustering visualisatie te genereren")