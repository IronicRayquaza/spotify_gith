import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")

def get_access_token():
    response = requests.post(
        "https://accounts.spotify.com/api/token",
        data={
            "grant_type": "refresh_token",
            "refresh_token": REFRESH_TOKEN,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )
    return response.json().get("access_token")

def get_current_track(token):
    headers = {"Authorization": f"Bearer {token}"}
    r = requests.get("https://api.spotify.com/v1/me/player/currently-playing", headers=headers)
    if r.status_code == 200 and r.json().get("item"):
        item = r.json()["item"]
        return item["name"], item["artists"][0]["name"]
    # fallback to recently played
    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?limit=1", headers=headers)
    if r.status_code == 200 and r.json()["items"]:
        track = r.json()["items"][0]["track"]
        return track["name"], track["artists"][0]["name"]
    return None, None

def handler(request, response):
    token = get_access_token()
    song, artist = get_current_track(token)
    if song and artist:
        svg = f'''<svg width="400" height="60" xmlns="http://www.w3.org/2000/svg">
        <rect width="400" height="60" fill="#1DB954"/>
        <text x="20" y="35" font-size="24" fill="#fff">🎵 {song} - {artist}</text>
        </svg>'''
    else:
        svg = '''<svg width="400" height="60" xmlns="http://www.w3.org/2000/svg">
        <rect width="400" height="60" fill="#ccc"/>
        <text x="20" y="35" font-size="24" fill="#333">No song playing</text>
        </svg>'''
    response.headers["Content-Type"] = "image/svg+xml"
    response.body = svg
    return response 