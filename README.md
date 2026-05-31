<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=700&size=28&pause=1000&color=00D9FF&center=true&vCenter=true&width=600&lines=🏏+IPL+Stats+API;🎵+Spotify+Stats+API;Built+with+Flask+%26+Python;Clean+JSON+%7C+Fast+%7C+Simple" alt="Typing SVG" />

<br/>

```
███████╗██╗      █████╗ ███████╗██╗  ██╗     █████╗ ██████╗ ██╗
██╔════╝██║     ██╔══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██║
█████╗  ██║     ███████║███████╗█████╔╝     ███████║██████╔╝██║
██╔══╝  ██║     ██╔══██║╚════██║██╔═██╗     ██╔══██║██╔═══╝ ██║
██║     ███████╗██║  ██║███████║██║  ██╗    ██║  ██║██║     ██║
╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝
```

### 🏏 IPL Stats API &nbsp;·&nbsp; 🎵 Spotify Stats API

> Two REST APIs built with **Flask & Python** — Cricket stats & Music data, served as clean JSON.

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-FF6B6B?style=for-the-badge)
![JSON](https://img.shields.io/badge/Returns-JSON-F7DF1E?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

<br/>

</div>

---

## 📦 Summary

This repo contains **2 Flask REST APIs** built as learning projects.
Each API lives in its own folder and serves real data as JSON over HTTP.

| # | Folder | Description | Endpoints |
|---|--------|-------------|-----------|
| 01 | 🏏 [`ipl-stats-api`](#-ipl-stats-api-1) | Cricket stats — teams, players, head-to-head records | 6 |
| 02 | 🎵 [`spotify-stats-api`](#-spotify-stats-api-1) | Music data — songs, artists, albums, charts & search | 12 |

---

## 🗂️ Project Structure

```bash
flask-api/
│
├── 📂 ipl-stats-api/
│   ├── app.py              # Flask routes
│   └── ipl.py              # Data & logic
│
├── 📂 spotify-stats-api/
│   ├── app.py              # Flask routes
│   └── spotify.py          # Data & logic
│
└── 📄 README.md
```

---

## ⚙️ Setup

```bash
# 1. Clone the repo
git clone https://github.com/amit-0333/flask-api.git

# 2. Navigate into it
cd flask-api

# 3. Install Flask
pip install flask

# 4. Run any API
cd ipl-stats-api && python app.py
cd spotify-stats-api && python app.py
```

---

## 🏏 IPL Stats API

> Cricket statistics API — teams, head-to-head records, batting & bowling stats.

```bash
cd ipl-stats-api
python app.py
# → Server running at http://127.0.0.1:5000
```

### 🔗 Endpoints

| Method | Endpoint | Params | Description |
|--------|----------|--------|-------------|
| `GET` | `/` | — | Health check |
| `GET` | `/api/teams` | — | All IPL teams |
| `GET` | `/api/teamvteam` | `?team1=&team2=` | Head-to-head record |
| `GET` | `/api/team-record` | `?team=` | Overall team stats |
| `GET` | `/api/batting-record` | `?batsman=` | Batsman stats |
| `GET` | `/api/bowling-record` | `?bowler=` | Bowler stats |

### 🧪 Example Requests

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

## 🎵 Spotify Stats API

> Music data API — browse songs, artists, albums, search tracks & view charts.

```bash
cd spotify-stats-api
python app.py
# → Server running at http://127.0.0.1:5000
```

### 🔗 Endpoints

| Method | Endpoint | Params | Description |
|--------|----------|--------|-------------|
| `GET` | `/` | — | Health check |
| `GET` | `/api/songs` | — | All songs |
| `GET` | `/api/song/<song>` | path | Specific song details |
| `GET` | `/api/random` | — | Random song |
| `GET` | `/api/artists` | — | All artists |
| `GET` | `/api/artist/<artist>` | path | Artist's songs |
| `GET` | `/api/albums` | — | All albums |
| `GET` | `/api/album/<album>` | path | Album details |
| `GET` | `/api/top-tracks` | — | Top tracks chart |
| `GET` | `/api/top-artists` | — | Top artists chart |
| `GET` | `/api/search/<keyword>` | path | Search by keyword |
| `GET` | `/api/stats` | — | Overall stats |

### 🧪 Example Requests

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

# Charts
curl http://127.0.0.1:5000/api/top-tracks
curl http://127.0.0.1:5000/api/top-artists

# Stats
curl http://127.0.0.1:5000/api/stats
```

---

## 🧩 My Approach

```
1. 📖 Understand what data needs to be served
2. 🔨 Design the routes & URL structure
3. 🚀 Write the Flask endpoints
4. 🧹 Keep the code clean & modular
5. ✅ Test every route manually
```

---

## 🎯 Learning Goals

- [x] Build and run a Flask server
- [x] Create REST API routes
- [x] Use query parameters (`?key=value`)
- [x] Use path parameters (`/<variable>`)
- [x] Return clean JSON responses
- [x] Organize code into modules
- [ ] Add error handling & 404 responses
- [ ] Connect to a real database
- [ ] Deploy to a cloud platform

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

> 📝 *Built while learning Flask — solutions and structure may improve over time.*

⭐ **Star this repo if you found it useful!**

</div>
