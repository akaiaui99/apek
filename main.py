import streamlit as st
import random

rand_links = [
    "https://netflxkauiaoia.com/?oaia9298298kja",
    "https://netactuaia7822.com/?opaioa89aHJhj"
]

def get_random_link():
    return random.choice(rand_links)

def main():
    st.set_page_config(page_title="Redirect Page", layout="wide")

    rand_link = get_random_link()

    # Display the random link
    st.write(f"Click the button below to open a new tab and visit the random link:")
    if st.button("Open Random Link in New Tab"):
        js_code = f"window.open('{rand_link}', '_blank');"
        html_button = f'<button onclick="{js_code}">Open Random Link in New Tab</button>'
        st.markdown(html_button, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
