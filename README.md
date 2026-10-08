# Computational Pipeline Concept for Personalized Cancer Prevention and Therapy Design

> **Status: concept / discussion draft (v0.1). Not medical advice. Not peer reviewed. Not tested in patients.**

This repository explores how software could support cancer risk assessment, early detection, and therapy design,
and is explicit about what is established, what is speculative, and what is unsolved.

It does **not** claim a cure, a universal vaccine, a painless treatment, or an end to cancer.

## Read first
- [`Cancer_Prevention_Therapy_Design_Concept_Paper.pdf`](Cancer_Prevention_Therapy_Design_Concept_Paper.pdf) - the concept paper

## Three groups, three different problems
| Group | Realistic focus today |
|---|---|
| High inherited risk (e.g. BRCA1/2, Lynch) | Genetic testing, surveillance, risk-reducing options with a clinician |
| Lifestyle / environment-related risk | Risk reduction, vaccination, screening, early detection |
| Established or advanced cancer | Combination therapy, personalization, monitoring |

## Planned modules
1. Risk assessment (probabilistic, based on published models)
2. Variant and neoantigen analysis (public data only)
3. Editing design (wrapper around validated tools, with off-target warnings)
4. Delivery-aware design notes
5. Toxicity monitoring support (clinician-facing, never autonomous)

## What exists in this repo
- `compare_sequences.py` - a small, real utility that lists substitutions between two equal-length FASTA sequences.
  It is a learning tool, not a clinical variant caller. Supports `--quiet` and a VCF-like `--vcf` mode (not valid VCF).
- `test_compare_sequences.py` - unit tests (`python -m unittest`).

## Known open problems
Tissue-specific delivery, editing efficiency in vivo, off-target effects, unedited cells, tumor heterogeneity,
immune toxicity of cell therapies, stage 4 solid tumors, cost, and ethics. See Section 5 of the paper.

## Rules for this project
- No clinical use. No patient data without ethics approval.
- Any simulation must label its parameters as assumptions and must not be presented as evidence.
- Verify every citation before adding it.

## Contributing
Feedback from clinicians, geneticists, and bioinformaticians is especially welcome. Open an issue to challenge a claim.

## License
Suggested: MIT for code, CC BY 4.0 for the paper .
