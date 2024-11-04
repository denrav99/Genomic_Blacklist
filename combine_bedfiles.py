import os
import pandas as pd
from glob import glob

BED_DIR = "/proj/sens2017106/nobackup/denise/2kbp_bins_bed"
OUTPUT_FILE = "output_table2.bed"

bed_files = sorted(glob(os.path.join(BED_DIR, "*normalized.bed")))
#print(f"BED files found: {bed_files}")

#bed_files_test = bed_files[:10]

regions_df = pd.read_csv(bed_files[0], sep="\t", header=None, usecols=[0, 1, 2])

temp_coverage = []

for bed_file in bed_files:
	print(f"Adding coverage data from: {bed_file}", flush=True)
	coverage_df = pd.read_csv(bed_file, sep="\t", header=None, usecols=[3])
	temp_coverage.append(coverage_df)

coverage_combined = pd.concat(temp_coverage, axis=1)
regions_df = pd.concat([regions_df, coverage_combined], axis=1)

regions_df.to_csv(OUTPUT_FILE, sep="\t", header=False, index=False)

print(f"Combined BED file saved as: {OUTPUT_FILE}")
