import pandas as pd
from itertools import combinations


star_alleles = pd.read_csv('star_allele_table.csv')


# initial data
normal = []
decrease = []
no_func = []
for index, row in star_alleles.iterrows():
    if row['activity_score'] == 1:
        normal.append(int(row['star_allele']))
    if row['activity_score'] == 0.5:
        decrease.append(int(row['star_allele']))
    if row['activity_score'] == 0:
        no_func.append(int(row['star_allele']))


sa_freq = []    # final result


# add couple of star alleles that have activity score 0.0
for comb in list(combinations(no_func, 2)):
    row = list(comb)
    row.append(float(1/(5*465)))
    row.append(0)
    sa_freq.append(row)
# add couple of star alleles that have activity score 0.5
for i in no_func:
    for j in decrease:
        sa_freq.append([i, j, float(1/(5*403)), 1])
# add couple of star alleles that have activity score 1.0
for i in no_func:
    for j in normal:
        sa_freq.append([i, j, float(1 / (5 * 388)), 2])
for comb in list(combinations(decrease, 2)):
    row = list(comb)
    row.append(float(1 / (5 * 388)))
    row.append(2)
    sa_freq.append(row)
# add couple of star alleles that have activity score 1.5
for i in decrease:
    for j in normal:
        sa_freq.append([i, j, float(1 / (5 * 130)), 3])
# add couple of star alleles that have activity score 2.0
for comb in list(combinations(normal, 2)):
    row = list(comb)
    row.append(float(1 / (5 * 45)))
    row.append(4)
    sa_freq.append(row)


# save data to csv
data = pd.DataFrame(sa_freq, columns=['allele_1', 'allele_2', 'prob', 'label'])
data.to_csv(r'~/PycharmProjects/bdi-pgx/sa_freq.csv', index=None, header=True)