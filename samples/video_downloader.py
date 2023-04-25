import os
import sys
import re
import yt_dlp

def video_downloader():
    url_pattern = re.compile(r'^https?://[^\s/$.?#].[^\s]*$')

    while True:
        video_url = input("Video URL: ")

        if url_pattern.match(video_url):
            ydl = yt_dlp.YoutubeDL()
            ydl.extract_info(video_url, download=False)
            break
        else:
            print('\nError: Invalid URL Format')
        return

    while True:
        
        if not os.path.exists('downloads/'):
            try:
                os.mkdir('downloads')
                break
            except OSError:
                print("Invalid path, please try again.")
        else:
            break

    ydl_opts = {'outtmpl': 'downloads/' + '%(title)s.%(ext)s'}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = 'Video Dowloader'
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')
    video_downloader()

    while True:
        response = input('\nDo you want to continue? (Y/N) ')
        if response == 'y' or response == 'Y':
            main()
        elif response == 'n' or response == 'N':
            print('\nThank you and have a great day.\n')
            sys.exit()
        else:
            print('\nError: Please select Y or N.\n')
            continue

if __name__ == '__main__':
    main() 