# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches


def plot_scatter(plot_d, ignore = None, save=None):
    """scatter plot given a dictionary object"""
    fig = plt.figure(figsize=(6,6))
    gs = gridspec.GridSpec(1, 1)
    fig_axs = [fig.add_subplot(sp) for sp in gs]
    fig_axs[0].scatter(plot_d['x'], plot_d['y'])
    if ignore is None:
        ignore = set([])
    if(('title' in plot_d) and ('title' not in ignore)):
        fig_axs[0].set_title(plot_d['title'])
    if(('xlabel' in plot_d) and ('xlabel' not in ignore)):
        fig_axs[0].set_xlabel(plot_d['xlabel'])
    if(('ylabel' in plot_d) and ('ylabel' not in ignore)):
        fig_axs[0].set_ylabel(plot_d['ylabel'])
    if(('xticklabels' in plot_d) and ('xticklabels' not in ignore)):
        fig_axs[0].set_xticklabels(
            [textwrap.fill(x, 50) for x in plot_d['xticklabels']],
            rotation=270+45, rotation_mode="anchor", ha='left',
            minor=False
        )        
    gs.tight_layout(fig, rect=[0, 0, 1, 1]) 
    if save is not None:
        fig.savefig(save, bbox_inches="tight", pad_inches=0.0)


def plot_bar(plot_d, ignore = None, save=None):
    """bar plot given a dictionary object"""    
    fig = plt.figure(figsize=(6,6))
    gs = gridspec.GridSpec(1, 1)
    fig_axs = [fig.add_subplot(sp) for sp in gs]
    fig_axs[0].bar(plot_d['x'], plot_d['y'])
    if ignore is None:
        ignore = set([])
    if(('title' in plot_d) and ('title' not in ignore)):
        fig_axs[0].set_title(plot_d['title'])
    if(('xlabel' in plot_d) and ('xlabel' not in ignore)):
        fig_axs[0].set_xlabel(plot_d['xlabel'])
    if(('ylabel' in plot_d) and ('ylabel' not in ignore)):
        fig_axs[0].set_ylabel(plot_d['ylabel'])
    if(('xticklabels' in plot_d) and ('xticklabels' not in ignore)):
        fig_axs[0].xaxis.set_ticks(np.arange(len(plot_d['x'])) + 1) 
        fig_axs[0].set_xticklabels(
            [textwrap.fill(x, 50) for x in plot_d['xticklabels']],
            rotation=270+45, rotation_mode="anchor", ha='left',
            minor=False
        )        
    gs.tight_layout(fig, rect=[0, 0, 1, 1]) 
    if save is not None:
        fig.savefig(save, bbox_inches="tight", pad_inches=0.0)


def plot(plot_d, ignore = None, save=None):
    """line plot given a dictionary object"""    
    fig = plt.figure(figsize=(6,6))
    gs = gridspec.GridSpec(1, 1)
    fig_axs = [fig.add_subplot(sp) for sp in gs]
    fig_axs[0].plot(plot_d['x'], plot_d['y'])
    if ignore is None:
        ignore = set([])
    if(('title' in plot_d) and ('title' not in ignore)):
        fig_axs[0].set_title(plot_d['title'])
    if(('xlabel' in plot_d) and ('xlabel' not in ignore)):
        fig_axs[0].set_xlabel(plot_d['xlabel'])
    if(('ylabel' in plot_d) and ('ylabel' not in ignore)):
        fig_axs[0].set_ylabel(plot_d['ylabel'])
    if(('xticklabels' in plot_d) and ('xticklabels' not in ignore)):
        fig_axs[0].set_xticklabels(
            [textwrap.fill(x, 50) for x in plot_d['xticklabels']],
            rotation=270+45, rotation_mode="anchor", ha='left',
            minor=False
        )        
    gs.tight_layout(fig, rect=[0, 0, 1, 1]) 
    if save is not None:
        fig.savefig(save, bbox_inches="tight", pad_inches=0.0)


def plot_ax_stacked_bar(
    ax, y, label = None, title = None, xlabel = None, ylabel = None,
    bar_width = 1, show_legend=False, 
    show_xticklabels = False, show_yticklabels = False,
):
    '''
    Given an Axes class object, plot a stacked bar plot on that object
    https://matplotlib.org/api/axes_api.html
    - ax: Axes object
    - y: data
    - label: legend
    - title: sub plot title
    - xlabel: x-axis label
    - ylabel: y-axis label
    - bar_width: width of the stacked bar plot
    - show_legend: Boolean, whether we will show a legend or not
    - show_xticklabels: Boolean, whether we will show xticklabels  
    - show_yticklabels: Boolean, whether we will show yticklabels
    '''
    assert label is None or len(y) == len(label)
    data_len = len(y)
    bottom = np.append(np.zeros(1), np.cumsum(y)[:-1])
    p = [None] * data_len
    colors = color_pallet_with_gray(data_len)
    for i in range(data_len):
        p[i] = ax.bar(0, y[i], bottom=bottom[i], width=(2 * bar_width), color=colors[i])
    ax.set_xlim((0, 1))
    ax.set_ylim((0, 1))
    if(show_legend and label is not None):
        ax.legend(
            (p[i] for i in range(data_len)),
            tuple(label),
            bbox_to_anchor=(1, 1)
        )
    if(not show_xticklabels):            
        ax.set_xticklabels([]) 
    if(not show_yticklabels):            
        ax.set_yticklabels([]) 
    if(title is not None):
        ax.set_title(title)
    if(xlabel is not None):
        ax.set_xlabel(xlabel)        
    if(ylabel is not None):
        ax.set_ylabel(ylabel)        
    return ax