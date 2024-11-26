from flask import Flask, request, jsonify
from dotenv import load_dotenv
import requests
import os


load_dotenv()

app = Flask(__name__)

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"


@app.route("/get_video", methods=["GET"])
def get_video():
    artist = request.args.get("artist")
    song = request.args.get("song")
    query = f"{artist} {song} official music video"
    response = requests.get(
        YOUTUBE_SEARCH_URL,
        params={
            "part": "snippet",
            "q": query,
            "key": YOUTUBE_API_KEY,
            "type": "video",
            "maxResults": 1
        }
    )
    data = response.json()
    video_id = data["items"][0]["id"]["videoId"]
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    return jsonify({"video_url": video_url})


if __name__ == '__main__':
    app.run(debug=True)