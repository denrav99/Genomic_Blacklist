#!/bin/bash -l

#SBATCH -p core
#SBATCH -n 1
#SBATCH -t 3-00:00:00
#SBATCH -J separate_tables

module load bioinfo-tools tabix

# Compress BED file
bgzip -f $INPUT_BED
bgzip -f $INPUT_BED_STATS

# Index compressed BED file
tabix -p bed ${INPUT_BED}.gz 
tabix -p bed ${INPUT_BED_STATS}.gz

# Extract autosomes
tabix ${INPUT_BED}.gz $(seq -s " " 1 22) > autosomes.bed
tabix ${INPUT_BED_STATS}.gz $(seq -s " " 1 22)  > autosomes_sd_mean.bed

# Extract sex chromosomes
tabix ${INPUT_BED}.gz X > chrX.bed
tabix ${INPUT_BED_STATS}.gz X > chrX_sd_mean.bed

tabix ${INPUT_BED}.gz Y > chrY.bed
tabix ${INPUT_BED_STATS}.gz Y > chrY_sd_mean.bed

