import streamlit as st

# Streamlit Page Configuration
st.set_page_config(page_title="AI Search Widget", page_icon="🔍", layout="wide")

st.title("🔍 AI Search Widget Integration")

# HTML Code for Google AI Search Widget
search_widget_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- Google AI Search Widget JavaScript -->
    <script src="https://cloud.google.com/ai/gen-app-builder/client?hl=en_US"></script>

    <style>
        /* Styling for the search input */
        #searchWidgetTrigger {
            padding: 10px;
            width: 250px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 5px;
            outline: none;
            cursor: pointer;
        }

        /* Positioning for the widget */
        gen-search-widget {
            position: absolute;
            z-index: 9999;
        }
    </style>
</head>
<body>

    <h3>Search Here:</h3>

    <!-- Search Widget (Hidden by Default) -->
    <gen-search-widget
        configId="92a03cfa-4608-49bd-a888-e23a77bec5bb"
        triggerId="searchWidgetTrigger">
    </gen-search-widget>

    <!-- Search Input Field to Open Widget -->
    <input type="text" placeholder="Search here..." id="searchWidgetTrigger" />

    <script>
        // Optional: Manually trigger the search widget on input click
        document.getElementById("searchWidgetTrigger").addEventListener("click", function () {
            document.querySelector("gen-search-widget").setAttribute("open", "true");
        });
    </script>

</body>
</html>
"""

# Embed the widget inside Streamlit using st.components.v1.html
st.components.v1.html(search_widget_html, height=300)

