1. "pytube" Library: All files will use the "pytube" library for downloading videos from YouTube. 

2. "os" Library: All files will use the "os" library for directory and file operations.

3. "shutil" Library: The "video_downloader.py" and "playlist_downloader.py" files will use the "shutil" library for moving downloaded videos to the appropriate folders.

4. "get_video_info" Function: This function will be defined in "utils.py" and used in "video_downloader.py" and "playlist_downloader.py" to extract video information such as the uploader/channel name.

5. "download_video" Function: This function will be defined in "video_downloader.py" and used in "main.py" and "playlist_downloader.py" to download individual videos.

6. "download_playlist" Function: This function will be defined in "playlist_downloader.py" and used in "main.py" to download all videos from a playlist.

7. "create_directory" Function: This function will be defined in "utils.py" and used in "video_downloader.py" and "playlist_downloader.py" to create a new directory for each uploader/channel.

8. "move_video" Function: This function will be defined in "utils.py" and used in "video_downloader.py" and "playlist_downloader.py" to move downloaded videos to the appropriate folders.

9. "video_url" Variable: This variable will be used in "main.py", "video_downloader.py", and "playlist_downloader.py" to store the URL of the video to be downloaded.

10. "playlist_url" Variable: This variable will be used in "main.py" and "playlist_downloader.py" to store the URL of the playlist to be downloaded.

11. "uploader_channel" Variable: This variable will be used in "video_downloader.py", "playlist_downloader.py", and "utils.py" to store the name of the uploader/channel.