import streamlit as st

# Streamlit Page Configuration
st.set_page_config(page_title="AI Search Widget", page_icon="🔍", layout="wide")

st.title("🔍 AI Search Widget Integration")

# HTML Code for Google AI Search Widget (Updated)
search_widget_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Google AI Search Widget JavaScript -->
    <script src="https://cloud.google.com/ai/gen-app-builder/client?hl=en_US"></script>

    <style>
        /* Style for the button */
        #searchWidgetTrigger {
            padding: 12px 20px;
            font-size: 16px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: 0.3s;
        }

        #searchWidgetTrigger:hover {
            background-color: #0056b3;
        }

        /* Positioning for the widget */
        gen-search-widget {
            position: relative;
            display: block;
            width: 100%;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h3>Click the button to search:</h3>

    <!-- Search Button to Open Widget -->
    <button id="searchWidgetTrigger">Open Search</button>

    <!-- Search Widget (Hidden by Default) -->
    <gen-search-widget
        configId="92a03cfa-4608-49bd-a888-e23a77bec5bb"
        triggerId="searchWidgetTrigger">
    </gen-search-widget>

</body>
</html>
"""

# Embed the widget inside Streamlit
st.components.v1.html(search_widget_html, height=350)

