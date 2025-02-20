import streamlit as st

# Streamlit Page Configuration
st.set_page_config(page_title="AI Search Widget", page_icon="🔍", layout="wide")

st.title("🔍 AI Search Widget Integration")

st.write("Click the button below to open the AI-powered search widget in a new tab.")

# Google AI Search Widget Link (Replace with actual working link if needed)
search_widget_url = "https://cloud.google.com/ai/gen-app-builder"  # Update with your actual link

# Create a button that opens the widget in a new tab
st.markdown(f'<a href="{search_widget_url}" target="_blank"><button style="padding: 12px 20px; font-size: 16px; background-color: #007BFF; color: white; border: none; border-radius: 5px; cursor: pointer;">Open AI Search</button></a>', unsafe_allow_html=True)
