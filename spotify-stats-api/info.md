<div align="center">

```
███████╗██████╗  ██████╗ ████████╗██╗███████╗██╗   ██╗
██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝╚██╗ ██╔╝
███████╗██████╔╝██║   ██║   ██║   ██║█████╗   ╚████╔╝ 
╚════██║██╔═══╝ ██║   ██║   ██║   ██║██╔══╝    ╚██╔╝  
███████║██║     ╚██████╔╝   ██║   ██║██║        ██║   
╚══════╝╚═╝      ╚═════╝    ╚═╝   ╚═╝╚═╝        ╚═╝   
```

### 🎵 Spotify Stats API

> A Flask REST API serving **music data** — songs, artists, albums, charts & search, all as clean JSON.

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-FF6B6B?style=for-the-badge)
![JSON](https://img.shields.io/badge/Returns-JSON-F7DF1E?style=for-the-badge)
![Music](https://img.shields.io/badge/Music-Spotify-1DB954?style=for-the-badge&logo=spotify&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</div>

---

## 📌 About

This is a **beginner Flask project** that exposes music data through a REST API.
Every route returns clean **JSON** — browse songs, discover artists, explore albums, and search tracks.

Built to learn:
- How Flask routing works with path parameters (`/<variable>`)
- How to handle both path & query parameters
- How to return structured JSON with `jsonify()`
- How to organize API logic into separate modules

---

## 🗂️ File Structure

```bash
spotify-stats-api/
│
├── 📄 app.py           # Flask app — all routes defined here
├── 📄 spotify.py       # Data & business logic (helper functions)
└── 📄 README.md
```

### 🧠 How It Works

```
Request → app.py (route) → spotify.py (logic + data) → JSON Response
```

| File | Role |
|------|------|
| `app.py` | Defines all URL routes, handles HTTP requests |
| `spotify.py` | Contains all data & functions that process the requests |

---

## ⚙️ Setup & Run

```bash
# 1. Make sure Flask is installed
pip install flask

# 2. Run the server
python app.py

# 3. Server starts at
# → http://127.0.0.1:5000
```

---

## 🔗 API Endpoints

| Method | Endpoint | Params | Description |
|--------|----------|--------|-------------|
| `GET` | `/` | — | Health check — returns `This Is Spotify API` |
| `GET` | `/api/songs` | — | All songs in the library |
| `GET` | `/api/song/<song>` | path | Specific song details |
| `GET` | `/api/random` | — | A random song |
| `GET` | `/api/artists` | — | All artists |
| `GET` | `/api/artist/<artist>` | path | All songs by an artist |
| `GET` | `/api/albums` | — | All albums |
| `GET` | `/api/album/<album>` | path | Songs in a specific album |
| `GET` | `/api/top-tracks` | — | Top tracks chart |
| `GET` | `/api/top-artists` | — | Top artists chart |
| `GET` | `/api/search/<keyword>` | path | Search songs by keyword |
| `GET` | `/api/stats` | — | Overall library stats |

---

## 🧪 Example Requests

```bash
# ✅ Health check
curl http://127.0.0.1:5000/

# 🎵 All songs
curl http://127.0.0.1:5000/api/songs

# 🔍 Specific song
curl http://127.0.0.1:5000/api/song/Blinding+Lights

# 🎲 Random song
curl http://127.0.0.1:5000/api/random

# 🎤 All artists
curl http://127.0.0.1:5000/api/artists

# 🎤 Artist songs
curl http://127.0.0.1:5000/api/artist/The+Weeknd

# 💿 All albums
curl http://127.0.0.1:5000/api/albums

# 💿 Specific album
curl http://127.0.0.1:5000/api/album/After+Hours

# 📈 Top charts
curl http://127.0.0.1:5000/api/top-tracks
curl http://127.0.0.1:5000/api/top-artists

# 🔎 Search
curl http://127.0.0.1:5000/api/search/love

# 📊 Stats
curl http://127.0.0.1:5000/api/stats
```

### 🌐 Or paste directly in browser

```
http://127.0.0.1:5000/api/songs
http://127.0.0.1:5000/api/artist/The+Weeknd
http://127.0.0.1:5000/api/album/After+Hours
http://127.0.0.1:5000/api/search/love
http://127.0.0.1:5000/api/top-tracks
http://127.0.0.1:5000/api/stats
```

---

## 📤 Sample JSON Response

```json
// GET /api/songs
{
  "songs": [
    "Blinding Lights",
    "Shape of You",
    "Starboy",
    ...
  ]
}

// GET /api/song/Blinding+Lights
{
  "title": "Blinding Lights",
  "artist": "The Weeknd",
  "album": "After Hours",
  "duration": "3:20",
  "streams": 3500000000
}

// GET /api/stats
{
  "total_songs": 100,
  "total_artists": 45,
  "total_albums": 30
}
```

---

## 🧩 My Approach

```
1. 📖 Understand what music data to expose
2. 🔨 Design clean URL routes — path vs query params
3. 🚀 Write Flask endpoints in app.py
4. 🧹 Keep all logic separate in spotify.py
5. ✅ Test every route with curl & browser
```

---

## 🎯 Learning Goals

- [x] Set up a Flask server
- [x] Create GET routes
- [x] Use path parameters (`/<variable>`)
- [x] Return JSON with `jsonify()`
- [x] Separate logic into a module (`spotify.py`)
- [x] Build search & chart endpoints
- [ ] Add error handling for unknown songs/artists
- [ ] Add 404 responses for missing resources
- [ ] Connect to the real Spotify API (OAuth)

---

## 🛠️ Tech Stack

- 🐍 **Python** — Core language
- ⚗️ **Flask** — Web framework
- 🗂️ **JSON** — Response format

---

## 👨‍💻 Author

**Amit Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-amit--0333-181717?style=flat&logo=github)](https://github.com/amit-0333)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amit%20Kumar-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/amit-kumar-a62a3640a/)
[![Kaggle](https://img.shields.io/badge/Kaggle-amitkumar038975-20BEFF?style=flat&logo=kaggle)](https://www.kaggle.com/amitkumar038975)

---

<div align="center">

> 📝 *Part of the [`flask-api`](https://github.com/amit-0333/flask-api) repo — built while learning Flask.*

⭐ **Star the repo if you found it useful!**

</div>
