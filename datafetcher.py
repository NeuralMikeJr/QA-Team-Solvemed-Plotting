import json
import os
import numpy as np

def get_bbox_size_EBI(json_file):
    with open(json_file) as f:
        data = json.load(f)
    bbox_size = []
    for i in range(len(data)):
        for j in range(len(data[i]['annotations'])):
            if data[i]['annotations'][j]['label'] == 'EBI':
                bbox_size.append(data[i]['annotations'][j]['coordinates']['width'] * data[i]['annotations'][j]['coordinates']['height'])
                # print(bbox_size)
    return bbox_size

def get_diff_EBI(bbox_size):
    diff = []
    for i in range(len(bbox_size)-1):
        diff.append(bbox_size[i+1] - bbox_size[i])
    return diff

def get_stats_EBI(diff):
    mean = np.mean(diff)
    std = np.std(diff)
    return mean, std

def get_bbox_size_IBI(json_file):
    with open(json_file) as f:
        data = json.load(f)
    bbox_size = []
    for i in range(len(data)):
        for j in range(len(data[i]['annotations'])):
            if data[i]['annotations'][j]['label'] == 'IBI':
                bbox_size.append(data[i]['annotations'][j]['coordinates']['width'] * data[i]['annotations'][j]['coordinates']['height'])
                # print(bbox_size)
    return bbox_size

def get_diff_IBI(bbox_size):
    diff = []
    for i in range(len(bbox_size)-1):
        diff.append(bbox_size[i+1] - bbox_size[i])
    return diff

def get_stats_IBI(diff):
    mean = np.mean(diff)
    std = np.std(diff)
    return mean, std

def get_bbox_size_IBP(json_file):
    with open(json_file) as f:
        data = json.load(f)
    bbox_size = []
    for i in range(len(data)):
        for j in range(len(data[i]['annotations'])):
            if data[i]['annotations'][j]['label'] == 'IBP':
                bbox_size.append(data[i]['annotations'][j]['coordinates']['width'] * data[i]['annotations'][j]['coordinates']['height'])
                # print(bbox_size)
    return bbox_size

def get_diff_IBP(bbox_size):
    diff = []
    for i in range(len(bbox_size)-1):
        diff.append(abs(bbox_size[i+1] - bbox_size[i]))
    return diff

def get_stats_IBP(diff):
    mean = np.mean(diff)
    std = np.std(diff)
    return mean, std    