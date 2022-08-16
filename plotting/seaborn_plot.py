import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import savgol_filter
import seaborn as sns

def plot_hist(diff):
    sns.distplot(diff, bins=20)
    plt.xlabel('Difference [px]')
    plt.ylabel('Number of frames')
    plt.title('Histogram of differences between adjacent frames')
    plt.show()

def smooth_plot(bbox_size):
    yhat = savgol_filter(bbox_size, 51, 3)
    sns.lineplot(x=range(len(yhat)), y=yhat)
    plt.legend()
    plt.xlabel('Frame')
    plt.ylabel('Bbox size [px]')
    plt.title('Bbox size')
    plt.show()