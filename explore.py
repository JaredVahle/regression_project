import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np
from scipy import stats

def plot_variable_pairs(train,cols,hue = None):
    '''
    this function takes in a list of columns and as default has hue set to none,
    and will create a pairplot with the regression line for each col.
    '''
    plot_kws = {"line_kws":{"color":"red"}, "scatter_kws": {"alpha": 0.7}}
    sns.pairplot(train[cols],hue = hue , kind = "reg", plot_kws = {"line_kws":{"color":"red"}, "scatter_kws": {"alpha": 0.1}})
    plt.show()

def zillow_heatmap(train,target):
    '''
    returns a heatmap and correlation for our target of tax_value
    '''
    plt.figure(figsize = (8,12))
    heatmap = sns.heatmap(train.corr()[[target]].sort_value(by = target, ascending = False), vmin = -.5, vmax = .5, annot = True)
    heatmap.set_title(f"Features Correlating with {target}")
    
    return heatmap

