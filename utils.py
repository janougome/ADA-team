import numpy as np
import pandas as pd
from collections import Counter

def unique_speaker_per_gender(quotes, time = None):
        """
    Allows to computed the frequency of quotes said by each gender in a given dataframe of quotes,
    as well as the total number of Occurrences associated with each gender. 


    Parameters
    ----------
    quotes: dataframe of quotes
    time: can be a string, a float or an int
        Defines the year or period associated with the dataframe of quotes
        into the same category "Others".
        
    Returns
    -------
    summary: a dataframe of the following shape
    '''
    root
     |-- gender: string 
     |-- unique_speaker: nb of unique speakers of this gender / nb total unique speakers
     |-- time: string, float or int
    """
        speaker_grouped = quotes.groupby(['qids', 'gender'])
        speakers = Counter([x[1] for x in speaker_grouped['numOccurrences'].sum().index])
        speaker_per_gender = {k: v/speaker_grouped.ngroups for k, v in speakers.items()}
        speaker_items = speaker_per_gender.items()
        speaker_list = list(speaker_items)
        df_speaker = pd.DataFrame(speaker_list, columns = ['gender', 'count'])
        df_speaker['time'] = time
        return df_speaker


def quotes_by_gender(quotes, time = None, major_only = False, others_grouped = False):
    """
    Allows to computed the frequency of quotes said by each gender in a given dataframe of quotes,
    as well as the total number of Occurrences associated with each gender. 


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
     |-- count: float
     |-- Occurrences: float
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
    
    #Take the number of occurences by gender
    occurrences = gender_grouped['numOccurrences'].sum() \
            .reset_index(name='Occurrences') \
            .sort_values(['Occurrences'], ascending=False)
    #Normalization
    occurrences['Occurrences'] = occurrences['Occurrences']/quotes['numOccurrences'].sum()
    
    summary = summary.merge(occurrences)


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


