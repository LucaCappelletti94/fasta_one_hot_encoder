from fasta_one_hot_encoder import FastaOneHotEncoder
import numpy as np
import filecmp


def test_fasta_one_hot_encoder():
    encoder = FastaOneHotEncoder("acgtn")
    path = "test_data/my_test_fasta.fa"
    encoded = encoder.transform(path, verbose=True)
    np.save(path, encoded)

    expected = "{path}-expected.npy".format(path=path)
    new_file = "{path}.npy".format(path=path)

    assert filecmp.cmp(expected, new_file)
