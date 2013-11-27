#!/usr/local/bin/python
import numpy as np
import os
import matplotlib.pyplot as plt
import sklearn.decomposition

def load(dir, limit = 0):
    features_list = list()
    songs = list()
    count = 0;
    for _, _, filenames in os.walk(dir):
        for song in sorted(filenames, key=lambda s: int(s[0:3])):
            if limit is 0 or count < limit:
                print "loading " + song
                features_list.append(np.load(os.path.join(dir, song)).flatten())
                songs.append(song)
                count += 1
    return songs, np.vstack(features_list)

print "Loading freqs..."
songs, freqs = load('log_features')
pca = sklearn.decomposition.RandomizedPCA(n_components = 3)
print "Fitting..."
pca.fit(freqs)
