#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here
    errors = (abs(predictions - net_worths)).flatten()
    indices = errors.argsort()

    cleaned_data = [(ages[idx],net_worths[idx], errors[idx]) for idx in indices[:-9]]
   
    return cleaned_data

