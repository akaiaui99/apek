import streamlit as st
import random
import time

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

    # Auto-redirect after 5 seconds
    st.write(f'<meta http-equiv="refresh" content="5;URL=\'{rand_link}\'"/>')

    # Show a message to the user
    st.markdown(f"Redirecting to [this link]({rand_link}) in 5 seconds...")
    
    # Optional: Add a countdown timer
    for i in range(5, 0, -1):
        st.write(f"Redirecting in {i} seconds...")
        time.sleep(1)
    
    # Perform the actual redirect
    st.experimental_rerun()

if __name__ == "__main__":
    main()
