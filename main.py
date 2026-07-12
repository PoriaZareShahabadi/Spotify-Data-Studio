import pandas as pd
import platform
import os
import sys
import time
from src import data_loader
from src import data_cleaner
from src import data_visualizer

def clearTerminal():
    os_name = platform.system()
    if(os_name == "Linux"):
        os.system("clear")
    else:
        os.system("cls")

def print_heads():
    print("=============================       Spotify Data  Studio & Management System       =============================")
    print("1. Load Dataset & View Missing Values Report")
    print("2. Clean Missing Values (Mean / Median / KNN)")
    print("3. Handle Outliers (IQR / Z-score)")
    print("4. Add a New Song to the Dataset (Interactive Input")
    print("5. Calculate Genre Insights & Correlation Matrix")
    print("6. Generate Advanced Visualizations (Plots)")
    print("7. Exit")
    print("================================================================================================================")
    print("Enter your choice (1-7): ")

loaded_data_frame = False
way_of_handling = None
had_been_handled_outliers = False
had_been_cleaned = False
numeric_properties = ["popularity","duration_ms","danceability","energy","key","loudness","mode","speechiness","acousticness","instrumentalness","liveness","valence","tempo","time_signature"]
run = True
while(run) :
    print_heads()
    accepted_n = False
    n = input().strip()
    if(n.isdigit()):
        n = int(n)
        if(n>=1 and n<=7):
            accepted_n = True
    while(not accepted_n):
        print("Please enter a valid number: ", flush=True)
        n = input().strip()
        if(n.isdigit()):
            n = int(n)
            if(n>=1 and n<=7):
                accepted_n = True
    if(n == 1):
        loaded_data_frame = True
        clearTerminal()
        # loading dataset
        print("Loading Dataset ",end="", flush=True)
        time.sleep(1)
        print(".",end="", flush=True)
        os_name = platform.system()
        if(os_name == "Linux"):
            df = pd.read_csv('data/spotify_tracks.csv')
        else:
            df = pd.read_csv('data\spotify_tracks.csv')
        properties = df.columns.tolist()
        properties = properties[1:]
        normalized_df = df.copy()
        for column in numeric_properties:
            minimum = df[column].min()
            maximum = df[column].max()

            if maximum != minimum:
                normalized_df[column] = (df[column] - minimum) / (maximum - minimum)
        # creating instances (Song class) from dataframe
        for i in range(len(df)):
            if(i == len(df) // 3):
                print(".",end="", flush=True)
            elif(i == 2 * (len(df) // 3)):
                print(".", flush=True)
            row = df.iloc[i]
            track_id = row["track_id"]
            artists = row["artists"]
            album_name = row["album_name"]
            track_name = row["track_name"]
            popularity = row["popularity"]
            duration_ms = row["duration_ms"]
            explicit = row["explicit"]
            danceability = row["danceability"]
            energy = row["energy"]
            key = row["key"]
            loudness = row["loudness"]
            mode = row["mode"]
            speechiness = row["speechiness"]
            acousticness = row["acousticness"]
            instrumentalness = row["instrumentalness"]
            liveness = row["liveness"]
            valence = row["valence"]
            tempo = row["tempo"]
            time_signature = row["time_signature"]
            track_genre = row["track_genre"]
            try :
                track_id = data_loader.Song(track_id, artists, album_name, track_name, popularity, duration_ms, explicit, danceability, energy, key, loudness, mode, speechiness, acousticness , instrumentalness, liveness, valence, tempo, time_signature, track_genre)
            except ValueError as e:
                print(f"Song number {i} with the track id of {track_id}: {e}", flush=True)
        # missing values report
        print("Finding Missing Values ", end="", flush=True)
        time.sleep(1)
        print(".",end="", flush=True)
        count_of_missing_values = 0
        list_of_rows_with_missing_values = []
        for i in range(len(df)):
            if(i == len(df) // 3):
                print(".",end="",flush=True)
            elif(i == 2 * (len(df) // 3)):
                print(".", flush=True)
            row = df.iloc[i]
            if row.isna().any():
                list_of_rows_with_missing_values.append(i)
            count_of_missing_values += row.isna().sum()
        for i in list_of_rows_with_missing_values:
            row = df.iloc[i]
            print(f"Song number {i} with track id of {row['track_id']} has a(more) missing value(s).",flush=True)
        print(f"Total number of missing values are {count_of_missing_values}", flush=True)
        input("Please Enter to continue ...")
    elif(n == 2):
        if(loaded_data_frame):
            clearTerminal()
            m = int(input("Please enter a way of cleaning missing values (Mean[1], Median[2], Knn[3]): ").strip())
            while(m < 1 and m > 3):
                m = int(input("please enter a valid number: ").strip())
            # cleaning missing values using mean
            if(m == 1):
                mean_imputer = data_cleaner.MeanImputer()
                mean_imputer.impute(df,numeric_properties)
                df.to_csv("data/spotify_tracks.csv", index=False)
                print("Done!", flush=True)
                time.sleep(2)
            # cleaning missing values using median
            elif(m == 2):
                median_imputer = data_cleaner.MedianImputer()
                median_imputer.impute(df,numeric_properties)
                df.to_csv("data/spotify_tracks.csv", index=False)
                print("Done!", flush=True)
                time.sleep(2)
            # cleaning missing values using knn
            elif(m == 3):
                knn_imputer = data_cleaner.KNNImputer()
                knn_imputer.impute(df,numeric_properties)
                df.to_csv("data/spotify_tracks.csv", index=False)
                print("Done!", flush=True)
                time.sleep(2)
            # filling the string type missing values
            print("Filling the string type missing values", flush=True)
            time.sleep(1)
            for column in df.columns:
                missing_rows = df[df[column].isna()].index
                for row in missing_rows:
                    value = input(f"Song {row} with property {column} has a missing value.\nPlease enter a value for it: ")
                    df.at[row, column] = value
                    df.to_csv("data/spotify_tracks.csv", index = False)
        else:
            print("You didn't load the Dataset! Please first load the Dataset.", flush=True)
            time.sleep(5)
            clearTerminal()
            continue
    elif(n == 3):
        if(loaded_data_frame and had_been_cleaned):
            numeric_properties = ["popularity","duration_ms","danceability","energy","key","loudness","mode","speechiness","acousticness","instrumentalness","liveness","valence","tempo","time_signature"]
            clearTerminal()
            m = int(input("Please enter a way of handling outliers (IQR[1], Z-Score[2]): ").strip())
            while(m < 1 and m > 2):
                m = int(input("please enter a valid number: ").strip())
            # handle outliers with IQR
            if(m == 1):
                had_been_handled_outliers = True
                way_of_handling = "IQR"
                iqroutliershandler = data_cleaner.IQROutlierHandler()
                df = iqroutliershandler.handle(df,numeric_properties)
                df.to_csv("data/spotify_tracks.csv", index=False)
                print("Done!", flush=True)
                time.sleep(1)
            # handle outliers with Z-score
            elif(m == 2):
                had_been_handled_outliers = True
                way_of_handling = "Z-Score"
                zscoreoutliershandler = data_cleaner.ZScoreOutlierHandler()
                df = zscoreoutliershandler.handle(df,numeric_properties)
                df.to_csv("data/spotify_tracks.csv", index=False)
                print("Done!", flush=True)
                time.sleep(1)
        else:
            if(not loaded_data_frame):
                print("You didn't load the Dataset! Please first load the Dataset.", flush=True)
                time.sleep(3)    
                clearTerminal() 
                continue 
            else:
                print("You didn't clean the Dataframe! Please first clean the data.", flush=True)
                time.sleep(3)
                clearTerminal()
                continue
    elif(n == 4):
        if(loaded_data_frame):
            clearTerminal()
            print("Please enter the properties of the new song:", flush=True)
            # Adding a new song
            track_id = input("Track_id: ")
            artists = input("Artists: ")
            album_name = input("Album_name: ")
            track_name = input("Track_name: ")
            popularity = input("Popularity: (0-100) ")
            duration_ms = input("Duration_ms: ")
            explicit = input("Explicit: [false, true] ")
            danceability = input("Danceability: (0-1) ")
            energy = input("Energy: (0-1) ")
            key = input("Key: ")
            loudness = input("Loudness: ")
            mode = input("Mode: (0-1) ")
            speechiness = input("Speechiness: (0-1) ")
            acousiticness = input("Acousticness: (0-1) ")
            instrumentalness = input("Instrumentalness: (0-1) ")
            liveness = input("Liveness: (0-1) ")
            valence = input("Valence: (0-1) ")
            tempo = input("Tempo:")
            time_signature = input("Time_signature: (0-5) ")
            track_genre = input("Track_genre: ")
            try:
                data_loader.Song.appand_song(track_id, artists, album_name, track_name, popularity, duration_ms, explicit, danceability, energy, key, loudness, mode, speechiness, acousiticness, instrumentalness, liveness, valence, tempo, time_signature, track_genre, df)
                print("Adding the new song ",end="",flush=True)
                time.sleep(1)
                print(".",end="",flush=True)
                time.sleep(1)
                print(".",end="",flush=True)
                time.sleep(1)
                print(".",flush=True)
                time.sleep(1)
                print("Done!",flush=True)
                time.sleep(0.5)
            except ValueError as e:
                print(e,flush=True)
                time.sleep(5)
        else:
            print("You didn't load the Dataset! Please first load the Dataset.",flush=True)
            time.sleep(5)
            clearTerminal()
            continue
    elif(n == 5):
        if(loaded_data_frame):
            clearTerminal()
            data_visualizer.draw_heatmap_plot()
        else:
            print("You didn't load the Dataset! Please first load the Dataset.", flush=True)
            time.sleep(5)
            clearTerminal()
            continue
    elif(n == 6):
        if(loaded_data_frame):
            clearTerminal()
            m = int(input("What plot would you like to have ? (Scatter[1], Box[2], Spider[3]) "))
            while(m<1 and m>3):
                m = int(input("Please eneter a valid number: "))
            # Scatter plot
            if(m == 1):
                clearTerminal()
                property_one = input("Please enter a valid property: ")
                property_one = property_one.lower()
                property_two = input("Please enter a valid property: ")
                property_two = property_two.lower()
                data_visualizer.draw_scatter_plot(normalized_df, property_one, property_two)
            # Box plot
            elif(m == 2):
                clearTerminal()
                property = input("Please enter a valid property: ")
                property = property.lower()
                data_visualizer.draw_box_plot(property, had_been_handled_outliers, way_of_handling)
            # Spider
            elif(m == 3):
                clearTerminal()
                properties_used = input("Please enter properties you want to be used seperated by spaces: ").split()
                genre = input("Please enter your genre: ").lower()
                data_visualizer.draw_spider_plot(properties_used, genre)
        else:
            print("You didn't load the Dataset! Please first load the Dataset.", flush=True)
            time.sleep(5)
            clearTerminal()
            continue
    elif(n == 7):
        sys.exit(0)
    
    
    clearTerminal()