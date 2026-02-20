# 6.1 Example Streamlit App: Text Summarization
# This is the code you would save as app.py locally using
# a text editor such as Notepad, VS Code, etc.

import streamlit as st
from openai import OpenAI
import os

# Configure the Streamlit page
st.set_page_config(page_title="Text Summarizer", layout="wide")

# Add a title and description
st.title("AI Text Summarizer")
st.write("Paste your text below and let AI create a concise summary for you.")

# Initialize the OpenAI client using the API key from Streamlit secrets
# When deployed, this will read from the Secrets section in Streamlit Cloud
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Create a text area for user input
user_text = st.text_area(
    "Enter the text you want to summarize:",
    height=200,
    placeholder="Paste your text here..."
)

# Create a button to trigger summarization
if st.button("Summarize Text"):
    if user_text.strip():
        # Show a loading message while processing
        with st.spinner("Summarizing your text..."):
            try:
                # Create the prompt for summarization
                prompt = f"Please summarize the following text in 2-3 sentences: {user_text}"

                # Call the OpenAI API
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )

                # Extract and display the summary
                summary = response.choices[0].message.content
                st.success("Summary created successfully!")
                st.write("**Summary:**")
                st.write(summary)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter some text to summarize.")

# Add footer with instructions
st.markdown("---")
st.info("This app uses OpenAI's GPT models. Make sure your API key is set in the Secrets section.")