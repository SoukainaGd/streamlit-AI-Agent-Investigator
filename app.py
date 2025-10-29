import streamlit as st
import json
from crew import run_investigation

st.title("🕵️‍♀️ AI Agent Investigator by Soukaina")
company = st.text_input("Enter a company or organization to investigate:")
if st.button("Run Investigation"):
    with st.spinner("Investigating..."):
        result = run_investigation(company)
        st.success("Investigation complete!")

        st.json(result.raw if hasattr(result, "raw") else result)

        # Optionally save
        filename = f"{company}_investigation.json"
        with open(filename, "w") as f:
            json.dump(result.raw if hasattr(result, "raw") else result, f, indent=2)
        st.download_button("Download Results", data=open(filename).read(), file_name=filename)
