import numpy as np
import os
import scipy.io.wavfile as wav

samples_list = list()

for _, _, filenames in os.walk('wav'):
    for song in filenames:
        rlsamples = wav.read(os.path.join('wav', song), True)[1]
        channels = rlsamples.transpose()
        samples = (rlsamples[0] + rlsamples[1]) / 2
        samples_list += [samples]

all_samples = np.vstack(samples_list)
