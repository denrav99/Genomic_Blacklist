import pandas as pd

table_Y = pd.read_csv("chrY.bed", sep="\t", header=None)  
table_X = pd.read_csv("chrX.bed", sep="\t", header=None)

men = []
women = []


for column_index_Y in range(3, table_Y.shape[1]):	
	column_data_Y = table_Y.iloc[:, column_index_Y]
	mean_Y = column_data_Y.mean()
	
	if mean_Y > 0.1:
		men.append(column_index_Y)


for column_index_X in range(3, table_X.shape[1]):
	column_data_X = table_X.iloc[:, column_index_X]
	mean_X = column_data_X.mean()

	if mean_X > 0.75:
		women.append(column_index_X)


men_table = table_Y.iloc[:, [0, 1, 2] + men]
women_table = table_X.iloc[:, [0, 1, 2] + women]

men_table.to_csv("chrY_men_filtered.bed", sep="\t", header=False, index=False)
women_table.to_csv("chrX_women_filtered.bed", sep="\t", header=False, index=False)
