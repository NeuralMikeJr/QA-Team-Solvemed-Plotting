import numpy as np
from scipy.signal import savgol_filter
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, HoverTool
from datafetcher import get_bbox_size_IBP, get_diff_IBP, get_stats_IBP

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