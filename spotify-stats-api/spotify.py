import pandas as pd

# Load and clean dataset
df = pd.read_csv("data.csv").fillna("N/A")

# --- Songs ---

def get_all_songs():
    return df["track_name"].tolist()

def get_song(song_name):
    match = df[df["track_name"].str.lower() == song_name.lower()]
    return match.to_dict("records")

def random_song():
    return df.sample(1).to_dict("records")

# --- Artists ---

def get_artists():
    return sorted(df["artist_name"].unique().tolist())

def get_artist_songs(artist):
    match = df[df["artist_name"].str.lower() == artist.lower()]
    return match.to_dict("records")

# --- Albums ---

def get_albums():
    return sorted(df["album_name"].unique().tolist())

def get_album(album):
    match = df[df["album_name"].str.lower() == album.lower()]
    return match.to_dict("records")

# --- Discovery & Search ---

def top_tracks(limit=10):
    top = df.sort_values("track_popularity", ascending=False)
    return top.head(limit).to_dict("records")

def top_artists(limit=10):
    top = df.sort_values("artist_popularity", ascending=False).drop_duplicates("artist_name")
    return top.head(limit)[["artist_name", "artist_popularity"]].to_dict("records")

def search(keyword):
    results = df[df["track_name"].str.contains(keyword, case=False, na=False)]
    return results.to_dict("records")

# --- Analytics ---

def stats():
    return {
        "total_songs": len(df),
        "total_artists": df["artist_name"].nunique(),
        "total_albums": df["album_name"].nunique(),
        "album_types": df["album_type"].nunique()
    }