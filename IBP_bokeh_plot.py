import json
import os
import numpy as np
from scipy.signal import savgol_filter
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool
from datafetcher import get_bbox_size_IBP, get_diff_IBP, get_stats_IBP

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
    output_file('diff.html')
    p = figure(plot_width=800, plot_height=400, title='Difference between adjacent frames IBP',
               x_axis_label='Frame IBP', y_axis_label='Difference IBP [px]')
    p.line(x=list(range(len(diff))), y=diff, line_width=2)
    show(p)

def plot_hist(diff):
    output_file('hist.html')
    p = figure(plot_width=800, plot_height=400, title='Histogram of differences between adjacent frames IBP',
               x_axis_label='Difference IBP [px]', y_axis_label='Number of frames IBP')
    p.quad(top=diff, bottom=0, left=list(range(len(diff))), right=list(range(1, len(diff)+1)),
           fill_color='red', line_color='black')
    show(p)

def smooth_plot(bbox_size):
    yhat = savgol_filter(bbox_size, 51, 3)
    output_file('smooth.html')
    p = figure(plot_width=800, plot_height=400, title='Bbox size IBP',
               x_axis_label='Frame IBP', y_axis_label='Bbox size IBP [px]')
    p.line(x=list(range(len(yhat))), y=yhat, line_width=2)
    show(p)

def main():
    json_files = os.listdir('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/')
    bbox_size = []
    for json_file in json_files:
        bbox_size.extend(get_bbox_size_IBP('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/' + json_file))
    diff = get_diff_IBP(bbox_size)
    mean, std = get_stats_IBP(diff)
    print('Mean:', mean)
    print('Standard deviation:', std)
    plot_diff(diff)
    plot_hist(diff)
    smooth_plot(bbox_size)

if __name__ == '__main__':
    main()