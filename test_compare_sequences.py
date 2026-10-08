import os, tempfile, unittest
from compare_sequences import find_substitutions, read_fasta


class TestCompare(unittest.TestCase):
    def test_identical(self):
        self.assertEqual(find_substitutions("ACGT", "ACGT"), [])

    def test_one_substitution(self):
        self.assertEqual(find_substitutions("ACGT", "ACTT"), [(3, "G", "T")])

    def test_length_mismatch(self):
        with self.assertRaises(ValueError):
            find_substitutions("ACGT", "ACG")

    def test_ambiguous_base_skipped(self):
        self.assertEqual(find_substitutions("ACNT", "ACGT"), [])

    def test_multi_record_fasta_rejected(self):
        with tempfile.NamedTemporaryFile("w", suffix=".fa", delete=False) as f:
            f.write(">a\nACGT\n>b\nACGT\n")
        try:
            with self.assertRaises(ValueError):
                read_fasta(f.name)
        finally:
            os.remove(f.name)


if __name__ == "__main__":
    unittest.main()
