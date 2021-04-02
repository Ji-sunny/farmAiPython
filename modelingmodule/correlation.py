from scipy.stats.stats import spearmanr
from scipy.stats.stats import spearmanr

# 시각화: amchart - heat map with legend

def pearson(data_x, data_y):
    pearsonr(data_x, data_y)

    return 'a'


def pearson_all(data):
    data.corr(method='pearson')

    return 'a'


def spearman(data_x, data_y):
    spearmanr(data_x, data_y)

    return 'b'


def spearman_all(data):
    data.corr(method='pearson')

    return 'a'
