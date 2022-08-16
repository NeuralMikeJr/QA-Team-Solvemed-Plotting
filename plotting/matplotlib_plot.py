import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

def plot_hist(diff):
    plt.hist(diff, bins=20)
    plt.xlabel('Difference [px]')
    plt.ylabel('Number of frames')
    plt.title('Histogram of differences between adjacent frames')
    plt.show()

def smooth_plot(bbox_size):
    yhat = savgol_filter(bbox_size, 51, 3)
    plt.plot(yhat)
    plt.legend()
    plt.xlabel('Frame')
    plt.ylabel('Bbox size [px]')
    plt.title('Bbox size')
    plt.show()