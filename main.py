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

    # Create a button to trigger the redirect
    if st.button("Visit Random Link"):
        js_code = f"window.location.href = '{rand_link}';"
        html_button = f'<button onclick="{js_code}">Visit Random Link</button>'
        st.markdown(html_button, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
