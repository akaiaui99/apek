from flask import Flask

app = Flask(__name__)

rand_links = [
    "https://netflxkauiaoia.com/?oaia9298298kja",
    "https://netactuaia7822.com/?opaioa89aHJhj"
]

last_link_index = -1

@app.route('/')
def do_get():
    global last_link_index

    # Ensure that the next link is different from the previous one
    while True:
        rand_link_index = random.randint(0, len(rand_links) - 1)
        if rand_link_index != last_link_index:
            break

    last_link_index = rand_link_index
    rand_link = rand_links[rand_link_index]

    output = f'<!DOCTYPE html><html><head><base target="_top">'
    output += '<style>'
    output += 'body {'
    output += '  background-color: #e6e6e6;'
    output += '}'
    output += 'div {'
    output += '  position: fixed;'
    output += '  top: 50%;'
    output += '  left: 50%;'
    output += '  transform: translate(-50%, -50%);'
    output += '}'
    output += 'a {'
    output += '  display: block;'
    output += '}'
    output += 'img {'
    output += '  max-width: 100%;'
    output += '  height: auto;'
    output += '}'
    # CSS media queries for responsiveness
    output += '@media (max-width: 600px) {'
    output += '  div {'
    output += '    width: 90%;'
    output += '  }'
    output += '}'
    output += '</style>'
    output += '</head><body>'
    output += f'<div><a href="{rand_link}"><img src="https://cf-assets.www.cloudflare.com/slt3lc6tev37/79wsjD0Xy7FmmYvR0sCncy/5b732b7e26adb7d6c06d943d14dc4acd/not-a-robot.png" /></a></div>'
    output += '</body></html>'

    return output

if __name__ == '__main__':
    app.run()
