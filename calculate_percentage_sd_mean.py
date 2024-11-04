import pandas as pd 

data = pd.read_csv("autosomes_sd_mean.bed", sep="\t", header=None)

def calculate_percentage_mean(df, threshold_min, threshold_max, stat_column):

    stat_inside_range = 0
    N = len(df)

    for value in df[stat_column]:
        if value > threshold_min and value < threshold_max:
            stat_inside_range += 1

    percent = (stat_inside_range / N) * 100

    print(f"{percent} % is inside of range")


def calculate_percentage_sd(df, threshold, stat_column):

    stat_below_threshold = 0
    N = len(df)

    for value in df[stat_column]:
        if value < threshold:
            stat_below_threshold += 1

    percent = (stat_below_threshold / N) * 100

    print(f"{percent} % is below threshold")


calculate_percentage_mean(data, 0.75, 1.25, "mean")
#calculate_percentage_sd(data, 0.1, "sd")
