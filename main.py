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
    st.set_page_config(page_title="Random Link Page")
    
    rand_link = get_random_link()

    st.write("<!DOCTYPE html><html><head><base target='_top'><style>body { background-color: #e6e6e6; } div { position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); } a { display: block; } img { max-width: 100%; height: auto; } @media (max-width: 600px) { div { width: 90%; } }</style></head><body>", unsafe_allow_html=True)
    st.write(f"<div><a href='{rand_link}'><img src='https://cf-assets.www.cloudflare.com/slt3lc6tev37/79wsjD0Xy7FmmYvR0sCncy/5b732b7e26adb7d6c06d943d14dc4acd/not-a-robot.png' /></a></div>", unsafe_allow_html=True)
    st.write("</body></html>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
