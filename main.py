import streamlit as st
import time
import random

def get_random_url():
    urls = [
        "https://netflxkauiaoia.com/?oaia9298298kja",
        "https://netactuaia7822.com/?opaioa89aHJhj"
    ]
    return random.choice(urls)

def main():
    st.title("Aplikasi Redirect Otomatis Streamlit")
    st.write("Anda akan diarahkan secara otomatis ke salah satu URL.")

    while True:
        rand_url = get_random_url()
        st.markdown(f'<meta http-equiv="refresh" content="5;URL=\'{rand_url}\'"/>', unsafe_allow_html=True)
        time.sleep(5)  # Waktu tunggu sebelum mengalihkan ke URL berikutnya

if __name__ == "__main__":
    main()
