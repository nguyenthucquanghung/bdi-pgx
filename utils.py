# this file was used to test cyvcf2 output
from cyvcf2 import VCF

vcf = '22_42126578-42130778.vcf'
# vcf = 'CYP2D6/CYP2D6_3.vcf'
vcf_obj = VCF(vcf)
count = 0
for variant in vcf_obj:
    chromosome = variant.CHROM
    pos = variant.POS
    ref = variant.REF
    alt = variant.ALT
    af = variant.INFO.get('AF')
    variant_type = variant.INFO.get('variant_type')
    print('----------------------')
    print(chromosome)
    print(pos)
    print(ref)
    print(alt)
    print(af)
    print(variant_type)
    count += 1
print(count)
