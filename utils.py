```python
import os
from pytube import YouTube

def get_video_info(video_url):
    video = YouTube(video_url)
    uploader_channel = video.author
    return uploader_channel

def create_directory(uploader_channel):
    if not os.path.exists(uploader_channel):
        os.makedirs(uploader_channel)

def move_video(video_path, uploader_channel):
    destination_path = os.path.join(uploader_channel, os.path.basename(video_path))
    os.rename(video_path, destination_path)
```