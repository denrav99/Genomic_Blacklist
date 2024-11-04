import pandas as pd
import os
import glob

chromosome_names =["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "X", "Y"]

for bed in sorted(glob.glob(os.path.join(BED_DIR, "*"))):
	df = pd.read_csv(bed, sep="\t", header=None)

	df.iloc[:, 0] = df.iloc[:, 0].astype(str).str.strip()	
	df = df[df.iloc[:, 0].isin(chromosome_names)]

	coverage = pd.to_numeric(df.iloc[:, 3], errors='coerce')
	print(coverage)
	regions = df.iloc[:, :3]	

	mean_coverage = coverage.mean()
	normalised = coverage / mean_coverage
	normalised = normalised.fillna(0.0)	

	regions[3] = normalised
	
	output_file = os.path.splitext(bed)[0] + "_normalized.bed"
	regions.to_csv(output_file, sep="\t", header=False, index=False)
	break

