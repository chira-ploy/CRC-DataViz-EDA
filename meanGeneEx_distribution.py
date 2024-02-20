#!usr/bin/env python

#Author = Chiranan Khantham

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def meanGeneEx_distribution(df, groupBy_column, groupBy_column_index):
    """
    Generates a violin plot to visualize the mean gene expression distribution across different groups.

    Parameters:
    - df (DataFrame): The DataFrame containing gene expression data.
    - groupBy_column (str): The name of the column used for grouping.
    - groupBy_column_index (int): The index of the column used for grouping.

    Returns:
    None
    """
    
    df_mean = df.iloc[:, [groupBy_column_index] + list(range(9, len(df.columns)))].groupby(groupBy_column).mean()

    # Reset index to make 'Location' a column again
    df_mean_reset_index = df_mean.reset_index()

    # Reshape the DataFrame for Seaborn
    dx_melted = pd.melt(df_mean_reset_index, id_vars=[groupBy_column], var_name='gene', value_name='mean_expression')

    # Plot using Seaborn
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=dx_melted, x=groupBy_column, y='mean_expression', palette ='pastel', inner='point', legend=False)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
