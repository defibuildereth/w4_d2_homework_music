from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        artist = Artist(row['name'], row['id'])
    return artist


def albums(artist):
    albums = []
    id = artist.id
    sql = "SELECT * FROM albums WHERE artist_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for row in results:
        album = Album(row['title'], row['genre'], artist)
        albums.append(album)
    return albums

def select_all():
    sql = "SELECT * FROM artists"
    return run_sql(sql)

def delete(id):
    pass

def update(artist):
    pass
