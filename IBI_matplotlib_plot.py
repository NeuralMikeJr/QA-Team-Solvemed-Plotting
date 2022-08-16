import json
import os
from matplotlib_plot import plot_hist, smooth_plot
from datafetcher import get_bbox_size_IBI, get_diff_IBI, get_stats_IBI

def main():
    json_files = os.listdir('C:/Users/48795/Documents/Solvemed/Annotations/14-07-2022/14-07-2022/')
    bbox_size = []
    for json_file in json_files:
        bbox_size.extend(get_bbox_size_IBI('C:/Users/48795/Documents/Solvemed/Annotations/14-07-2022/14-07-2022/' + json_file))
    diff = get_diff_IBI(bbox_size)
    mean, std = get_stats_IBI(diff)
    print('Mean:', mean)
    print('Standard deviation:', std)
    plot_hist(diff)
    smooth_plot(bbox_size)

if __name__ == '__main__':
    main()