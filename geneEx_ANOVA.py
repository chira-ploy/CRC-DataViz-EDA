#!usr/bin/env python

#Author = Chiranan Khantham

import pandas as pd
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

