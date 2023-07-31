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

    # Get a random link
    rand_link = get_random_link()

    # Redirect the user to the random link
    st.redirect(rand_link)

if __name__ == "__main__":
    main()
