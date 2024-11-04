# Calculate mean and sd in regions

import pandas as pd

# Read input BED file


table = "chrY_men_filtered.bed"
df = pd.read_csv(table, sep="\t", header=None)

df.iloc[:, 3:] = df.iloc[:, 3:].astype(float)
df = df.fillna(0)

regions = df.iloc[:, :3]
coverage = df.iloc[:, 3:]

mean_list = coverage.mean(axis=1)
sd_list = coverage.std(axis=1)

regions.loc[:, 'mean'] = mean_list
regions.loc[:, 'sd'] = sd_list

regions.columns = ['chr', 'start', 'end', 'mean', 'sd']
regions.to_csv("Y_sd_mean_men.bed", sep="\t", header = False, index = False)

 
