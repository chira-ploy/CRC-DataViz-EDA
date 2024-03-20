#!usr/bin/env python

#Author = Chiranan Khantham

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway

def geneEx_ANOVA(df, groupBy_column, alpha=0.05):
    """
    Perform one-way ANOVA for each gene in the DataFrame.
    
    Parameters:
        df (DataFrame): The DataFrame containing gene expression data.
        groupBy_column (str): The column name to group by.
    
    Returns:
        List of genes whose p-values are lower than threshold.
        A DataFrame containing gene name, F-statistic, and p-value for all genes.
    """
    threshold = alpha
    gene_columns = df.iloc[:, 9:]  # columns of genes start from column 9
    groupBy_list = df[groupBy_column].unique()
    ANOVA_all = []
    significant_genes = []
    
    for column in gene_columns:
        samples = [df[df[groupBy_column] == group][column] for group in groupBy_list]
        f_statistic, p_value = f_oneway(*samples)
        ANOVA_all.append([column, f_statistic, p_value])
        
        if p_value < threshold:
            significant_genes.append(column) 
            
    df_ANOVA_all = pd.DataFrame(ANOVA_all, columns=['Gene', 'f_statistic', 'p_value'])
            
    return significant_genes, df_ANOVA_all

def plot_multiple_boxplot(df, groupBy_column, significant_genes):
    
    sorted_significant_genes = sorted(significant_genes)
    num_plots = len(sorted_significant_genes)
    num_cols = 4 

    # Calculate the number of rows needed based on the number of genes and maximum columns
    num_rows = (num_plots + num_cols - 1) // num_cols

    # Set up subplots
    fig, axes = plt.subplots(nrows=num_rows, ncols=num_cols, figsize=(20, 5*num_rows))

    # Flatten the axes array to handle different cases
    axes = axes.flatten()

    # Loop through gene
    for i, gene in enumerate(sorted_significant_genes):
        # Assign the current subplot for the box plot
        ax = axes[i]
    
        # Plot the box plot for the current gene
        sns.boxplot(data=df, x=groupBy_column, y=gene, ax=ax, width=0.5)
        sns.stripplot(data=df, x=groupBy_column, y=gene, ax=ax, color='black', size=4)
    
        # Set labels and title for the subplot
        ax.set_xlabel(groupBy_column)
        ax.set_ylabel('Expression')
        ax.set_title(f'Boxplot for Gene: {gene}')
        ax.tick_params(axis='x')
    
    # Remove empty subplots after plotting genes
    for ax in axes[num_plots:]:
        ax.remove()

    # Adjust layout
    plt.subplots_adjust(wspace=0.2, hspace=0.3)  # Increase space between subplots
    plt.show()

def main(df, groupBy_column, alpha=0.05):
    
    significant_genes, _ = geneEx_ANOVA(df, groupBy_column, alpha)
    plot_multiple_boxplot(df, groupBy_column, significant_genes)
    
    return significant_genes