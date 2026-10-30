## us-life-expectancy
Project Description: Analysis of life expectancy estimates across U.S. states and D.C.
## Team Name:
Team Time Analyzers
## Contributors: 
Sophie Villar, Reem Mounir, Josie Spayd

## Objective and Motivation:
1. **specify dataset and provide details**

The objective of this project is to investigate a chosen dataset relating to our groups interest and write a functional program aimed at recieving useful information. Our chosen datasets reflects estimates of life expectancy at birth during the year of 2018 and 2020. Within our datasets, the estimates of life expectancy at birth are organized by total, male, and female populations based in each of the fifty states as well as the District of Columbia (D.C.). 

Our motive behind our project focuses on the perspective of a researcher from the U.S. Department of Health and Human Services that is interested in how life expectancies shifted before and during the COVID-19 pandemic. With a range of data spanning two years, any information we extract with our program would be considered valid for confirming a significant comparison. 

2. **specify the questions that you are asking (with the form of the expected answers) and the potential benefits that one would have**

- *Question one: How did the life expectancy gap between males and females change within and across the U.S. from 2018 to 2020?*
    - Expected Answer: We expect that the life expectancy of females will remain higher independent of the year and state. 
    - Potential Benefits: Recognizing that females have a longer life expectancy than males will serve as a larger motive for scientists to investigate deeper into womens health to better identify the factors that contribute to longer life span and apply any findings to all of human kind.

- *Question two: How did state-level variation and rankings in overall life expectancy shift between 2018 and 2020, and which states experienced the largest overall gains or drops?*
    - Expected Answer: Considering the rise of the COVID-19 pandemic in 2020, we expect that the life expectancy estimates should slightly decrease from 2018 to 2020. Additionally, we expect that states with major cities such as New York will have experienced the largest overall drops because the pandemic was spread faster in densly populated areas.
    - Potential Benefits: Identifying the states that were sucessful in avoiding life expectancy losses would allow public health officials to compare the data against regional healthcare response procedures and allocate future healthcare resources accordingly.

- *Question three: How did the relationship between the gender life expectancy gap and overall state life expectancy evolve between 2018 and 2020?*
    - Expected Answer: Since the pandemic impacted different states and genders differently, we expect to see the typical life expectancy gender gap in 2018 to be disrupted during 2020. 
    - Potential Benefits: Knowing the answer to this question would help identify if a certain states health department helped to protect both men and women equally during the pandemic, or if the pandemic widened the health gap between genders.This information would give health officials more insight on who is more vulnerable if a nationwide health emergency happens again.

## Introduction/Context of the Project:
1. this section is not mandatory, but if you feel like some content needs to be introduced in order to understand the methods and questions, please add all necessary details here

*ANSWER HERE*

## Implementation Details:
1. **go over the methods (with metrics, tools, plots) to be used to answer the question. this is the main body of the repo**

*Question one: How did the life expectancy gap between males and females change within and across the U.S. from 2018 to 2020?*
- Means: 
    - Organize all given data by sex, state, and year
    - Calculate gaps in Life expectancy for males and females in each state and each year
    - Compare the gaps in life expectancy in each state between 2018 and 2020
    - calculate the average gap in life expectancy across the whole US
- Metrics: 
    - mean life expectancy (male and female)
    - average gap in life expectancy in years
    - standard deviation in the gaps in life expectancy
    - minimum and maximum gaps
- Tools: 
    - excel to filter through data, do calculations, and create graphs 
- Plots: 
    - bar chart to compare male vs. female life expectancy across the US
    - line graph to show average life expectancy gaps
    - bar chart to compare life expectancy data across 2018 and 2020

*Question two: How did state-level variation and rankings in overall life expectancy shift between 2018 and 2020, and which states experienced the largest overall gains or drops?*
- Means: 
    - organize total life expectancies per state in 2018 and 2020
    - calculate change in totals (2018 data - 2020 data)
    - rank states from highest to lowest totals for both years 
    - find which states have the highest increases and decreases in their totals
- Metrics: 
    - average the total life expectancies across the US
    - standard deviation of totals across the US
    - minimum and maximum totals 
    - change in totals from 2018 to 2020
- Tools: 
    - excel to organize the data and calculate the changes across the US as well as create graphs
- Plots: 
    - bar charts to compare totals between 2018 and 2020 
    - bar chart showing changes across the US across both years 
    - box plot for distributions of totals across 2018 and 2020
*Question three: How did the relationship between the gender life expectancy gap and overall state life expectancy evolve between 2018 and 2020?*
- Means: 
    - calculate the gap in life expectancies between males and females in 2018 and 2020
    - find total life expectancies for each state in 2018 and 2020
    - create a scatter plot to compare the gap in life expectancy and the totals for each state in 2018 and 2020
    - do linear regression to find relationship between these numbers
    - use linear regression data to compere 2018 and 2020 
- Metrics: 
    - find the correlation coefficient to find the strength and direction of the relationship 
    - find R^2 to find the variation in the gaps explained by the totals
    - find the slope to see how the gap changes with the totals increasing 
    - average the gap and totals for each state in 2018 and 2020 
- Tools: 
    - excel to organize all the data, create scatter plots, do linear regression, and find the correlation coefficient
- Plots: 
    - scatter plot gaps vs totals in 2018
    - scatter plot gaps vs totals in 2020
    - add trend lines to both graphs to perform linear regression and compare both years 

2. **added in coming phases**: screenshots that you feel is necessary to show project's complexity such as block diagrams, snippets, of the code that carries explicitly a method, a top-level code, etc.

## Results:
will be populated later

## Conclusions: 
will be populated later

## Actions that need to be completed:
will be populated later
1. list all actions that need to be completed (checklist)

    - Identify methods and metrics to answer questions
    - Create a GitHub Repo and add the methods and metrics to it
    - Submit the link of the GitHub repo as a URL

2. mention the issues that the group is facing for each action, if any

## References/Source Files:
list all references the group used for the project (including journal/conference papers, GitHub repositories, open-source files, etc.)

- 2018 dataset: https://catalog.data.gov/dataset/u-s-state-life-expectancy-by-sex-2018?from_hint=eyJxIjoiVS5TLiBsaWZlIGV4cGVjdGFuY3kgYnkgc2V4Iiwic29ydCI6InJlbGV2YW5jZSJ9  
- 2020 dataset: https://catalog.data.gov/dataset/u-s-state-life-expectancy-by-sex-2020?from_hint=eyJxIjoiZmVtYWxlIiwic29ydCI6InBvcHVsYXJpdHkifQ%3D%3D 
- course canvas page (lecture slides): https://canvas.jmu.edu/courses/2193471/files/folder/Lecture%20Notes  

**this is all used as a key for writing, do not delete anything below!**
paragraph `import matlpotlib`

paragraph *italic* or **bold**

    import matplotlip

OR

``` 
import matplotlib
```

Link [Text](URL)

images as ![Caption](URL)
