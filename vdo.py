from yt_dlp import YoutubeDL
url = input("enter youtube url: ")
options = {"format": "bv + ba/b", "merge_output_format": "mp4"}
with youtubeDL(options) as ydl:
    ydl.download([url])