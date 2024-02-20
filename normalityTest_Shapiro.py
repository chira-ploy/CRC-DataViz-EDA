#!usr/bin/env python
#Author = Chiranan Khantham

from scipy.stats import shapiro

def normalityTest_Shapiro(data, alpha=0.05):
    """
    Check whether the given data follows a normal distribution using a statistical test.

    Parameters:
    - data (array-like): The data to be tested for normality.
    - alpha (float, optional): The significance level for the Shapiro-Wilk test. Default is 0.05.

    Returns:
    - normality (str): A string indicating the result of the normality test.
    """
    
    # Perform Shapiro-Wilk test
    statistic, p_value = shapiro(data)

    # Interpret the results
    alpha = 0.05
    if p_value > alpha:
        print("Data looks normally distributed (fail to reject H0)")
    else:
        print("Data does not look normally distributed (reject H0)")
