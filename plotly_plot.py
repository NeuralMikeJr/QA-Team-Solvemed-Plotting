import plotly.graph_objects as go
import numpy as np
from scipy.signal import savgol_filter

def plot_hist(diff):
    fig = go.Figure()
    fig.add_trace(go.Histogram(x=diff,
                               xbins=dict(start=min(diff), end=max(diff), size=20)))
    fig.update_layout(title='Histogram of differences between adjacent frames', title_x=0.5,
                   xaxis_title='Difference [px]',
                   yaxis_title='Number of frames')
    fig.show()

def smooth_plot(bbox_size):
    yhat = savgol_filter(bbox_size, 51, 3)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(range(len(yhat))), y=yhat,
                    mode='lines',
                    name='lines'))
    fig.update_layout(title='Bbox size', title_x=0.5,
                   xaxis_title='Frame',
                   yaxis_title='Bbox size [px]')
                   
    fig.show()
