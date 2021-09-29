import xlrd
import sys

wb = xlrd.open_workbook(sys.argv[1])
sheet = wb.sheet_by_name('Sheet1')
geneDict = {}
geneDictMax = {}

def findColumnIndex(name, sheet):
    for col in range(sheet.ncols):
        if sheet.cell_value(0, col) == name:
            return col

for row in range(1, sheet.nrows):
    geneName = sheet.cell_value(row, findColumnIndex("Gene", sheet))
    if geneDict.has_key(geneName):
        alleleCount = geneDict[geneName] + float(sheet.cell_value(row, findColumnIndex("Allele Count European (Finnish)", sheet))) + float(sheet.cell_value(row, findColumnIndex("Allele Count European (non-Finnish)", sheet)))
        geneDict[geneName] = alleleCount
    else:
        alleleCount = float(sheet.cell_value(row, findColumnIndex("Allele Count European (Finnish)", sheet))) + float(sheet.cell_value(row, findColumnIndex("Allele Count European (non-Finnish)", sheet)))
        geneDict[geneName] = alleleCount

for row in range(1, sheet.nrows):
    geneName = sheet.cell_value(row, findColumnIndex("Gene", sheet))
    if geneDictMax.has_key(geneName):
        maxCount = max(geneDictMax[geneName], float(sheet.cell_value(row, findColumnIndex("Allele Number European (Finnish)", sheet))) + float(sheet.cell_value(row, findColumnIndex("Allele Number European (non-Finnish)", sheet))))
        geneDictMax[geneName] = maxCount
    else:
        maxCount = float(sheet.cell_value(row, findColumnIndex("Allele Number European (Finnish)", sheet))) + float(sheet.cell_value(row, findColumnIndex("Allele Number European (non-Finnish)", sheet)))
        geneDictMax[geneName] = maxCount

print("Total Allele Counts by Gene:")
print("---------------------------------")

for key in geneDict.keys():
    print(key + ": " + str(int(geneDict[key])))

print("Max Allele Number by Gene:")
print("---------------------------------")

for key in geneDictMax.keys():
    print(key + ": " + str(int(geneDictMax[key])))
