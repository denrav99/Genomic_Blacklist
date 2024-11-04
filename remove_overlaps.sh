module load bioinfo-tools
module load BEDTools/2.31.1

DIR="/proj/sens2017106/nobackup/denise/blacklist_proj/output/tables/blacklist_separated_by_sex/finished_blacklist_sex_separated_0.08.bed"

bedtools subtract -a $DIR -b Agnes_overlaps_cleaned.bed > cleaned_blacklist.bed

bedtools intersect -a $DIR -b Agnes_overlaps_cleaned.bed > subtracted_regions.bed
