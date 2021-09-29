# 
## Table of Contents

**Steps used for Analysis**
  * [Whole Exome Sequencing and Annotation Processing - Ruddle](./seq_analysis_protocols/ruddle_exome.md)
  * Variant filtering using specified parameters (see below)
  * [PCA Analysis using HapMap](./quality_control_analyses/pca_analysis.md)
  * [Kinship, Relatedness, and Sex-Check using PLINK](./quality_control_analyses/plink_analysis.md)
  * [Annotate Variants using Annovar](./PPIL4_BurdenAnalysis_with_GnomAD/AnnotateVariantsUsingAnnovar.md)
  * [Annotate Variants using Varcards](./downstream_variant_analysis/AnnotateVariantsUsingVarcards.md)
  * [Case Control using GNOMAD](./stat_tests_PPIL4/case_control_GNOMAD.md)

**VARIANT FILTERING PARAMETERS**
  * Standard filtering based VQSR = "PASS"
  * DP≥8, GQ≥20
  * MAF < 1E-04 in gnomAD NFE (both genome and exome)
  * LoF or CADDv1.3 ≥ 30

 
