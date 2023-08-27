```python
from playlist_downloader import download_playlist
from video_downloader import download_video

def main():
    while True:
        print("1. Download a single video")
        print("2. Download a playlist")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            video_url = input("Enter the URL of the video: ")
            download_video(video_url)
        elif choice == '2':
            playlist_url = input("Enter the URL of the playlist: ")
            download_playlist(playlist_url)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```