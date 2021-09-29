# python /home/wd256/scripts/IA_filter.py <vcf>
# function: filter the vcf file by the following criteria and generate a variant table:
# VQSR = "PASS"; DP >= 8, GQ >= 20; MAF < 1E-04 in gnomAD NFE (both genome and exome); LoF or CADDv1.3 >= 30

import sys
import gzip

header = []
header_flag = 'F'
order = []

if sys.argv[1][-3:-1]=='.gz':
	file = gzip.open(sys.argv[1],'r')
	out = open(sys.argv[1][:-7] + '_filtered_variantTable.txt', 'w')
else:
	file =  open(sys.argv[1],'r')
	out = open(sys.argv[1][:-4] + '_filtered_variantTable.txt', 'w')
	
for line in file:
	data = line.strip().split('\t')
	if '#CHROM' in line:
		store = data
	elif line[0] != '#':
		info = data[7].split(';')
		Info = {}
		for key in info:
			if len(key.split('=')) == 2:
				Info[key.split('=')[0]] = key.split('=')[1]
				order.append(key.split('=')[0]) 

		# Print out header
		if header_flag == 'F':
			for key in order:
				header.append(key)
			out.write('SAMPLE'+'\t'+'\t'.join(store[0:7])+'\t'+'\t'.join(header)+'\tGT\tDP\tAD\tGQ\tPL\n')
			header_flag = 'T'
		
		if Info['Gene.refGene'] != 'PPIL4':
			continue
						
		# VQSR = "PASS"
		if data[6] != 'PASS':
			continue
		
		# MAF < 1E-04 in gnomAD NFE (both genome and exome)
		if Info['gnomAD_exome_NFE'] != '.':
			if float(Info['gnomAD_exome_NFE']) >= 0.0001:
				continue
		if Info['gnomAD_genome_NFE'] != '.':
			if float(Info['gnomAD_genome_NFE']) >= 0.0001:
				continue
				
		# LoF or missense with CADDv1.3 >= 30
		if not (Info['Func.refGene'] == 'splicing' or (Info['Func.refGene'] == 'exonic' and ((Info['ExonicFunc.refGene'] == 'nonsynonymous_SNV' and float(Info['CADD13_PHRED']) >= 30) or Info['ExonicFunc.refGene'] == 'frameshift_deletion' or Info['ExonicFunc.refGene'] == "frameshift_insertion" or Info['ExonicFunc.refGene'] == "stopgain" or Info['ExonicFunc.refGene'] == "stoploss"))):
			continue
						
		# Get line contents
		line_out = '\t'.join(data[0:7])
		for i in header:
			if i not in Info:
				line_out = line_out+'\t'+'NA'
			else:
				line_out = line_out+'\t'+Info[i]

		# Print out each line
		item_format = data[8].split(':')
		for j in store[9:]:
			item = data[store.index(j)].split(':')
			
			GT = item[item_format.index('GT')]
			if GT == './.' or GT == '0/0':
				continue

			DP = item[item_format.index('DP')]
			AD = item[item_format.index('AD')]
			
			if 'GQ' not in item_format:
				GQ = 'NA'
			else:
				GQ = item[item_format.index('GQ')]
			if 'PL' not in item_format:
				PL = 'NA'
			else:
				PL = item[item_format.index('PL')]

			#  DP >= 8, GQ >= 20
			if DP!='NA' and float(DP) < 8:
				continue
			if GQ !='NA' and float (GQ) < 20:
				continue

			out.write(j+'\t'+line_out+'\t'+'\t'.join([GT,DP,AD,GQ,PL])+'\n')		

out.close()
