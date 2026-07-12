import pandas as pd

"""
This is how we got the min and max data of each numerical columns
print(df.select_dtypes(include="number").min())
print("-----------------------------------------")
print(df.select_dtypes(include="number").max())
"""

class Song:
    def __init__(self, track_id, artists, album_name, track_name, popularity, duration_ms, explicit, danceability, energy, key, loudness, mode, speechiness, acousiticness, instrumentalness, liveness, valence, tempo, time_signature, track_genre):
        self.__track_id = track_id
        self.__artists = artists
        self.__album_name = album_name
        self.__track_name = track_name
        self.__popularity = popularity
        self.__duration_ms = duration_ms
        self.__explicit = explicit
        self.__danceability = danceability
        self.__energy = energy
        self.__key = key
        self.__loudness = loudness
        self.__mode = mode
        self.__speechiness = speechiness
        self.__acousiticness = acousiticness
        self.__instrumentalness = instrumentalness
        self.__liveness = liveness
        self.__valence = valence
        self.__tempo = tempo
        self.__time_signature = time_signature
        self.__track_genre = track_genre
        
    def set_popularity(self, popularity):
        if(popularity>=0 and popularity <= 100) :
            self.__popularity = popularity
        else:
            raise ValueError("Popularity must be between 0 and 100.")
            
    def set_danceability(self, danceability):
        if(danceability>=0 and danceability<=1):
            self.__danceability = danceability
        else:
            raise ValueError("Danceability must be between 0 and 1.")
            
    def set_energy(self, energy):
        if(energy>=0 and energy<=1):
            self.__energy = energy
        else:
            raise ValueError("Energy must be between 0 and 1.")
            
    def set_mode(self, mode):
        if(mode >=0 and mode <=1):
            self.__mode = mode
        else:
            raise ValueError("Mode must be between 0 and 1.")
            
    def set_speechness(self,speechiness):
        if(speechiness>=0 and speechiness<=1):
            self.__speechiness = speechiness
        else:
            raise ValueError("Speechiness must be between 0 and 1.")
    
    def set_acousticness(self, acousiticness):
        if(acousiticness>=0 and acousiticness<=1):
            self.__acousiticness = acousiticness
        else:
            raise ValueError("Acousticness must be between 0 and 1.")
            
    def set_instrumentalness(self, instrumentalness):
        if(instrumentalness>=0 and instrumentalness<=1):
            self.__instrumentalness = instrumentalness
        else:
            raise ValueError("Instrumentalness must be between 0 and 1.")
    
    def set_liveness(self, liveness):
        if(liveness >= 0 and liveness<=1):
            self.__liveness = liveness
        else:
            raise ValueError("Liveness must be between 0 and 1.")
    
    def set_valence(self, valence):
        if(valence>=0 and valence<=1):
            self.__valence = valence
        else:
            raise ValueError("Valence must be between 0 and 1.")
    
    def set_time_signature(self, time_signature):
        if(time_signature>=0 and time_signature<=5):
            self.__time_signature = time_signature
        else:
            raise ValueError("Time_signature must be between 0 and 5.")
        
    
    @classmethod
    def appand_song(cls, track_id, artists, album_name, track_name, popularity, duration_ms, explicit, danceability, energy, key, loudness, mode, speechiness, acousiticness, instrumentalness, liveness, valence, tempo, time_signature, track_genre, df):
        
        if explicit == "false" or explicit == "False":
            explicit = False
        else:
            explicit = True

        new_row = {"Unnamed: 0" : len(df),
                   "track_id" : track_id,
                   "artists" : artists,
                   "album_name" : album_name,
                   "track_name" : track_name,
                   "popularity" : int(popularity),
                   "duration_ms" : int(duration_ms),
                   "explicit" : bool(explicit),
                   "danceability" : float(danceability),
                   "energy" : float(energy),
                   "key" : int(key),
                   "loudness" : float(loudness), 
                   "mode" : int(mode),
                   "speechiness" : float(speechiness),
                   "acousiticness" : float(acousiticness),
                   "instrumentalness" : float(instrumentalness),
                   "liveness" : float(liveness),
                   "valence" : float(valence),
                   "tempo" : float(tempo),
                   "time_signature" : int(time_signature),
                   "track_genre" : track_genre 
                   }
        
        df.loc[len(df)] = new_row
       
        pd.DataFrame([new_row]).to_csv("data/spotify_tracks.csv",mode="a",header=False,index=False)
        
        return cls(track_id, artists, album_name, track_name, int(popularity), int(duration_ms), bool(explicit), float(danceability), float(energy), int(key), float(loudness), int(mode), float(speechiness), float(acousiticness), float(instrumentalness), float(liveness), float(valence), float(tempo), int(time_signature), track_genre)
   
    
   
    
   
    
   
    
   
    
   
    