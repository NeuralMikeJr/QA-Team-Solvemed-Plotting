import json
import matplotlib.pyplot as plt
import os
import numpy as np
from datafetcher import get_bbox_size_IBI, get_diff_IBI, get_stats_IBI

def plot_bbox_size(bbox_size):
    plt.plot(bbox_size)
    plt.xlabel('Frame IBI')
    plt.ylabel('Bbox size IBI [px]')
    plt.title('Bbox size IBI')
    plt.show()

def plot_diff(diff):
    plt.plot(diff)
    plt.xlabel('Frame IBI')
    plt.ylabel('Difference IBI [px]')
    plt.title('Difference between adjacent frames IBI')
    plt.show()

def plot_hist(diff):
    plt.hist(diff, bins=20)
    plt.xlabel('Difference IBI [px]')
    plt.ylabel('Number of frames IBI')
    plt.title('Histogram of differences between adjacent frames IBI')
    plt.show()

def main():
    json_files = os.listdir('C:/Users/48795/Documents/Solvemed/Annotations/14-07-2022/14-07-2022/')
    bbox_size = []
    for json_file in json_files:
        bbox_size.extend(get_bbox_size_IBI('C:/Users/48795/Documents/Solvemed/Annotations/14-07-2022/14-07-2022/' + json_file))
    diff = get_diff_IBI(bbox_size)
    mean, std = get_stats_IBI(diff)
    print('Mean:', mean)
    print('Standard deviation:', std)
    plot_bbox_size(bbox_size)
    plot_diff(diff)
    plot_hist(diff)

if __name__ == '__main__':
    main()