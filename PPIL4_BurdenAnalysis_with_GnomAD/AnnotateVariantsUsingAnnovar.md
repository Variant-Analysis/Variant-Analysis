For reference and citation: https://github.com/bio-ontology-research-group/VSIM/tree/master/VSIM/annovar

**Download Required Databases**

 * annotate_variation.pl -buildver hg19 -downdb cytoBand humandb/
 * annotate_variation.pl -buildver hg19 -downdb -webfrom annovar refGene humandb/
 * annotate_variation.pl -buildver hg19 -downdb -webfrom annovar exac03 humandb/ 
 * annotate_variation.pl -buildver hg19 -downdb -webfrom annovar gnomad_exome humandb/
 * annotate_variation.pl -buildver hg19 -downdb -webfrom annovar gnomad_genome humandb/
 * annotate_variation.pl -buildver hg19 -downdb -webfrom annovar cadd13 humandb/

**Obtain Variant List From GnomAD**

 * To download variant list, search the gene of interest on gnomAD website (https://gnomad.broadinstitute.org/) 
 * Choose variants annotated as pLoF and missense/inframe indel.
 * Ignore filtered variants which did not pass quality control process by gnomAD.
 * Export variants to csv.

**Annotate Variants with Annovar**
 * table_annovar.pl ./ex1.avinput humandb/ -buildver hg19 -out myanno -remove -protocol refGene,cytoBand,cadd13,exac03,gnomad_exome,gnomad_genome -operation g,r,f,f,f,f -nastring 0 -csvout -otherinfo

**Filter Variants and Count Alleles**
 * pip install fisher
 * python filterVariantsAndCountAlleles.py [PPIL_gnomAD_annovar.csv](./PPIL_gnomAD_annovar.csv)

Variant filtering in gnomAD (version 2.1.1) for non-Finnish + Finnish control data was performed using aforementioned inclusion criteria. Variants that were flagged (LOFTEE) by gnomAD (version 2.1.1) for low confidence were assessed in dbSNP database (https://www.ncbi.nlm.nih.gov/snp/), whether any clinical information was associated with the variant and were excluded if no pathogenicity was reported.



