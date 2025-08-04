import streamlit as st
from email_sender import send_email
from find_summary import get_summary
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

sender_email = os.getenv("sender_email")
sender_password = os.getenv("sender_password")

# Streamlit app title
st.title("Article Summarizer and Emailer")

# Input fields
url = st.text_input("Enter the URL of the news article or webpage:")
email = st.text_input("Enter your email address:")
submit = st.button("Summarize and Send")


# Main logic
if submit and url and email:
    with st.spinner("Summarizing article..."):
        summary = get_summary(url)
        st.write("### Summary")
        st.write(summary)

        if not summary.startswith("Error"):
            # Replace with your email and app password (for Gmail)
            with st.spinner("Sending email..."):
                email_result = send_email(summary, email, sender_email, sender_password)
                if email_result is True:
                    st.success("Summary sent to your email!")
                else:
                    st.error(email_result)
        else:
            st.error(summary)

# Instructions for users
st.markdown("""
### Instructions
1. Enter a valid news article or webpage URL.
2. Provide your email address.
3. Click "Summarize and Send" to receive the summary.
**Note**: Ensure the URL is accessible and contains extractable text.
""")