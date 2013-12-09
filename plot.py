#!/usr/local/bin/python
import numpy as np
import os
import matplotlib.pyplot as plt

def load(dir, limit = 0):
    features_list = list()
    count = 0;
    for _, _, filenames in os.walk(dir):
        for song in filenames:
            if limit is 0 or count < limit:
                print "loading " + song
                features_list.append(np.load(os.path.join(dir, song)).flatten())
                count += 1
    return np.vstack(features_list)

freqs = load('features', 100)
