from fasta_one_hot_encoder import FastaOneHotEncoder
import numpy as np


def test_fasta_one_hot_encoder():
    encoder = FastaOneHotEncoder("acgtn", sparse=False)
    path = "test_data/my_test_fasta.fa"
    encoded = encoder.transform(path, verbose=True)

    assert np.all(encoded == np.load(path+"-expected.npy"))
