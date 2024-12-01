import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv("medical_examination.csv")

# 2
BMI = df["weight"] / (df["height"] / 100)**2
df['overweight'] = (BMI > 25).astype(int)


# 3
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# 4
def draw_cat_plot():
    # 1. Convertir el DataFrame a formato largo
    df_cat = pd.melt(
        df, 
        id_vars=["cardio"], 
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
        var_name="variable", 
        value_name="value"    
    )

    #df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="count")
    df_cat = df_cat.groupby("cardio").value_counts()
    df_cat = df_cat.reset_index()

    print(df_cat.head())
    
    cat_plot = sns.catplot(
        x="variable",  
        y="count",    
        hue="value",   
        col="cardio",  
        data=df_cat,   
        kind="bar",    
        height=5,      
        aspect=1       
    )

    cat_plot.set_axis_labels("Variable", "Conteo")
    cat_plot.set_titles("Cardio = {col_name}")
    #cat_plot.despine(left=True)
    plt.show()

    # 8
    fig = cat_plot


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = None

    # 12
    corr = None

    # 13
    mask = None



    # 14
    fig, ax = None

    # 15



    # 16
    fig.savefig('heatmap.png')
    return fig
