import pygal
from scipy.signal import savgol_filter

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