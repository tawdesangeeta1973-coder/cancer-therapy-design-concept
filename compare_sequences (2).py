"""
compare_sequences.py - list point differences between two equal-length DNA sequences.

A real, small utility (not a simulation, not a clinical variant caller). It compares a
"reference/normal" sequence with a "sample/tumor" sequence and reports substitutions.
It does NOT align sequences, call indels, or interpret clinical meaning. Real pipelines
use tools such as BWA, GATK, or Mutect2 on sequencing data; this is a learning starting point.

Coordinate assumption:
    Position 1 in the normal file and position 1 in the tumor file are assumed to refer
    to the SAME base of the SAME reference coordinate system. This tool does not verify
    that. If the files are not already aligned to a common reference, every reported
    "substitution" is meaningless.

Usage:
    python compare_sequences.py normal.fasta tumor.fasta
    python compare_sequences.py normal.fasta tumor.fasta --quiet
    python compare_sequences.py normal.fasta tumor.fasta --vcf
"""
import sys


def read_fasta(path):
    """Read a single-record FASTA file and return the sequence as an upper-case string."""
    seq, records = [], 0
    with open(path) as f:
        for line in f:
            if line.startswith(">"):
                records += 1
                continue
            seq.append(line.strip().upper())
    if records > 1:
        raise ValueError(f"{path} has {records} records; this tool expects exactly one.")
    return "".join(seq)


def find_substitutions(ref, alt):
    if len(ref) != len(alt):
        raise ValueError(
            f"Sequences differ in length ({len(ref)} vs {len(alt)}). "
            "This tool needs pre-aligned, equal-length sequences."
        )
    # Only positions where BOTH bases are unambiguous A/C/G/T are reported.
    # Positions with N or other IUPAC codes are skipped on purpose: an unknown
    # base is not evidence of a mutation. Do not "fix" this.
    return [
        (i + 1, r, a)
        for i, (r, a) in enumerate(zip(ref, alt))
        if r != a and r in "ACGT" and a in "ACGT"
    ]


def parse_args(argv):
    positional = [a for a in argv[1:] if not a.startswith("-")]
    flags = {a for a in argv[1:] if a.startswith("-")}
    if (flags - {"--quiet", "--vcf"}) or len(positional) != 2:
        sys.exit(__doc__)
    return positional[0], positional[1], "--quiet" in flags, "--vcf" in flags


if __name__ == "__main__":
    normal_path, tumor_path, quiet, vcf = parse_args(sys.argv)
    ref, alt = read_fasta(normal_path), read_fasta(tumor_path)
    if not ref or not alt:
        sys.exit("No sequence found in one or both input files.")

    diffs = find_substitutions(ref, alt)

    if vcf:
        # VCF-LIKE only: no header and a placeholder contig name ("seq"), so this is
        # not a valid VCF file. It is a bridge to the concept, not a file format.
        for pos, r, a in diffs:
            print(f"seq\t{pos}\t.\t{r}\t{a}\t.")
    elif quiet:
        for pos, r, a in diffs:
            print(f"{pos}\t{r}\t{a}")
    else:
        rate = len(diffs) / len(ref)
        print(f"Compared {len(ref)} bases; found {len(diffs)} substitution(s) ({rate:.4%}).")
        for pos, r, a in diffs:
            print(f"position {pos}: {r} -> {a}")
