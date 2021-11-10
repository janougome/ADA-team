import numpy as np
import pandas as pd


def quotes_by_gender(quotes, time = None, major_only = False, others_grouped = False):
    """
    Allows to computed the frequency of quotes said by each gender in a given dataframe of quotes.


    Parameters
    ----------
    quotes: dataframe of quotes
    time: can be a string, a float or an int
        Defines the year or period associated with the dataframe of quotes
    major_only: bool, optional
        If true, returns only the counts for the 2 most represented genders in the dataset.
    others_grouped: bool, optional
        If True, it groups the other genders than the 2 most represented genders into the same category "Others".
        
    Returns
    -------
    summary: a dataframe of the following shape
    '''
    root
     |-- gender: string 
     |-- count: string 
     |-- time: string, float or int
    """
    #Group by gender
    gender_grouped = quotes.groupby(quotes.gender)

    #Take the number of quotes by gender
    summary = gender_grouped['gender'].count() \
            .reset_index(name='count') \
            .sort_values(['count'], ascending=False)
    
    #Normalization
    summary['count'] = summary['count']/len(quotes)

    if major_only:
        if time is not None:
            summary['time'] = time
            return summary[0:2]
        else:
            return summary[0:2]
    else:
        if others_grouped:
            others = pd.DataFrame([['others', summary[2:]['count'].sum()]], columns = ['gender', 'count'])
            summary = summary[0:2].append(others, ignore_index = True)
            if time is not None:
                summary['time'] = time
                return summary
            else:
                return summary
        else:
            if time is not None:
                summary['time'] = time
                return summary
            else:
                return summary
