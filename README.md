# ada-2021-project-adamn
# Women's voices before and after #MeToo
## Table of Contents
1. [Abstract](#abstract)
2. [Research Questions](#research-questions)
3. [Proposed Additional Datasets](#proposed-additional-datasets)
4. [Methods](#methods)
5. [Contributions](#Contributions)

## Abstract
In October 2017, the exposure of sexual harassment allegations against famed film producer Harvey Weinstein led to the re-emergence of the #MeToo movement. The goal of this social movement was to visibly demonstrate the magnitude of the sexual assault problem through widespread media coverage of victim’s testimony. In this project, we are provided with the Quotebank dataset, an open corpus of 178 million quotations attributed to the speakers who uttered them, extracted from 162 million English news articles published between 2008 and 2020. Our goal is to exploit this dataset (2015 to 2020) to analyze if women are more represented in newspapers after the #MeToo movement. We would like to analyze whether the liberation of women's voices regarding sexual harassment has led to an increased representation of their opinions and statements in general in newspapers.

## Research Questions
1. How are female speakers represented in newspapers compared to male speakers?

First, in a primary descriptive analysis, we compare male and female speakers over the years in several aspects:
- We observe the evolution of the number of quotations and of the number of occurrences spoken by each gender. 
- We compare the number of different speakers of each genre.
- We observe the main occupations represented for each genre, the ages of speakers, and the way genders are referred to in the quotes.
2. Have women spoken more after the 'MeToo' movement? And has the representation of women evolved after Metoo for different occupation categories?

Second, we focus on the evolution of women's voices after #Metoo by conducting an observational study. First, we seek to analyze if women in general have spoken more in the newspaper after the movement, compared to men.
- We will analyze if the profile of the female speakers has changed: whether the professions represented have differed post-Metoo. This would help us determine the extent to which women's views have gained credibility.

## Proposed Additional Datasets
Since our analysis focuses on the representation of women in newspapers, we need to collect additional information about the speaker. To do so, we use the additional speaker metadata available for ~9M unique Wikidata entities (identified by their QID) in the form of a .parquet file. This file contains several attributes from which we kept: 'gender', 'date_of_birth', 'id', 'ethnic_group', 'academic_degree', 'occupation' and 'religion'. We then merged this additional data set with our original one. However, the parquet file provides us with wikicodes. To get readable information, we used the file "wikidata_labels_descriptions.csv.bz2" allowing to link the wikicode to a readable label. This way, each quotation is linked to its speaker and his attributes in a readable way.

## Methods
### Preprocessing
The first step in our work is to pre-process the provided data. Since our study relies on speaker analysis, we eliminate all unknown speakers, those with an assigned probability below 0.7 and the unnecessary columns. We then dealt with the huge dataset by loading the dataframe in chunks using Pandas APIs with a chunk size of 1 million. We then merged each chunk with the relevant attributes of the reduced package, the wikicodes were then made readable using labels (explained above). We then filtered the data by removing quotes spoken by a speaker with unknown gender and/or date of birth and keeping only the first gender in the list. We calculated the speaker's age at that point, stored it in an age column, and deleted the date of birth column. We then retrieved the data in a JSON file. 
### Data exploration
The first questions we address are descriptive. We are especially interested in the number of quotes and of occurrences for each gender. At the very beggining, we explore the data with all genders. Then, we grouped our speakers by gender (keeping only women and men) and performed our descriptive analyses by year first and then categorizing "before", "during", and "after" Metoo. We also quantify briefly the impact of the #MeToo movement in the newspaper, as well as the way how different gender are refered to.
### Observational study
Now we want to answer the question of whether the women have more spoken after the #Metoo movement and we would like to see if certain professions are now more represented in newspapers than before MeToo. In this part, the entire dataset is treated. We conduct an observational study, with the treatment being "the MeToo movement happened." Control and treatment groups consist of speakers before and after #Metoo, respectively. We will calculate the propensity score for each speaker in order to obtain the probability to be treated (being a speaker before or after #MeToo). Propensity scores will be calculated based on observed features such as age, occupation, academic degree and gender through a logistic regression (treatment ~ age + C(Government) + C(Scientist) + … + C(bachelor) + C(phD) + ... + C(male) + C(female)). In order to answer the question if women in general speak more after the movement, we will match pairs of speakers (1 control, 1 treated) based on the propensity scores, only if they are of the same gender. Then, we will also proceed by occupational category and we will match pairs of female speakers with the same occupation, as well as pairs of male speakers with the same occupation. The measured outcome will be the number of quotations and occurrences attributed to each group for a specific profession: the number of quotations only after 2017 for the treated one, and only before 2017 for the control one. By iterating this process across all pairs for multiple profession categories, we will be able to tell if, for example, women scientists spoke more in newspapers after MeToo, but controlling for confounding factors through matching. By comparing with men, we will be able to tell if the trends we observe are just global trends or really related to women. The datastory is available [here](https://josephinepotdevin.github.io/datastory/).

## Contributions
- Lisa: Data preprocessing and filtering, propensity scores and matching
-	Julie: Problem formulation, ReadMe redaction, group the academic degree by categories
-	Jeannette: First descriptive tasks, analysis of the balanced data after matching, (graphs), conclusions
-	Josephine: Group the occupations in categories, data story

