import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv(r"C:\Users\mugok\Desktop\Data sets\medical_examination.csv")

# Add 'overweight' column
df['overweight'] = np.where(df['weight'] / np.square(df['height'] /100) > 25 , 1,0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['cholesterol'] =np.where(df['cholesterol'] == 1 , 0 ,1)
df['gluc'] = np.where(df['gluc'] == 1 , 0 ,1)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat =  pd.melt(df,id_vars = ["cardio"] , value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature and rename one of the columns for the catplot to work correctly.
    
    # Draw the catplot with 'sns.catplot()'
    
    figure  = sns.catplot(x ="variable", data = df_cat , hue= 'value', kind='count',col = 'cardio')

    figure.set_axis_labels('variable','total')


    # Get the figure for the output
    fig = figure


    # Save figure and declare as return value for the function.
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
  (df['ap_lo'] <= df['ap_hi']) &
  (df['height'] >= df['height'].quantile(0.025))&
  (df['height'] <= df['height'].quantile(0.975))&
  (df['weight'] >= df['weight'].quantile(0.025))&
  (df['weight'] <= df['weight'].quantile(0.975))
  
  
  ]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr , dtype = bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (14,7))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr , annot = True , mask =mask)


    # Save figure and declare as return value for the function.

    fig.savefig('heatmap.png')
    return fig
