import streamlit as st
import random

rand_links = [
    "https://netflxkauiaoia.com/?oaia9298298kja",
    "https://netactuaia7822.com/?opaioa89aHJhj"
]

last_link_index = -1

def get_random_link():
    global last_link_index
    while True:
        rand_link_index = random.randint(0, len(rand_links) - 1)
        if rand_link_index != last_link_index:
            break
    last_link_index = rand_link_index
    return rand_links[rand_link_index]

def main():
    st.set_page_config(page_title="Redirect Page", layout="wide")

    rand_link = get_random_link()

    # Redirect the user
    st.markdown(f'<meta http-equiv="refresh" content="0;URL=\'{rand_link}\'"/>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
