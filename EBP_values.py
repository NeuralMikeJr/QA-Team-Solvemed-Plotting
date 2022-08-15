import json
import matplotlib.pyplot as plt
import os
import numpy as np

def get_bbox_size(json_file):
    with open(json_file) as f:
        data = json.load(f)
    bbox_size = []
    for i in range(len(data)):
        for j in range(len(data[i]['annotations'])):
            if data[i]['annotations'][j]['label'] == 'EBP':
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

def plot_bbox_size(bbox_size):
    plt.plot(bbox_size)
    plt.xlabel('Frame EBP')
    plt.ylabel('Bbox size EBP [px]')
    plt.title('Bbox size EBP')
    plt.show()

def plot_diff(diff):
    plt.plot(diff)
    plt.xlabel('Frame EBP')
    plt.ylabel('Difference EBP [px]')
    plt.title('Difference between adjacent frames EBP')
    plt.show()

def plot_hist(diff):
    plt.hist(diff, bins=20)
    plt.xlabel('Difference EBP [px]')
    plt.ylabel('Number of frames EBP')
    plt.title('Histogram of differences between adjacent frames EBP')
    plt.show()

def main():
    json_files = os.listdir('C:/Users/48795/Documents/Solvemed/Annotations/14-07-2022/14-07-2022/')
    bbox_size = []
    for json_file in json_files:
        bbox_size.extend(get_bbox_size('C:/Users/48795/Documents/Solvemed/Annotations/14-07-2022/14-07-2022/' + json_file))
    diff = get_diff(bbox_size)
    mean, std = get_stats(diff)
    print('Mean:', mean)
    print('Standard deviation:', std)
    plot_bbox_size(bbox_size)
    plot_diff(diff)
    plot_hist(diff)

if __name__ == '__main__':
    main()