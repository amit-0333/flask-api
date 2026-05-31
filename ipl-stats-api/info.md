<div align="center">

```
██╗██████╗ ██╗         ███████╗████████╗ █████╗ ████████╗███████╗
██║██╔══██╗██║         ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝
██║██████╔╝██║         ███████╗   ██║   ███████║   ██║   ███████╗
██║██╔═══╝ ██║         ╚════██║   ██║   ██╔══██║   ██║   ╚════██║
██║██║     ███████╗    ███████║   ██║   ██║  ██║   ██║   ███████║
╚═╝╚═╝     ╚══════╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝
```

### 🏏 IPL Stats API

> A Flask REST API serving **Indian Premier League** cricket statistics — teams, players, head-to-head records & more.

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-FF6B6B?style=for-the-badge)
![JSON](https://img.shields.io/badge/Returns-JSON-F7DF1E?style=for-the-badge)
![Cricket](https://img.shields.io/badge/Cricket-IPL-0078D4?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

</div>

---

## 📌 About

This is a **beginner Flask project** that exposes IPL cricket data through a REST API.
Every route returns clean **JSON** — making it easy to consume from any frontend, Postman, or curl.

Built to learn:
- How Flask routing works
- How to handle query parameters
- How to return structured JSON responses
- How to organize API logic into modules

---

## 🗂️ File Structure

```bash
ipl-stats-api/
│
├── 📄 app.py         # Flask app — all routes defined here
├── 📄 ipl.py         # Data & business logic (helper functions)
└── 📄 README.md
```

### 🧠 How It Works

```
Request → app.py (route) → ipl.py (logic + data) → JSON Response
```

| File | Role |
|------|------|
| `app.py` | Defines all URL routes, handles HTTP requests |
| `ipl.py` | Contains all data & functions that process the requests |

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
| `GET` | `/` | — | Health check — returns `hello world` |
| `GET` | `/api/teams` | — | List of all IPL teams |
| `GET` | `/api/teamvteam` | `?team1=&team2=` | Head-to-head record between two teams |
| `GET` | `/api/team-record` | `?team=` | Overall win/loss record of a team |
| `GET` | `/api/batting-record` | `?batsman=` | Career batting stats of a batsman |
| `GET` | `/api/bowling-record` | `?bowler=` | Career bowling stats of a bowler |

---

## 🧪 Example Requests

```bash
# ✅ Health check
curl http://127.0.0.1:5000/

# 🏟️ All IPL teams
curl http://127.0.0.1:5000/api/teams

# ⚔️ Head-to-head: MI vs CSK
curl "http://127.0.0.1:5000/api/teamvteam?team1=Mumbai+Indians&team2=Chennai+Super+Kings"

# 📊 Team overall record
curl "http://127.0.0.1:5000/api/team-record?team=Mumbai+Indians"

# 🏏 Batting record
curl "http://127.0.0.1:5000/api/batting-record?batsman=Virat+Kohli"

# 🎯 Bowling record
curl "http://127.0.0.1:5000/api/bowling-record?bowler=Jasprit+Bumrah"
```

### 🌐 Or paste directly in browser

```
http://127.0.0.1:5000/api/teams
http://127.0.0.1:5000/api/teamvteam?team1=Mumbai+Indians&team2=Chennai+Super+Kings
http://127.0.0.1:5000/api/team-record?team=Royal+Challengers+Bangalore
http://127.0.0.1:5000/api/batting-record?batsman=Rohit+Sharma
http://127.0.0.1:5000/api/bowling-record?bowler=Lasith+Malinga
```

---

## 📤 Sample JSON Response

```json
// GET /api/teams
{
  "teams": [
    "Mumbai Indians",
    "Chennai Super Kings",
    "Royal Challengers Bangalore",
    "Kolkata Knight Riders",
    ...
  ]
}

// GET /api/batting-record?batsman=Virat+Kohli
{
  "batsman": "Virat Kohli",
  "matches": 237,
  "runs": 7263,
  "average": 37.97,
  "strike_rate": 130.02
}
```

---

## 🧩 My Approach

```
1. 📖 Understand what cricket data to expose
2. 🔨 Design clean, readable URL routes
3. 🚀 Write Flask endpoints in app.py
4. 🧹 Keep logic separate in ipl.py
5. ✅ Test every route with curl & browser
```

---

## 🎯 Learning Goals

- [x] Set up a Flask server
- [x] Create GET routes
- [x] Handle query parameters (`?team=`)
- [x] Return JSON with `jsonify()`
- [x] Separate logic into a module (`ipl.py`)
- [ ] Add error handling for invalid inputs
- [ ] Add 404 responses for unknown teams/players
- [ ] Connect to a real IPL database

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
