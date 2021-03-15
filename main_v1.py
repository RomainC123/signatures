import os
import pathlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.manifold import TSNE

ROOT_PATH = pathlib.Path(__file__).resolve().parent.absolute()
GAUSS_PATH = os.path.join(ROOT_PATH, 'dataset', 'gauss')
if not os.path.exists(GAUSS_PATH):
    raise RuntimeError("Data does not exist, please download it")


df_sig4 = pd.read_csv(os.path.join(GAUSS_PATH, 'Complexity_4G.txt'), delimiter='\t', header=None)
df_sig8 = pd.read_csv(os.path.join(GAUSS_PATH, 'Complexity_8G.txt'), delimiter='\t', header=None)
df_sig24 = pd.read_csv(os.path.join(GAUSS_PATH, 'Complexity_24G.txt'), delimiter='\t', header=None)

list_df = [df_sig4, df_sig8, df_sig24]


def get_labels_tsne(df):

    df_mean = df.mean(axis=1)

    # Getting kmeans labels
    kmeans = KMeans(n_clusters=3, random_state=0)
    kmeans.fit(df_mean.values.reshape(-1, 1))
    kmeans_labels = kmeans.labels_

    # Getting AgglomerativeClustering labels
    ac = AgglomerativeClustering(n_clusters=2, linkage="single")  # Ya mieux à faire ici
    ac_labels = ac.fit_predict(df_mean.values.reshape(-1, 1))

    # Centering and applying TSNE
    df_centered = df - df.mean(axis=0)
    tsne = TSNE(n_components=2, perplexity=50)
    df_tsne = pd.DataFrame(tsne.fit_transform(df_centered))

    # Adding labels to our new dataframe
    df_tsne['kmeans_labels'] = kmeans_labels
    df_tsne['ac_labels'] = ac_labels

    return df_tsne

def get_cluster_report(df, label):
    pass

# Plotting everything with TSNE
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(14, 8))
cols = ['sig4', 'sig8', 'sig24']
rows = ['kmeans', 'AgglomerativeClustering']

for i in range(3):

    df_tsne = get_labels_tsne(list_df[i])

    for j in range(3):
        axes[0, i].scatter(df_tsne.loc[df_tsne['kmeans_labels'] == j].iloc[:, 0], df_tsne.loc[df_tsne['kmeans_labels'] == j].iloc[:, 1])
    for j in range(3):
        axes[1, i].scatter(df_tsne.loc[df_tsne['ac_labels'] == j].iloc[:, 0], df_tsne.loc[df_tsne['ac_labels'] == j].iloc[:, 1])

for ax, col in zip(axes[0], cols):
    ax.set_title(col)

for ax, row in zip(axes[:,0], rows):
    ax.set_ylabel(row, rotation=0, size='large')

# fig.tight_layout()
plt.show()
