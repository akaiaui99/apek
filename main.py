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

    # Get a random link
    rand_link = get_random_link()

    # Automatically open the random link in the browser
    webbrowser.open(rand_link)

if __name__ == "__main__":
    main()
