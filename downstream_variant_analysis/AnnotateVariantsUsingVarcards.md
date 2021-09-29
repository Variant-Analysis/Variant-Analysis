for reference and citation: https://academic.oup.com/nar/article/46/D1/D1039/4588107

**Steps for Creating variantCounts.xlsx**

 * Download variant list from gnomAD 2.1.1 (https://gnomad.broadinstitute.org/)
 * Filter variants flaged by gnomAD (mnv, lc_lof, lof_flag, mnv, lcr, os_lof)
 * Include missense and LoF (stop_gained, splice_acceptor, splice_donor, frameshift) only
 * Annotation queried using genomic coordinate (snv) on Varcards website (http://159.226.67.237/sun/varcards/) for remaining variants
 * Inclusion criteria: gnomAD  NFE_MAF<0.0001 for genome and exome; LoF variants; Missense variants CADD>=30 (v1.3).
 * Calculate allele counts using the script.
 * To download variant list, search the gene of interest on gnomAD website (https://gnomad.broadinstitute.org/) 
 * Choose variants annotated as pLoF and missense/inframe indel.
 * Ignore filtered variants which did not pass quality control process by gnomAD.
 * Export variants to csv.

**Calculate Allele Counts and Max Allele Number**

 * python2.7 calculateAlleleCountsForProcessedAndFilteredVariantTable.py variantCountsFor16Genes.xlsx

**Important Notes**

 * Variant tables were obtained using gnomAD v2.1.1
 * In gnomAD v2.1.1, POTEM gene has been as annotated POTEG; please see this link for an example variant: https://gnomad.broadinstitute.org/variant/14-19553862-G-A?dataset=gnomad_r2_1
