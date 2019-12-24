import pandas as pd
import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    numerator = reduce(op.mul, range(n, n - r, -1), 1)
    denominator = reduce(op.mul, range(1, r + 1), 1)
    return numerator / denominator


normal = 0
decrease = 0
no_func = 0
star_allele = pd.read_csv('star_allele_table.csv')
for score in star_allele['activity_score']:
    if score == 1:
        normal = normal + 1
    if score == 0.5:
        decrease = decrease + 1
    if score == 0:
        no_func = no_func + 1


print('Number of normal allele: ', normal)
print('Number of decrease allele: ', decrease)
print('Number of no function allele: ', no_func, '\n')
print('Number of label 0.0: {}'.format(int(ncr(no_func, 2))))
print('Number of label 0.5: {}'.format(no_func * decrease))
print('Number of label 1.0: {}'.format(int(ncr(decrease, 2)) + normal * no_func))
print('Number of label 1.5: {}'.format(decrease * normal))
print('Number of label 2.0: {}'.format(int(ncr(normal, 2))))
