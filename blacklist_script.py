import pandas as pd
import matplotlib.pyplot as plt

######## Get blacklisted bins #########

autosomes = pd.read_csv("autosomes_sd_mean.bed", sep="\t", header=None)
X = pd.read_csv("X_sd_mean_women.bed", sep="\t", header=None)
Y = pd.read_csv("Y_sd_mean_men.bed", sep="\t", header=None)

tables=[autosomes, X, Y]
total_genome_size = 0

for chr in tables:
	size = chr.shape[0] * 2000
	total_genome_size += size

print(f"Total genome size: {total_genome_size} base pairs") #För att kunna räkna procent blaklistade baser i slutet

#percentages = []

def blacklist(df, column_index, threshold_max, threshold_min=None):
	print("started blacklist function") 		

	if threshold_min is None:
		blacklist = df[(df[column_index] > threshold_max)]
	
	else:

		blacklist = df[(df[column_index] < threshold_min) | (df[column_index] > threshold_max)]
    	
	return blacklist		

######### Merge and filter blacklist ############


def merge_blacklist(df):
	print("started merging the blacklisted regions")

	df = df.iloc[:, [0, 1, 2]]

	merged_rows = []
	current_row = None

	for _, row in df.iterrows():

		if current_row is None:
                        current_row = row
		else:
                        if (row[0] == current_row[0] and row[1] == current_row[2]):
                                current_row[2] = row[2]
                        else:
                                merged_rows.append(current_row)
                                current_row = row

	merged_df = pd.DataFrame(merged_rows)	

	return merged_df

######## remove too small bins from blacklist #########

def filter_blacklist(df, size, total_genome_size):
	print("started filtering blacklist")
	
	small_regions = 0
	
	start = df.iloc[:, 1]
	end = df.iloc[:, 2]
	interval_size_before_filter = end - start
	
	small_regions = (interval_size_before_filter < size).sum()

	filtered_df = df[interval_size_before_filter >= size]

	header = ["chr", "start", "end"]
	filtered_df.columns = header
	

	interval_size_after_filter = filtered_df["end"] - filtered_df["start"]	
	size_blacklisted_regions = interval_size_after_filter.sum()
	percentage_blacklisted_regions = (size_blacklisted_regions / total_genome_size) * 100	

	#percentages.append(percentage_blacklisted_regions)

	print(f" removed {small_regions} from blacklist")
	print(f"blacklisted {percentage_blacklisted_regions}% of genome")

	return filtered_df

#max_values = [0.1, 0.15, 0.2, 0.22, 0.25, 0.27, 0.3, 0.35, 0.4, 0.45, 0.5]
#min_values = [0.75, 0.80, 0.83, 0.85, 0.87, 0.88, 0.89, 0.90]
#dev_from_1 = [0.25, 0.20, 0.17, 0.15, 0.13, 0.12, 0.11, 0.10]

#for max in max_values:

blacklist_autosomes = blacklist(autosomes, 3, 1.25, 0.75)
blacklist_X = blacklist(X, 3, 1.25, 0.75)
blacklist_Y = blacklist(Y, 4, 0.05)

whole_genome_blacklist = pd.concat([blacklist_autosomes, blacklist_X, blacklist_Y])
#whole_genome_blacklist.to_csv("whole_genome_blacklist.bed", sep="\t", header=0)

merged_blacklist = merge_blacklist(whole_genome_blacklist)
#merged_blacklist.to_csv("filtered_blacklist.bed", sep="\t", index=False)

merged_and_filtered_blacklist = filter_blacklist(merged_blacklist, 10000, total_genome_size)
merged_and_filtered_blacklist.to_csv("finished_blacklist_sex_separated_0.05.bed", sep="\t", header=False, index=False)
print(f"finished blacklist saved as: finished_blacklist.bed")	
	

#plt.plot(dev_from_1, percentages)
#plt.xlabel("Deviation from 1 (mean value)")
#plt.ylabel("Percentage of genome blacklisted")
#plt.title ("How much gets blacklisted with different thresholds?")
#plt.savefig("plot_different_blacklists.png", format="png")
#plt.close()	





