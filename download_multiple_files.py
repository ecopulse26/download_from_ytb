
#  https://youtu.be/Aq5WXmQQooo?si=XYuP9dK8f-2sh0r3
#  https://youtu.be/QDia3e12czc?si=Lz8tIdKiXc4C33Aq

from yt_dlp import YoutubeDL


def main():
    urls = []
    print("Entrez les URLs une par une. Tapez 'q' pour lancer le telechargement.")
    while True:
        inp01 = input("URL de la video YouTube : ")
        if inp01 == "q":
            break
        urls.append(inp01)

    options = {
        "outtmpl": "%(title)s.%(ext)s",
        "format": "best",
    }

    for i, url in enumerate(urls):
        print(f"[{i + 1}/{len(urls)}] Telechargement de {url}")
        with YoutubeDL(options) as ydl:
            ydl.download([url])

    print("Telechargement termine.")

main()
