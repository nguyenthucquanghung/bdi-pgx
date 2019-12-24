from cyvcf2 import VCF
import random
import pandas as pd
import pickle


def random_distribution(item_prob):
    r = random.uniform(0, 1)
    s = 0
    for item, prob in item_prob:
        s += prob
        if s >= r:
            return item
    return item_prob[-1][0]  # Might occur because of floating point inaccuracies => return last element


# get input
df = pd.read_csv('sa_freq.csv')
df['star_alleles'] = df[['allele_1', 'allele_2']].values.tolist()
sa_freq = df[['star_alleles', 'prob']].values.tolist()


# simulate data
gnomAD = '22_42126578-42130778.vcf'
adapter = {'A': 0, 'C': 1, 'T': 2, 'G': 3}
first_pos = 42126578
no_of_pos = 4201
no_of_samples = 120000
data = [[[0] * no_of_pos] * 4] * no_of_samples  # init data


# assign gnomAD variants with allele frequencies into initialized data
previous = -1
ls_alt = []
for variant in VCF(gnomAD):
    if variant.INFO.get('AF') < 0.05:
        if variant.POS == previous:
            ls_alt.append([variant.ALT, variant.INFO.get('AF')])
        else:
            def_freq = 1
            for alt, freq in ls_alt:
                def_freq -= freq
            ls_alt.append(['DEF', def_freq])
            for i in range(no_of_samples):
                alt = random_distribution(ls_alt)
                if alt != 'DEF':
                    data[i][adapter[alt[0]]][previous - first_pos] = 1
            previous = variant.POS
            ls_alt.clear()
            ls_alt.append([variant.ALT, variant.INFO.get('AF')])


# random distribute a pair of star alleles to samples
for i in range(no_of_samples):
    sa_pair = random_distribution(sa_freq)
    sa_1 = 'CYP2D6/CYP2D6_{}.vcf'.format(sa_pair[0])
    sa_2 = 'CYP2D6/CYP2D6_{}.vcf'.format(sa_pair[1])
    for variant in VCF(sa_1):
        if len(variant.ALT[0]) == 1:
            pos = variant.POS - first_pos
            for j in range(4):
                data[i][j][pos] = 0
            data[i][adapter[variant.ALT[0]]][pos] = 1


# save simulated data
pickle.dump(data, open('simulated_data.pkl', 'wb'))
