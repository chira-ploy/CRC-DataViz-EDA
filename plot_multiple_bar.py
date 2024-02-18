#! usr/bin/env python

# Author = Chiranan Khantham

import matplotlib.pyplot as plt
import seaborn as sns

def plot_multiple_bar(df, column_list, title=''):
    """Plot bar graphs for multiple columns in the DataFrame.

    Parameters:
    - df: DataFrame
    - column_list: list of str, column names to plot
    - title: str, title of the multiple plots
    """
    
    # Determine the number of rows and columns based on the number of plots
    num_plots = len(column_list)
    num_rows = (num_plots + 1) // 2  # Ensure at least 1 row
    num_cols = 2  # Maximum 2 columns
    
    # Set up subplots
    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(12, 8))
    
    # Flatten the axes array to handle different cases
    axes = axes.flatten()
    
    # Loop through columns and plot bar graphs
    for i, column in enumerate(column_list):
        value_counts_sorted = df[column].value_counts().sort_index()
        sns.barplot(x=value_counts_sorted.index, y=value_counts_sorted, ax=axes[i])
        axes[i].set_title(f'{column} Distribution')
        
    # Adjust layout
    plt.tight_layout()
    plt.suptitle(title)
    plt.subplots_adjust(top=0.9)  # Adjust the top of the figure to make room for suptitle
    
    plt.show()
