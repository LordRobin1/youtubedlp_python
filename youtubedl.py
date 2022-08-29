import os
from yt_dlp import YoutubeDL

x = True
SAVE_PATH = '/'.join(os.getcwd().split('/')[:3]) + '/Downloads'
opts_a = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '256',
    }],
    'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
}
opts_v = {
    'format': 'bestvideo',
    'postprocessors': [{
        'preferredcodec': 'mp4',
    }],
    'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
}
opts_r = {
    'outtmpl': SAVE_PATH + '/%(title)s.%(ext)s',
}

def download (url, opts={}):
    ydl_opts = opts
    with YoutubeDL(ydl_opts) as ydl: 
        ydl.download(url)

def dialog ():
    url = ''
    while url == "":
        print("copypaste url: ", end="")
        url = input()

    print("[V]ideo || [A]udio || [R]eddit (or for Youtube if 'v' doesn't work)")
    va = input()
    
    if va == "a": 
        opts = opts_a
    elif va == "v":
        opts = opts_v
    else:
        opts = opts_r

    try:
        download(url, opts)
    except Exception as exception:
        print(f"Error: {exception} \nEnter a valid URL") if va == "v" else print("Enter a valid URL")
        dialog()

while x:
    dialog()
    print("\n" + "="*6 + "\n Done\n" + "="*6 + "\n\n Exit? (y/n)", end="  ")
    exit = input()
    if exit == "y": x = False