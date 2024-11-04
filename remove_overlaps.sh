module load bioinfo-tools
module load BEDTools/2.31.1

bedtools subtract -a $DIR -b Agnes_overlaps_cleaned.bed > cleaned_blacklist.bed

bedtools intersect -a $DIR -b Agnes_overlaps_cleaned.bed > subtracted_regions.bed
