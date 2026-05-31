<div align="center">

```
███████╗██╗      █████╗ ███████╗██╗  ██╗     █████╗ ██████╗ ██╗
██╔════╝██║     ██╔══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██║
█████╗  ██║     ███████║███████╗█████╔╝     ███████║██████╔╝██║
██╔══╝  ██║     ██╔══██║╚════██║██╔═██╗     ██╔══██║██╔═══╝ ██║
██║     ███████╗██║  ██║███████║██║  ██╗    ██║  ██║██║     ██║
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝
```

# 🏏 IPL Stats API &nbsp;·&nbsp; 🎵 Spotify API

> **Two REST APIs built with Flask** — Cricket stats & Music data, served as clean JSON.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-FF6B6B?style=flat-square)
![JSON](https://img.shields.io/badge/Returns-JSON-F7DF1E?style=flat-square)

</div>

---

## 📁 Project Structure

```
flask-api-basics/
│
├── ipl_app.py          # IPL Stats API
├── ipl.py              # IPL data & logic
│
├── spotify_app.py      # Spotify API
├── spotify.py          # Spotify data & logic
│
└── README.md
```

---

## 🏏 IPL Stats API

> Cricket statistics — teams, players, head-to-head records & more.

### Run

```bash
python ipl_app.py
# Server starts at http://127.0.0.1:5000
```

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `GET` | `/api/teams` | All IPL teams |
| `GET` | `/api/teamvteam` | Head-to-head record |
| `GET` | `/api/team-record` | Overall team stats |
| `GET` | `/api/batting-record` | Batsman stats |
| `GET` | `/api/bowling-record` | Bowler stats |

### Example Usage

```bash
# All teams
curl http://127.0.0.1:5000/api/teams

# Head-to-head
curl "http://127.0.0.1:5000/api/teamvteam?team1=Mumbai+Indians&team2=Chennai+Super+Kings"

# Team record
curl "http://127.0.0.1:5000/api/team-record?team=Mumbai+Indians"

# Batting record
curl "http://127.0.0.1:5000/api/batting-record?batsman=Virat+Kohli"

# Bowling record
curl "http://127.0.0.1:5000/api/bowling-record?bowler=Jasprit+Bumrah"
```

---

## 🎵 Spotify API

> Music data — songs, artists, albums, charts & search.

### Run

```bash
python spotify_app.py
# Server starts at http://127.0.0.1:5000
```

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `GET` | `/api/songs` | All songs |
| `GET` | `/api/song/<song>` | Specific song details |
| `GET` | `/api/random` | Random song |
| `GET` | `/api/artists` | All artists |
| `GET` | `/api/artist/<artist>` | Artist's songs |
| `GET` | `/api/albums` | All albums |
| `GET` | `/api/album/<album>` | Album details |
| `GET` | `/api/top-tracks` | Top tracks chart |
| `GET` | `/api/top-artists` | Top artists chart |
| `GET` | `/api/search/<keyword>` | Search by keyword |
| `GET` | `/api/stats` | Overall stats |

### Example Usage

```bash
# All songs
curl http://127.0.0.1:5000/api/songs

# Specific song
curl http://127.0.0.1:5000/api/song/Blinding+Lights

# Random song
curl http://127.0.0.1:5000/api/random

# Artist songs
curl http://127.0.0.1:5000/api/artist/The+Weeknd

# Album details
curl http://127.0.0.1:5000/api/album/After+Hours

# Search
curl http://127.0.0.1:5000/api/search/love

# Top charts
curl http://127.0.0.1:5000/api/top-tracks
curl http://127.0.0.1:5000/api/top-artists

# Stats
curl http://127.0.0.1:5000/api/stats
```

---

## ⚙️ Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/flask-api-basics.git
cd flask-api-basics

# Install dependencies
pip install flask

# Run either API
python ipl_app.py
python spotify_app.py
```

---

## 🛠️ Tech Stack

- **Python** — Core language
- **Flask** — Web framework
- **JSON** — Response format

---

<div align="center">

Made with ❤️ &nbsp;|&nbsp; Learning Flask one endpoint at a time 🚀

</div>
