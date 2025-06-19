# Spotify Now Playing README Widget

A dynamic, real-time Spotify now-playing widget for your GitHub README, powered by Flask and the Spotify API.

## Features
- Shows your currently playing Spotify song (or most recent song)
- Embeddable as an SVG image in your GitHub README

## Setup

### 1. Register a Spotify App
- Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- Create an app, set redirect URI to `http://localhost/callback/`
- Note your **Client ID** and **Client Secret**

### 2. Get Your Refresh Token
Follow the steps in the project description or use a helper script to get your refresh token. You will need:
- `CLIENT_ID`
- `CLIENT_SECRET`
- `REFRESH_TOKEN`

### 3. Configure Environment Variables
Copy `.env.example` to `.env` and fill in your credentials:
```
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
REFRESH_TOKEN=your_refresh_token
```

### 4. Install Dependencies
```
pip install -r requirements.txt
```

### 5. Run the App
```
python main.py
```

The app will be available at `http://localhost:5000/`.

## Deploy
You can deploy this app to PythonAnywhere, Heroku, or any other cloud provider that supports Python and Flask.

## Add to Your GitHub README
Embed the widget in your README:
```markdown
<a href="https://yourusername.pythonanywhere.com/">
  <img src="https://yourusername.pythonanywhere.com/" alt="Spotify Now Playing" />
</a>
```

## License
MIT 