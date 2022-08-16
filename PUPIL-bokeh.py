import os
from plotting.datafetcher import get_bbox_size_IBP, get_diff_IBP, get_stats_IBP
from plotting.bokeh_plot import plot_hist, smooth_plot

def main():
    json_files = os.listdir('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/')
    bbox_size = []
    for json_file in json_files:
        bbox_size.extend(get_bbox_size_IBP('C:/Users/48795/Documents/Solvemed/Annotations/13-08-2022/13-08-2022/' + json_file))
    diff = get_diff_IBP(bbox_size)
    mean, std = get_stats_IBP(diff)
    print('Mean:', mean)
    print('Standard deviation:', std)
    plot_hist(diff)
    smooth_plot(bbox_size)

if __name__ == '__main__':
    main()