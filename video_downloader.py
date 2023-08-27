```python
from pytube import YouTube
import os
import shutil
from utils import get_video_info, create_directory, move_video

def download_video(video_url):
    yt = YouTube(video_url)
    uploader_channel = get_video_info(yt)
    create_directory(uploader_channel)
    video = yt.streams.get_highest_resolution()
    video.download(output_path='temp')
    move_video('temp', uploader_channel, video.title)
```