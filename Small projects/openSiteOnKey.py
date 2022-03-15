import webbrowser

import keyboard


def start():
    return webbrowser.open_new_tab('https://stackoverflow.com')


while True:
    if keyboard.is_pressed('p'):
        start()
    elif keyboard.is_pressed('esc'):
        break
