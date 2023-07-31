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
    st.write(f"Click the button below to open the random link:")
    if st.button("Open Random Link"):
        st.experimental_rerun()  # Rerun the app to show the link options

    if st.button("Open in New Tab"):
        st.experimental_rerun()  # Rerun the app to show the link options
        st.markdown(f'<a href="{rand_link}" target="_blank">Link</a>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
