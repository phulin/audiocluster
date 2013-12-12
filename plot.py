import json
import os
import numpy as np
import matplotlib.pyplot as plt
from mutagen.mp3 import EasyMP3
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import Normalize
import matplotlib

matplotlib.rc('font', size=16)

data = np.load('log.npy')
songs = json.load(open('songs.json'))

def year(song):
    mp3 = EasyMP3(os.path.join('mp3', song[:-8] + '.mp3'))
    return int(mp3.tags['date'][0])

years = np.load('years.npy')
normed_years = Normalize()(years)
clusters = np.load('clusters.npy')

def annot(axis):
    for i in range(len(data)):
        plt.annotate(songs[i][0:3], (data[i][0], data[i][axis]))

def plot():
    plt.show()

def graph_0vs(axis):
    plt.cla()
    plt.scatter(data[:,0], data[:,axis])
    plt.xlabel('Component 0')
    plt.ylabel('Component ' + str(axis))
    plt.savefig('0-' + str(axis) + '.pdf', backend='pdf')

def graph_years():
    plt.cla()
    plt.hist(years, 55, color='green')
    plt.xlabel('Year')
    plt.ylabel('Number of songs')
    plt.gca().set_xlim(1945, 2005)
    plt.gca().set_ylim(0,40)
    plt.savefig('years.pdf', backend='pdf')

def graph_time(times):
    plt.cla()
    plt.plot(times[0], label='0')
    plt.plot(times[1], label='1')
    plt.plot(times[2], label='2')
    plt.legend()
    plt.gca().set_xlim(-30, 1054)
    plt.xlabel('Sample point')
    plt.ylabel('Weight')
    plt.savefig('time_priorities.pdf', backend='pdf')


def graph_freqs(pt):
    x = np.arange(0, 22050, 22050. / 2048)
    plt.cla()
    plt.plot(x, pt[0], label='0')
    plt.plot(x, -pt[1], label='1')
    plt.plot(x, pt[2], label='2')
    plt.legend()
    plt.gca().set_xlim(x[0], x[-1])
    plt.xlabel('Frequency')
    plt.ylabel('Weight')
    plt.savefig('pca_freqs.pdf', backend='pdf')

def graph_clusters():
    plt.cla()
    plt.scatter(data[:,0], data[:,1], c=clusters, cmap='cool')
    plt.xlabel('Component 0')
    plt.ylabel('Component 1')
    plt.savefig('clusters.pdf', backend='pdf')
>>>>>>> Stashed changes
