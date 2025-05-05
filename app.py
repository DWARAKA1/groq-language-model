import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Streamlit app
st.title("Groq Language Model Interface")
st.write("Interact with the Groq language model using the `llama-3.3-70b-versatile` model.")

# Input prompt
user_prompt = st.text_area("Enter your prompt:", "Explain the importance of fast language models")

# Submit button
if st.button("Generate Response"):
    with st.spinner("Generating response..."):
        try:
            # Call the Groq API
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": user_prompt,
                    }
                ],
                model="llama-3.3-70b-versatile",
            )
            # Display the response
            response = chat_completion.choices[0].message.content
            st.subheader("Response:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")