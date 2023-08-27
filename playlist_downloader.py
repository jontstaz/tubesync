```python
from pytube import Playlist
from video_downloader import download_video
from utils import get_video_info, create_directory, move_video
import os
import shutil

def download_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        video = get_video_info(video_url)
        uploader_channel = video.uploader
        create_directory(uploader_channel)
        download_video(video_url)
        move_video(video.title, uploader_channel)
```