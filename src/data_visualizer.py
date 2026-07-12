import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Scatter plot

df = pd.read_csv("./data/spotify_tracks.csv")

def draw_scatter_plot(df,property_one, property_two):
    top10 = df["track_genre"].value_counts().head(10).index
    tracks_in_top10 = df[df["track_genre"].isin(top10)]
    plt.figure(figsize=(10,10))
    for genre in top10:
        tracks_in_top10_in_genre = tracks_in_top10[tracks_in_top10["track_genre"] == genre]
        plt.scatter(tracks_in_top10_in_genre[f"{property_one}"], tracks_in_top10_in_genre[f"{property_two}"], label = genre, alpha=0.6)
    plt.xlabel(f"{property_one}")
    plt.ylabel(f"{property_two}")
    plt.title(f"Scatter plot: {property_one} vs {property_two}")
    plt.legend()
    plt.show()

# Box plot

def draw_box_plot(property, is_it_after, way_of_handling): 
    plt.boxplot(df[f"{property}"])
    if(is_it_after == True) :
        plt.title(f"{property} (After {way_of_handling} Handling)")
    else:
        plt.title(f"{property} (Berfore Handling)")
    plt.ylabel(f"{property}")
    plt.show()

# Heatmap

def draw_heatmap_plot():
    df_without_first_column = df.iloc[:, 1:]
    corr = df_without_first_column.select_dtypes(include="number").corr()
    plt.figure(figsize=(11,10)) 
    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )
    plt.title("Correlation Heatmap")
    plt.show()

# Spider plot

def draw_spider_plot(properties, genre):
    values = df[df["track_genre"] == genre][properties].mean().tolist()
    N = len(properties)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(7,7), subplot_kw=dict(polar=True))
    ax.plot(angles, values, linewidth=2)
    ax.fill(angles, values, alpha=0.25) 
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(properties)
    plt.title(f"{genre} Genre")
    plt.show()

