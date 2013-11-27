import numpy as np

def freq_priority(num_windows, window_size, pca):
    priorities_list = []
    zeros = np.zeros(1025)
    ones = np.ones(1025)
    comb = np.column_stack([ones] + [zeros] * 2047).flatten()
    components = pca.components_.T
    priorities_list = [np.dot(comb[i:i+1024*2048], components) for i in range(2048)]
    return np.vstack(priorities_list)

def time_priority(pca):
    components = pca.components_.T
    priorities_list = [np.sum(components[2048*i:2048*i+2048], axis=0) for i in range(2048)]
    return np.vstack(priorities_list)
