from fasta_one_hot_encoder import FastaOneHotEncoder
import filecmp
import os


def test_combinatorial():
    encoder = FastaOneHotEncoder(
        "acgt", kmers_length=2, handle_unknown="ignore", sparse=False)
    path = "test_data/my_test_fasta.fa"
    df = encoder.transform_to_df(path, verbose=True)
    df.to_csv("test_data/new_combinatorial.csv")
    assert filecmp.cmp(
        "test_data/new_combinatorial.csv",
        "test_data/expected_combinatorial.csv"
    )
    os.remove("test_data/new_combinatorial.csv")
