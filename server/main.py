from flask import Flask, render_template
import os, ffmpeg_streaming
from ffmpeg_streaming import Formats


def get_file_path(filename="", local=True):
    if local:
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(os.path.join(BASE_DIR, "test"), filename)
    else:
        return filename


app = Flask(__name__)


@app.route("/video.mpd")
def video_mpd():
    # Get the video information from your database or other data source
    video_info = {"title": "My Video", "url": "/video.mp4", "duration": 60}

    # Render the MPD template with the video information
    file_path = os.path.join(get_file_path("output"), "dash.mpd")
    print(file_path)
    mpd = render_template(file_path, video=video_info)

    # Return the MPD file with the appropriate content type
    return mpd, {"Content-Type": "application/dash+xml"}


def main():
    file_path = os.path.join(get_file_path("output"), "dash.mpd")
    # print(file_path)
    video = ffmpeg_streaming.input(get_file_path("sample_video.mp4"))
    dash = video.dash(Formats.h264())
    dash.auto_generate_representations()
    dash.output(file_path, async_run=False)
    app.run()


main()
