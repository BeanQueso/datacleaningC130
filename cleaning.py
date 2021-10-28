import pandas as pd 
import csv 

df = pd.read_csv("merged_star_data.csv")

del df["Luminosity"]
del df["Star_name"]
del df["Distance"]
del df["Mass"]
del df["Radius"]
