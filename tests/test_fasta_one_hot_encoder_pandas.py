from fasta_one_hot_encoder import FastaOneHotEncoder
import pandas as pd


def test_fasta_one_hot_encoder():
    encoder = FastaOneHotEncoder("acgt", handle_unknown="ignore", sparse=False)
    path = "test_data/my_test_fasta.fa"
    df = encoder.transform_to_df(path, verbose=True)
    assert (df == pd.read_csv("test_data/test.csv", usecols=[
            "a", "c", "g", "t"])).all().all()
