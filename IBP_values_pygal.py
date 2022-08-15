import json
import pygal
import os
import numpy as np
from scipy.signal import savgol_filter

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
        diff.append(abs(bbox_size[i+1] - bbox_size[i]))
    return diff

def get_stats(diff):
    mean = np.mean(diff)
    std = np.std(diff)
    return mean, std

def plot_hist(diff):
    hist = pygal.Histogram()
    hist.add('Difference IBP [px]', diff)
    hist.render_to_file('histogram.svg')

def smooth_plot(bbox_size):
    yhat = savgol_filter(bbox_size, 51, 3)
    line_chart = pygal.Line()
    line_chart.title = 'Bbox size IBP'
    line_chart.x_labels = map(str, range(len(bbox_size)))
    line_chart.add('Bbox size IBP [px]', yhat)
    line_chart.render_to_file('line_chart.svg')

def main():
    json_files = os.listdir('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/')
    bbox_size = []
    for json_file in json_files:
        bbox_size.extend(get_bbox_size('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/' + json_file))
    diff = get_diff(bbox_size)
    mean, std = get_stats(diff)
    print('Mean:', mean)
    print('Standard deviation:', std)
    plot_hist(diff)
    smooth_plot(bbox_size)

if __name__ == '__main__':
    main()