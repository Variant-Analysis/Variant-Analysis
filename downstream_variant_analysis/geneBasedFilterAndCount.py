import sys

finnishAlleleCounts = []
nonFinnishAlleleCounts = []
totalAlleleNumbers = []
rsNumbers = []
geneDict = {}
geneDictMax = {}

def findColumnIndex(headerLine, name):
    for i in range(0, len(headerLine.split('\t'))):
        if headerLine.split('\t')[i].replace('\n', '') == name:
            return i

with open(sys.argv[1], "r") as fp:
    allLines = fp.readlines()
    lines = allLines[1:]
    headerLine = allLines[0]
    for line in lines:
        if (float(line.split('\t')[findColumnIndex(headerLine, "gnomAD_exome_NFE")]) < 0.0001 and float(line.split('\t')[findColumnIndex(headerLine, "gnomAD_genome_NFE")]) < 0.0001 and str(line.split('\t')[findColumnIndex(headerLine, "Otherinfo6")]).replace('\n', '') == "0"):
            if line.split('\t')[findColumnIndex(headerLine, "Otherinfo1")] in ["stop_gained", "frameshift_variant", "splice_acceptor_variant", "splice_donor_variant"]:
                geneName = line.split('\t')[findColumnIndex(headerLine, "Gene.refGene")]
                if geneDict.has_key(geneName):
                    alleleCount = geneDict[geneName] + float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo2")]) + float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo4")])
                    geneDict[geneName] = alleleCount
                else:
                    alleleCount = float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo2")]) + float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo4")])
                    geneDict[geneName] = alleleCount
                if geneDictMax.has_key(geneName):
                    maxCount = max(geneDictMax[geneName], float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo3")]) + float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo5")]))
                    geneDictMax[geneName] = maxCount
                else:
                    maxCount = float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo3")]) + float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo5")])
                    geneDictMax[geneName] = maxCount
            elif line.split('\t')[findColumnIndex(headerLine, "Otherinfo1")] == "missense_variant":
                if float(line.split('\t')[findColumnIndex(headerLine, "CADD13_PHRED")]) >= 30.0:
                    geneName = line.split('\t')[findColumnIndex(headerLine, "Gene.refGene")]
                    if geneDict.has_key(geneName):
                        alleleCount = geneDict[geneName] + float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo2")]) + float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo4")])
                        geneDict[geneName] = alleleCount
                    else:
                        alleleCount = float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo2")]) + float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo4")])
                        geneDict[geneName] = alleleCount
                    if geneDictMax.has_key(geneName):
                        maxCount = max(geneDictMax[geneName], float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo3")]) + float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo5")]))
                        geneDictMax[geneName] = maxCount
                    else:
                        maxCount = float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo3")]) + float(line.split('\t')[findColumnIndex(headerLine, "Otherinfo5")])
                        geneDictMax[geneName] = maxCount

print("Total Allele Counts by Gene:")
print("---------------------------------")

for key in geneDict.keys():
    print(key + ": " + str(int(geneDict[key])))

print("Max Allele Number by Gene:")
print("---------------------------------")

for key in geneDictMax.keys():
    print(key + ": " + str(int(geneDictMax[key])))
