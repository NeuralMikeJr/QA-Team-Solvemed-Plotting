import json
import os
import numpy as np
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool
from datafetcher import get_bbox_size_EBI, get_diff_EBI, get_stats_EBI

def plot_bbox_size(bbox_size):
    output_file('bbox_size.html')
    p = figure(plot_width=800, plot_height=400, title='Bbox size EBI', x_axis_label='Frame EBI', y_axis_label='Bbox size EBI [px]')
    p.line(x=list(range(len(bbox_size))), y=bbox_size, line_width=2)
    show(p)

def plot_diff(diff):
    output_file('diff.html')
    p = figure(plot_width=800, plot_height=400, title='Difference between adjacent frames EBI', x_axis_label='Frame EBI', y_axis_label='Difference EBI [px]')
    p.line(x=list(range(len(diff))), y=diff, line_width=2)
    show(p)

def plot_hist(diff):
    output_file('hist.html')
    p = figure(plot_width=800, plot_height=400, title='Histogram of differences between adjacent frames EBI', x_axis_label='Difference EBI [px]', y_axis_label='Number of frames EBI')
    p.quad(top=diff, bottom=0, left=list(range(len(diff))), right=list(range(1, len(diff)+1)), fill_color='red', line_color='black')
    show(p)

def main():
    json_files = os.listdir('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/')
    bbox_size = []
    for json_file in json_files:
        bbox_size.extend(get_bbox_size_EBI('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/' + json_file))
    diff = get_diff_EBI(bbox_size)
    mean, std = get_stats_EBI(diff)
    print('Mean:', mean)
    print('Standard deviation:', std)
    plot_bbox_size(bbox_size)
    plot_diff(diff)
    plot_hist(diff)

if __name__ == '__main__':
    main()
