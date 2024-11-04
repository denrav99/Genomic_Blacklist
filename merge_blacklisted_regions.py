#module load python/3.9.5

import pandas as pd

blacklist = pd.read_csv("cleaned_blacklist.bed", sep="\t", header=None)


previous_region = None
merged_regions = []

for _, row in blacklist.iterrows():
	current_chr = row.iloc[0]
	current_start = row.iloc[1]
	current_end =  row.iloc[2]

	if previous_region is not None:
		prev_chr, prev_start, prev_end = previous_region
		
		if current_chr == prev_chr and (current_start - prev_end) < 10000:
			
			print(f"Merging: {previous_region} with ({current_chr}, {current_start}, {current_end})")
			previous_region = (current_chr, prev_start, current_end)
			
		else:
			merged_regions.append(previous_region)
			previous_region = (current_chr, current_start, current_end)
	else:
		previous_region = (current_chr, current_start, current_end)

if previous_region is not None:
    merged_regions.append(previous_region)

merged_df = pd.DataFrame(merged_regions)
merged_df.to_csv("merged_blacklist_sex_separated.bed", sep='\t', header=False, index=False)
