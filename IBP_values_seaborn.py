import json
import matplotlib.pyplot as plt
import os
import numpy as np
from scipy.signal import savgol_filter
import seaborn as sns

def get_bbox_size(json_file):
    with open(json_file) as f:
        data = json.load(f)
    bbox_size = []
    for i in range(len(data)):
        for j in range(len(data[i]['annotations'])):
            if data[i]['annotations'][j]['label'] == 'IBP':
                bbox_size.append(data[i]['annotations'][j]['coordinates']['width'] * data[i]['annotations'][j]['coordinates']['height'])
                # print(bbox_size)
    return bbox_size

def get_diff(bbox_size):
    diff = []
    for i in range(len(bbox_size)-1):
        diff.append(bbox_size[i+1] - bbox_size[i])
    return diff

def get_stats(diff):
    mean = np.mean(diff)
    std = np.std(diff)
    return mean, std

def plot_diff(diff):
    sns.lineplot(x=range(len(diff)), y=diff)
    plt.xlabel('Frame IBP')
    plt.ylabel('Difference IBP [px]')
    plt.title('Difference between adjacent frames IBP')
    plt.show()

def plot_hist(diff):
    sns.distplot(diff, bins=20)
    plt.xlabel('Difference IBP [px]')
    plt.ylabel('Number of frames IBP')
    plt.title('Histogram of differences between adjacent frames IBP')
    plt.show()

def smooth_plot(bbox_size):
    yhat = savgol_filter(bbox_size, 51, 3)
    sns.lineplot(x=range(len(yhat)), y=yhat)
    plt.legend()
    plt.xlabel('Frame IBP')
    plt.ylabel('Bbox size IBP [px]')
    plt.title('Bbox size IBP')
    plt.show()

def main():
    json_files = os.listdir('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/')
    bbox_size = []
    for json_file in json_files:
        bbox_size.extend(get_bbox_size('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/' + json_file))
    diff = get_diff(bbox_size)
    mean, std = get_stats(diff)
    print('Mean:', mean)
    print('Standard deviation:', std)
    plot_diff(diff)
    plot_hist(diff)
    smooth_plot(bbox_size)

if __name__ == '__main__':
    main()