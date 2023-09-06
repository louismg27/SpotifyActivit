import csv
import json

import requests
import spotipy
import spotipy.util as util
from nbconvert import export
from spotipy import SpotifyOAuth
import sys
from spotipy.oauth2 import SpotifyClientCredentials


# Your Spotify API credentials
client_id = '9c00fda4b776445980799b07289642dc'
client_secret = 'c15da492a84d45c2a5dccf4415728820'
redirect_uri = 'http://localhost:8080'

# Your Spotify username (or Spotify user ID)
username = '312wbujzc5l4mfh73zjqss44djpu'
scope1 = 'user-read-playback-state'
scope2 = 'user-read-recently-played'
scope3 = 'user-read-currently-playing'
scope4 = 'user-modify-playback-state'
scope5 = 'streaming'
scope6 = 'user-library-read'
scope7 = 'user-library-modify'
scope8 = 'playlist-read-private'
scope9 = 'user-read-playback-position'
scope10 = 'user-read-recently-played'
scope11 = 'user-read-playback-position'
scope12 = 'user-top-read'

# Concatena los alcances con espacios en blanco
scope = ' '.join([scope1, scope2, scope3,scope4,scope5,scope6,scope7,scope8,scope9,scope10,scope11,scope12])


token = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)


# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
# else:
#     print("Can't get token for", username)


# Create a Spotify instance with the authentication manager
sp = spotipy.Spotify(auth_manager=token)

###########################################################################
#EJERCICIO 1 ##############################################################
###########################################################################
# Obtiene los 10 artistas más escuchados por el usuario
top_artists = sp.current_user_top_artists(limit=10, time_range='medium_term')
# Imprime la lista de artistas
print("*******************EJERCICIO 1***********************")
print("Los 10 artistas más escuchados por el usuario son:")
top_morelistened=[artist['name'] for artist in top_artists['items']]
for idx, artist_name in enumerate(top_morelistened, start=1):
    print(f"{idx}. {artist_name}")



###########################################################################
#EJERCICIO 2 ##############################################################
###########################################################################
# Crea un conjunto para almacenar los géneros únicos
favorite_genres = set()

# Itera a través de los artistas y obtiene sus géneros musicales
for artist in top_artists['items']:
    artist_info = sp.artist(artist['id'])
    genres = artist_info['genres']
    favorite_genres.update(genres)

# Convierte el conjunto de géneros a una lista y muestra los 5 principales
favorite_genres_list = list(favorite_genres)[:5]

# Imprime los 5 géneros musicales favoritos
print("*******************EJERCICIO 2***********************")
print("Los 5 géneros musicales favoritos del usuario son:")
for idx, genre in enumerate(favorite_genres_list, start=1):
    print(f"{idx}. {genre}")


###########################################################################
#EJERCICIO 3 ##############################################################
###########################################################################
# Obtiene las 10 canciones más escuchadas por el usuario
top_tracks = sp.current_user_top_tracks(limit=10, time_range='medium_term')

# Imprime la lista de las 10 canciones y sus artistas
print("*******************EJERCICIO 3**********************")
print("Las 10 canciones más escuchadas por el usuario son:")

list_topmusic=[{"Cancion": track['name'], "Artista": ", ".join([artist['name'] for artist in track['artists']])} for track in top_tracks['items']]
for idx, track_info in enumerate(list_topmusic, start=1):
    print(f"{idx}. {track_info['Cancion']} - {track_info['Artista']}")



# # ###########################################################################
# # #EJERCICIO 4 ##############################################################
# # ###########################################################################
# # URL de la playlist (reemplaza con la URL de tu playlist)
# playlist_url = 'https://open.spotify.com/playlist/37i9dQZF1DWWGFQLoP9qlv'
#
# # Obtén la información de la playlist
# playlist_id = playlist_url.split('/')[-1]
# playlist_info = sp.playlist(playlist_id)
# print("*******************EJERCICIO 4***********************")
# #1. GUARDAR EN DISCO LA PORTADA DE DICHA PLAYLIST************************
# # Obtiene la URL de la portada de la playlist
# cover_url = playlist_info['images'][0]['url']
#
# #Descarga la portada y guárdala en disco
# response = requests.get(cover_url,timeout=5)
# if response.status_code == 200:
#     with open('playlist_cover.jpg', 'wb') as f:
#         f.write(response.content)
#     print("1. La portada de la playlist se ha guardado en disco como 'playlist_cover.jpg'")
# else:
#     print("No se pudo descargar la portada de la playlist.")
#
# #2. OBTENER EL NUMERO DE FOLLOWERS*************************************
#
# # Extrae el número de seguidores de la playlist
# followers_count = playlist_info['followers']['total']
#
# # Imprime el número de seguidores
# print(f"2. La playlist tiene {followers_count} seguidores.")
#
# #3. OBTENER EL VALOR MEDIO DE LOS SIGUIENTES PARAMETROS DE TODAS SUS CANCIONES
#
# # Obtén la información de la playlist
# playlist_info2 = sp.playlist_tracks(playlist_id)
#
# # Inicializa las variables para los valores medios
# total_tracks = len(playlist_info2)
# tempo_sum = 0
# acousticness_sum = 0
# danceability_sum = 0
# energy_sum = 0
# instrumentalness_sum = 0
# liveness_sum = 0
# loudness_sum = 0
# valence_sum = 0
#
# # Itera a través de las canciones y suma los valores de los parámetros
# for track in playlist_info2['items']:
#     track_info = sp.audio_features(track['track']['id'])[0]
#     tempo_sum += track_info['tempo']
#     acousticness_sum += track_info['acousticness']
#     danceability_sum += track_info['danceability']
#     energy_sum += track_info['energy']
#     instrumentalness_sum += track_info['instrumentalness']
#     liveness_sum += track_info['liveness']
#     loudness_sum += track_info['loudness']
#     valence_sum += track_info['valence']
#
# # Calcula los valores medios
# tempo_avg = tempo_sum / total_tracks
# acousticness_avg = acousticness_sum / total_tracks
# danceability_avg = danceability_sum / total_tracks
# energy_avg = energy_sum / total_tracks
# instrumentalness_avg = instrumentalness_sum / total_tracks
# liveness_avg = liveness_sum / total_tracks
# loudness_avg = loudness_sum / total_tracks
# valence_avg = valence_sum / total_tracks
#
# # Imprime los valores medios
# print("3. Valores medios:")
# print("Valor medio de Tempo (bpm):", tempo_avg)
# print("Valor medio de Acousticness:", acousticness_avg)
# print("Valor medio de Danceability:", danceability_avg)
# print("Valor medio de Energy:", energy_avg)
# print("Valor medio de Instrumentalness:", instrumentalness_avg)
# print("Valor medio de Liveness:", liveness_avg)
# print("Valor medio de Loudness:", loudness_avg)
# print("Valor medio de Valence:", valence_avg)



#EJERCICIO 5
##############################################################
#Todos lso datos deberan guardarse en un fichero o ficheros CSV o JSON para su posterior analisis

# Crear un diccionario con los datos
data = {
    "Top 10 Artistas": top_morelistened,
    "Generos Musicales Favoritos": favorite_genres_list,
    "Top 10 Canciones": list_topmusic,
    # "Número de Seguidores de la Playlist": followers_count,
    # "Valores Medios de Parámetros": {
    #     "Tempo (bpm)": tempo_avg,
    #     "Acousticness": acousticness_avg,
    #     "Danceability": danceability_avg,
    #     "Energy": energy_avg,
    #     "Instrumentalness": instrumentalness_avg,
    #     "Liveness": liveness_avg,
    #     "Loudness": loudness_avg,
    #     "Valence": valence_avg
    # }
}


#Guardar los datos en un archivo JSON
with open('spotify_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent=4)

print("Los datos se han guardado en 'spotify_data.json' en formato JSON.")









#
# import pprint
# import webbrowser
# import pyautogui
# import time
# #
#
#
#
# flag = 0
#
# author = "KAROL G"
# song = "TQG".upper()
#
#
# if len(author)>0:
#     sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id,client_secret))
#     result = sp.search(author)
#     # user_info=sp.current_user()
#
#     for i in range(0,len(result["tracks"]["items"])):
#         name_song = result["tracks"]["items"][i]["name"].upper()
#         if song in name_song:
#             flag = 1
#             webbrowser.open(result["tracks"]["items"][i]["uri"])
#             time.sleep(5)
#             pyautogui.press("enter")
#
# if flag ==0:
#     song = song.replace("","%20")
#     webbrowser.open(f"spotify:search:{song}")
#     time.sleep(5)
#     for i in range(20):
#         pyautogui.press("tab")
#     pyautogui.press("enter")
#
#