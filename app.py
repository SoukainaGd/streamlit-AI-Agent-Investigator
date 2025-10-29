import streamlit as st
import json
import re
from crew import run_investigation

st.title("🕵️‍♀️ AI Agent Investigator by Soukaina")

company = st.text_input("Enter a company or organization to investigate:")

if st.button("Run Investigation") and company:
    with st.spinner("Investigating..."):
        result = run_investigation(company)
        st.success("Investigation complete!")

        # --- Extract the raw response safely ---
        data = result.raw if hasattr(result, "raw") else result

        # --- Handle case where LLM returns Markdown JSON ---
        if isinstance(data, str):
            cleaned = data.strip()

            # Remove Markdown code fences like ```json or ```
            cleaned = re.sub(r"^```[a-zA-Z]*", "", cleaned)
            cleaned = re.sub(r"```$", "", cleaned)
            cleaned = cleaned.strip()

            # Try parsing JSON
            try:
                parsed = json.loads(cleaned)
                st.json(parsed)
            except json.JSONDecodeError as e:
                st.error(f"⚠️ JSON Parse Error: {e}")
                st.write("Raw model output:")
                st.text(cleaned)
        else:
            st.json(data)

        # --- Optionally allow saving ---
        filename = f"{company}_investigation.json"
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=2)
            st.download_button("📥 Download Results", data=open(filename).read(), file_name=filename)
        except Exception as e:
            st.error(f"Error saving file: {e}")
