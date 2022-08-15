import json
import matplotlib.pyplot as plt
import os
import numpy as np
from scipy.signal import savgol_filter
from datafetcher import get_bbox_size_IBP, get_diff_IBP, get_stats_IBP

def plot_hist(diff):
    plt.hist(diff, bins=20)
    plt.xlabel('Difference IBP [px]')
    plt.ylabel('Number of frames IBP')
    plt.title('Histogram of differences between adjacent frames IBP')
    plt.show()

def smooth_plot(bbox_size):
    yhat = savgol_filter(bbox_size, 51, 3)
    plt.plot(yhat)
    plt.legend()
    plt.xlabel('Frame IBP')
    plt.ylabel('Bbox size IBP [px]')
    plt.title('Bbox size IBP')
    plt.show()

def main():
    json_files = os.listdir('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/')
    bbox_size = []
    for json_file in json_files:
        bbox_size.extend(get_bbox_size_IBP('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/' + json_file))
    diff = get_diff_IBP(bbox_size)
    mean, std = get_stats_IBP(diff)
    print('Mean:', mean)
    print('Standard deviation:', std)
    plot_hist(diff)
    smooth_plot(bbox_size)

if __name__ == '__main__':
    main()