import json
import matplotlib.pyplot as plt
import os
import numpy as np
from datafetcher import get_bbox_size_EBI, get_diff_EBI, get_stats_EBI

def plot_bbox_size_EBI(bbox_size):
    plt.plot(bbox_size)
    plt.xlabel('Frame EBI')
    plt.ylabel('Bbox size EBI [px]')
    plt.title('Bbox size EBI')
    plt.show()

def plot_diff_EBI(diff):
    plt.plot(diff)
    plt.xlabel('Frame EBI')
    plt.ylabel('Difference EBI [px]')
    plt.title('Difference between adjacent frames EBI')
    plt.show()

def plot_hist_EBI(diff):
    plt.hist(diff, bins=20)
    plt.xlabel('Difference EBI [px]')
    plt.ylabel('Number of frames EBI')
    plt.title('Histogram of differences between adjacent frames EBI')
    plt.show()

def main():
    json_files = os.listdir('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/')
    bbox_size = []
    for json_file in json_files:
        bbox_size.extend(get_bbox_size('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/' + json_file))
    diff = get_diff_EBI(bbox_size)
    mean, std = get_stats_EBI(diff)
    print('Mean:', mean)
    print('Standard deviation:', std)
    plot_bbox_size_EBI(bbox_size)
    plot_diff_EBI(diff)
    plot_hist_EBI(diff)

if __name__ == '__main__':
    main()