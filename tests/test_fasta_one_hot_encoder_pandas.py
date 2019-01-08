from fasta_one_hot_encoder import FastaOneHotEncoder
import filecmp


def test_fasta_one_hot_encoder_pandas():
    encoder = FastaOneHotEncoder("acgt", handle_unknown="ignore", sparse=False)
    path = "test_data/my_test_fasta.fa"
    df = encoder.transform_to_df(path, verbose=True)
    df.to_csv("test_data/new_pandas.csv")
    assert filecmp.cmp(
        "test_data/new_pandas.csv",
        "test_data/expected_pandas.csv"
    )
