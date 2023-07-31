import streamlit as st
import random
import webbrowser

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
    if st.button("Visit Random Link in New Tab"):
        webbrowser.open_new_tab(rand_link)

if __name__ == "__main__":
    main()
