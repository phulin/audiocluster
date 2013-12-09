#!/usr/local/bin/python
import numpy as np
import os
import scipy.signal as signal
import scipy.fftpack as fftpack
import scipy.io.wavfile as wav
import sys

# feature rep length = num_windows * window_size
num_windows = 1024
window_size = 2048
window = signal.hann(window_size)

# outer loop is dummy
for _, _, filenames in os.walk('wav'):
    for song in filenames:
        result_path = os.path.join('features', song) + '.npy'
        if os.path.exists(result_path):
            print "skipping " + song
            sys.stdout.flush()
            continue
        print "processing " + song
        rlsamples = wav.read(os.path.join('wav', song))[1]
        channels = rlsamples.transpose()
        samples = (channels[0] + channels[1]) / 2
        freqs_list = list()

        try:
            window_interval = (samples.size - window_size) / num_windows
            for i in range(num_windows):
                start = i * window_interval
                end = start + window_size
                freqs_list.append(fftpack.rfft(samples[start:end] * window))

            np.save(result_path, np.vstack(freqs_list))
        except:
            print "error - skipping " + song
