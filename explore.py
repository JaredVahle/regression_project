import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np
from scipy import stats

def zillow_heatmap(df):
    '''
    returns a heatmap and correlation for our target of tax_value
    '''
    plt.figure(figsize = (8,12))
    heatmap = sns.heatmap(df.corr()[["tax_value"]].sort_values(by='tax_value', ascending=False), vmin = -.5, vmax = .5, annot = True)
    heatmap.set_title(f"Features Correlating with tax value")
    
    return heatmap


def plot_categorical_and_continuous_vars(df,categorical,continuous):
    for cont_col in continuous:
        for cat in categorical:
            categorical_label = cat
            continuous_label = cont_col
            
            fig, axes = plt.subplots(figsize=(12,36), nrows=4,ncols=1)
            fig.suptitle(f'{continuous_label} by {categorical_label}', fontsize=18, y=1.02)
            sns.lineplot(ax=axes[0], x=cat, y=cont_col, data=df)
            axes[0].set_title('Line Plot', fontsize=14)
            axes[0].set_xlabel(categorical_label, fontsize=12)
            axes[0].set_ylabel(continuous_label, fontsize=12)
            
            sns.boxplot(ax=axes[1], x=cat, y=cont_col, data=df,\
                        color='blue')
            axes[1].set_title('Box-and-Whiskers Plot', fontsize=14)
            axes[1].set_xlabel(categorical_label, fontsize=12)
            axes[1].set_ylabel(continuous_label, fontsize=12)
            
            sns.swarmplot(ax=axes[2], x=cat, y=cont_col, data=df,\
                        palette='Blues')
            axes[2].set_title('Swarm Plot', fontsize=14)
            axes[2].set_xlabel(categorical_label, fontsize=12)
            axes[2].set_ylabel(continuous_label, fontsize=12)
            
            sns.barplot(ax=axes[3], x=cat, y=cont_col, data=df,\
                        palette='Purples')
            axes[3].set_title('Bar Plot', fontsize=14)
            axes[3].set_xlabel(categorical_label, fontsize=12)
            axes[3].set_ylabel(continuous_label, fontsize=12)
            
            plt.tight_layout()
            
            plt.show()


def plot_variable_pairs(df, cols, descriptive=None, hue=None):
    '''
    This function takes in a df, a list of cols to plot, and default hue=None 
    and displays a pairplot with a red regression line. If passed a descriptive
    dictionary, converts axis titles to the corresponding names.
    '''
    # sets line-plot options and scatter-plot options
    keyword_arguments={'line_kws':{'color':'red'}, 'scatter_kws': {'alpha': 0.1}}
    
    # creates pairplot object
    pairplot = sns.pairplot(df[cols], hue=hue, kind="reg",\
            plot_kws=keyword_arguments)
    
    # if passed a descriptive dictionary, iterates through matplotlib axes
    # in our pairplot object and sets their axis labels to the corresponding 
    # strings.
    if descriptive:
        for ax in pairplot.axes.flat:
            ax.set_xlabel(descriptive[ax.get_xlabel()])
            ax.set_ylabel(descriptive[ax.get_ylabel()])
    
    # Adds a super-title
    pairplot.fig.suptitle('Correlation of Continuous Variables', y=1.08)
    plt.show()


def plot_pairplot(df, cols, descriptive=None, hue=None):
    '''
    Take in train df, list of columns to plot, and hue=None
    and display scatter plots and hists.
    '''
    pairplot = sns.pairplot(df[cols],hue = df[hue], corner=True)
    pairplot.axes.flat[0].set_ylabel(cols[0])
    if descriptive:
        for ax in pairplot.axes.flat:
            if ax:
                ax.set_xlabel(descriptive[ax.get_xlabel()])
                ax.set_ylabel(descriptive[ax.get_ylabel()])
    pairplot.fig.suptitle('Correlation of Continuous Variables', y=1.08)
    plt.show()

