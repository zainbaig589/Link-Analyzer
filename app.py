import streamlit as st
from analyzer import get_analysis

st.set_page_config(page_title="AI Browser Security Assistant")

st.title("AI Browser Security Assistant")

url = st.text_input("Enter Website URL")

if st.button("Analyze"):

    if url:

        score, verdict, reasons = get_analysis(url)

        st.subheader(f"Safe: {score}/100")

        if score > 70:
            st.success(verdict)
        elif score > 40:
            st.warning(verdict)
        else:
            st.error(verdict)

        st.write("### Reasons:")

        for r in reasons:
            st.write("•", r)

    else:
        st.warning("Please enter a URL")