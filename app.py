import streamlit as st
from risk_engine import calculate_risk

st.title("AI Browser Security Assistant")

url = st.text_input("Enter Website URL")

if st.button("Analyze"):

    score, reasons = calculate_risk(url)

    st.subheader(f"Risk Score: {score}/100")

    if score > 70:
        st.error("High Risk Website")
    elif score > 40:
        st.warning("Medium Risk Website")
    else:
        st.success("Website Looks Safe")

    st.write("Reasons:")
    for r in reasons:
        st.write("- ", r)