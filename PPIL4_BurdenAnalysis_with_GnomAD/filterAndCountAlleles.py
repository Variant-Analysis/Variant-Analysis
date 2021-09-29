import sys
from fisher import pvalue

finnishAlleleCounts = []
nonFinnishAlleleCounts = []
totalAlleleNumbers = []
rsNumbers = []

with open(sys.argv[1], "r") as fp:
    lines = fp.readlines()[1:]
    for line in lines:
        if (float(line.split(',')[27]) < 0.0001 and float(line.split(',')[36]) < 0.0001):
            if line.split(',')[-1].replace('"', '').split('\t')[0] in ["stop_gained", "frameshift_variant", "splice_acceptor_variant", "splice_donor_variant"]:
                finnishAlleleCounts.append(int(line.split(',')[-1].replace('"', '').split('\t')[2]))
                totalAlleleNumbers.append(int(line.split(',')[-1].replace('"', '').split('\t')[3]) + int(line.split(',')[-1].replace('"', '').split('\t')[5]))
                nonFinnishAlleleCounts.append(int(line.split(',')[-1].replace('"', '').split('\t')[4]))
                if (str(line.split(',')[-1].replace('"', '').split('\t')[1]) != ''):
                    rsNumbers.append(str(line.split(',')[-1].replace('"', '').split('\t')[6].replace('\n', '')))
            elif line.split(',')[-1].replace('"', '').split('\t')[0] == "missense_variant":
                if float(line.split(',')[12]) >= 30.0:
                    finnishAlleleCounts.append(int(line.split(',')[-1].replace('"', '').split('\t')[2]))
                    totalAlleleNumbers.append(int(line.split(',')[-1].replace('"', '').split('\t')[3]) + int(line.split(',')[-1].replace('"', '').split('\t')[5]))
                    nonFinnishAlleleCounts.append(int(line.split(',')[-1].replace('"', '').split('\t')[4]))
                    if (str(line.split(',')[-1].replace('"', '').split('\t')[1]) != ''):
                        rsNumbers.append(str(line.split(',')[-1].replace('"', '').split('\t')[6].replace('\n', '')))
print("Total Finnish European Allele Counts (TFEAC): " + str(sum(finnishAlleleCounts)))
print("Total Non-Finnish European Allele Counts (TNEAC): " + str(sum(nonFinnishAlleleCounts)))
print("TFEAC + TNEAC: " + str(sum(finnishAlleleCounts) + sum(nonFinnishAlleleCounts)))
print("Max Allele Number: " + str(max(totalAlleleNumbers)))
print("Variant Count in Gnomad: " + str(len(finnishAlleleCounts)))
print("WARNING: Following rs numbers are flagged in gnomAD: " + str(filter(None, rsNumbers)))
print("Remove flagged variants, calculated Normal Allelle Count: " + str((max(totalAlleleNumbers)) - (len(finnishAlleleCounts) - len((filter(None, rsNumbers))))))
c1 = len(finnishAlleleCounts) - len((filter(None, rsNumbers)))
print("Variant Count after removing flagged variants: " + str(c1))
c2 = (max(totalAlleleNumbers)) - (len(finnishAlleleCounts) - len((filter(None, rsNumbers))))
p = pvalue(4.0, 864.0, len(finnishAlleleCounts) - len((filter(None, rsNumbers))), (max(totalAlleleNumbers)) - (len(finnishAlleleCounts) - len((filter(None, rsNumbers)))))
oddsratio = float(4.0)/float(864.0)/(float(c1)/float(c2))
print(p)
print(oddsratio)
