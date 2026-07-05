
#  https://youtu.be/Aq5WXmQQooo?si=XYuP9dK8f-2sh0r3
from yt_dlp import YoutubeDL

def main():
    url = input("URL de la video YouTube : ").strip()

    options = {
        "outtmpl": "%(title)s.%(ext)s",
        "format": "best",
    }

    with YoutubeDL(options) as ydl:
        ydl.download([url])

    print("Telechargement termine.")

if __name__ == "__main__":
    main()
