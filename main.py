import webbrowser

def redirect_to_url(url):
    webbrowser.open_new_tab(url)

if __name__ == "__main__":
    url_to_redirect = "https://www.example.com"  # Ganti dengan URL yang diinginkan
    redirect_to_url(url_to_redirect)
