from flask import Flask, jsonify
import spotify

app = Flask(__name__)

@app.route('/')
def home():
    return "This Is Spotify API"

# Songs 
@app.route("/api/songs")
def songsAPI():
    return jsonify({"songs": spotify.get_all_songs()})

@app.route("/api/song/<song>")
def songAPI(song):
    return jsonify(spotify.get_song(song))

@app.route("/api/random")
def randomAPI():
    return jsonify(spotify.random_song())

# Artists 
@app.route("/api/artists")
def artistsAPI():
    return jsonify({"artists": spotify.get_artists()})

@app.route("/api/artist/<artist>")
def artistAPI(artist):
    return jsonify(spotify.get_artist_songs(artist))

# Albums 
@app.route("/api/albums")
def albumsAPI():
    return jsonify({"albums": spotify.get_albums()})

@app.route("/api/album/<album>")
def albumAPI(album):
    return jsonify(spotify.get_album(album))

# Charts & Search 
@app.route("/api/top-tracks")
def topTracksAPI():
    return jsonify(spotify.top_tracks())

@app.route("/api/top-artists")
def topArtistsAPI():
    return jsonify(spotify.top_artists())

@app.route("/api/search/<keyword>")
def searchAPI(keyword):
    return jsonify(spotify.search(keyword))

@app.route("/api/stats")
def statsAPI():
    return jsonify(spotify.stats())

if __name__ == "__main__":
    app.run(debug=True)