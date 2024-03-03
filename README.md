## Introduction

This repository contains the code and documentation for the medical visualizer project , using medical examimation dataset. 
The primary goal of this project is to visualize and make calculations from medical examination data using pandas , seaborn and matplotlib.The dataset values were collected through medical examination exercises.

## Dataset Source and Overview

The medical examination dataset used in this project was obtained from a data analysis course  from FreeCodeCamp, which I completed. It consists of patients attributes such as: age ,gender,height ,weight , Systolic blood pressure , Diastolic blood pressure	, Cholesterol level , Glucose level, Smoking status ,Alcohol intake status , Physical activity ,  and Presence or absence of cardiovascular disease.

## Tools Used

For this project, the following tools and libraries were used:

- **Python:** for data cleaning tasks.
- **Pandas:** instrumental in data manipulation, cleaning, and handling missing values.
- **NumPy:** utilized for mathematical operations .
- **Matplotlib and Seaborn:** utilized to perform visualizations.

## Project Execution Process

The project involved the following steps:

1. **Data Understanding:** The dataset was thoroughly examined to understand the structure, columns, and their meanings. The data had a data dictionary attached which helped me gain an understanding of what all the columns represented.

2. Adding an **overweight** column to the data. To determine if a person is overweight, first calculate their BMI by dividing their weight in kilograms by the square of their height in meters. If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.

3. **Normalized** the data by making 0 always good and 1 always bad. If the value of **cholesterol** or **gluc** is 1, make the value 0. If the value is more than 1, make the value 1.

4. Converted the data into long format and created a chart that shows the value counts of the categorical features using seaborn's **catplot()**. The dataset was  split by **'Cardio'** so there is one chart for each cardio value.

5. **Cleaning the data**. Filtering out the following patient segments that represent incorrect data:
    - diastolic pressure is higher than systolic (Keep the correct data with **(df['ap_lo'] <= df['ap_hi'])**)
    - height is less than the 2.5th percentile (Keep the correct data with **(df['height'] >= df['height'].quantile(0.025))**)
    - height is more than the 97.5th percentile
    - weight is less than the 2.5th percentile
    - weight is more than the 97.5th percentile

 6. Creating a correlation matrix using the dataset and plotting the correlation matrix using seaborn's heatmap(). Mask the upper triangle.

## Documentation

For detailed information about this project, please refer to the Python (.py) files and visualized images (.png)  provided in this repository.

 
