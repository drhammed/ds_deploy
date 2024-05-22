import streamlit as st
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv('api.env')

# Retrieve the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

st.title('AI Search Assistant')

query = st.text_input('Enter your query:')

if st.button('Search'):
    if query:
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Use the appropriate engine
                prompt=query,
                max_tokens=100
            )
            st.success(response.choices[0].text.strip())
        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning('Please enter a query.')
