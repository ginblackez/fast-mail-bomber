import streamlit as st
import subprocess

def start_bombing(recipient_email):
    """Runs the PHP script with the email parameter."""
    result = subprocess.run(
        ["php", "index.php", "start-bombing", recipient_email], 
        capture_output=True, text=True
    )
    st.text(result.stdout)
    if result.stderr:
        st.error(result.stderr)

# Streamlit UI
st.title("Fast Mail Bomber - Streamlit Version")

recipient_email = st.text_input("Enter Recipient Email:")

if st.button("Start Bombing"):
    if recipient_email:
        start_bombing(recipient_email)
    else:
        st.error("Please enter a recipient email.")
