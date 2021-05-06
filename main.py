import sqlalchemy

engine = sqlalchemy.create_engine('postgresql://postgres:1234@localhost:5432/Music_Website')

connection = engine.connect()

genres = ['Pop', 'Rock', 'Blues', 'Electronic', 'Folk', 'Alternative', 'Hip-Hop', 'House', 'Latin']
performers = ['Kaleo', 'Luis Fonsi', 'Ed Sheeran', 'Jax Jones', 'The Weeknd', 'Charlie Puth', 'Dua Lipa', 'Hozier']
albums = {
    'Kaleo':2013, 'VIDA':2019, 'No.6 Collaborations Project':2019, 'Snacks':2018,
    'After Hours':2020, 'Nine Track Mind':2016, 'Dua Lipa':2017, 'Hozier':2015
          }
#tracks = {name:[duration, album_id]}
tracks = {
    'Ísland Er Land Þitt':['00:01:17', 1], 'Glass House':['00:04:16', 1], 'Rock "N" Roller':['00:04:05', 1], 'Pour Sugar On Me':['00:02:47', 1],
    'Sola':['00:03:25', 2], 'Apaga La Luz':['00:03:32', 2], 'Le Pido Al Cielo':['00:04:08', 2], 'Poco A Poco':['00:02:56', 2],
    'Beautiful People':['00:03:18', 3], 'Cross Me':['00:03:26', 3], 'South of the Border':['00:03:25', 3], 'Feels':['00:02:31', 3],
    'Ring Ring':['00:03:40', 4], 'Breathe':['00:03:30', 4], 'House Work':['00:02:39', 4],
    'In Your Eyes':['00:03:57', 5], 'After Hours':['00:06:02', 5], 'Alone Again':['00:04:10', 5], 'Repeat After Me':['00:03:16', 5],
    'One Call Away':['00:04:14', 6], 'Dangerously':['00:03:19', 6], 'Losing My Mind':['00:03:32', 6], 'Up All Night':['00:03:10', 6],
    'Hotter Than Hell':['00:03:08', 7], 'Be The One':['00:03:22', 7], 'IDGAF':['00:03:38', 7], 'Genesis':['00:03:25', 7],
    'Take Me To Church':['00:04:02', 8], 'Jackie And Wilson':['00:04:43', 8], 'Someone New':['00:03:43', 8], 'To Be Alone':['00:05:24', 8]
         }
collections = {
    'Collection1':2015, 'Collection2':2016, 'Collection3':2017, 'Collection4':2017,
    'Collection5':2018,'Collection6':2019, 'Collection7':2020, 'Collection8':2020
               }
#performers_genres = performer_id:[genre_id]
performers_genres = {1:[2, 3, 6], 2:[1, 9], 3:[7], 4:[8], 5:[1, 4], 6:[1], 7:[1, 8], 8:[3, 5]}
#performers_albums = {performer_id:album_id}
performers_albums = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8}
#collections_tracks = {collection_id:[track_id]}
collections_tracks = {
    1:[1, 5, 10, 14, 18], 2:[3, 6, 9, 12, 15], 3:[8, 11, 16, 21, 29], 4:[10, 12, 17, 21, 30],
    5:[4, 12, 17, 20, 22], 6:[2, 4, 13, 19, 23], 7:[2, 7, 8, 18, 24, 31], 8:[1, 4, 8, 10, 25, 26 ]
                    }


def Add_genre_to_table(genre):
    for i in genre:
        ins = connection.execute(f"""INSERT INTO Genre(name) VALUES('{i}');""")
    return ins


def Add_performer_to_table(performers):
    for i in performers:
        ins = connection.execute(f"""INSERT INTO Performer(name) VALUES('{i}');""")
    return ins


def Add_album_to_table(albums):
    for name, year in albums.items():
        ins = connection.execute(f"""INSERT INTO Album(name, year) VALUES('{name}', {year});""")
    return ins


def Add_track_to_table(tracks):
    for name, duration_albumID in tracks.items():
        ins = connection.execute(f"""INSERT INTO Track(name, duration, album_id)
         VALUES('{name}', '{duration_albumID[0]}', '{duration_albumID[1]}');""")
    return ins


def Add_collection_to_table(collections):
    for name, year in collections.items():
        ins = connection.execute(f"""INSERT INTO Collection(name, year)
         VALUES('{name}', {year});""")
    return ins


def Add_performer_genre_to_table(performers_genres):
    for performer_id, genre_id_lst in performers_genres.items():
        for i in range(len(genre_id_lst)):
            ins = connection.execute(f"""INSERT INTO GenrePerformer(genre_id, performer_id)
            VALUES({genre_id_lst[i]}, {performer_id});""")
    return ins


def Add_performer_album_to_table(performers_albums):
    for performer_id, album_id in performers_albums.items():
        ins = connection.execute(f"""INSERT INTO PerformerAlbum(performer_id, album_id)
        VALUES({performer_id}, {album_id});""")
    return ins


def Add_collection_track_to_table(collections_tracks):
    for collection_id, track_id_lst in collections_tracks.items():
        for i in range(len(track_id_lst)):
            ins = connection.execute(f"""INSERT INTO CollectionTrack(collection_id, track_id)
            VALUES({collection_id}, {track_id_lst[i]});""")
    return ins


Add_genre_to_table(genres)
Add_performer_to_table(performers)
Add_album_to_table(albums)
Add_track_to_table(tracks)
Add_collection_to_table(collections)
Add_performer_genre_to_table(performers_genres)
Add_performer_album_to_table(performers_albums)
Add_collection_track_to_table(collections_tracks)

