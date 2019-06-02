"""Create a new fasta one hot encoder."""
from sklearn.preprocessing import OneHotEncoder
from multiprocessing import Pool, cpu_count
import os
import itertools
from typing import List
import numpy as np
import pandas as pd
from tqdm import tqdm


class FastaOneHotEncoder:
    """Create a new fasta one hot encoder."""

    def __init__(self,
                 nucleotides: str,
                 kmers_length: int = 1,
                 lower: bool = True,
                 processes: int = -1,
                 **kwargs):
        """Create a new fasta one hot encoder.
            nucleotides:str, list of nucleotides to encode for.
            kmers_length:int = 1, length of kmers
            lower:bool = True, whetever to convert sequences to lowercase.
            processes:int = -1, number of processes to use, -1 to use all available cores.
        """
        assert isinstance(nucleotides, str)
        assert isinstance(kmers_length, int)
        assert kmers_length >= 1
        assert isinstance(lower, bool)
        assert isinstance(processes, int)
        assert processes == -1 or processes > 1
        self._processes = processes
        self._lower = lower
        self._kmers_length = kmers_length
        if self._processes == -1:
            self._processes = cpu_count()
        self._onehot_encoder = OneHotEncoder(categories='auto', **kwargs)
        self._onehot_encoder.fit(
            self._get_combinations(nucleotides).reshape(-1, 1)
        )

    @property
    def classes(self)->List[str]:
        return self._onehot_encoder.categories_

    def _get_combinations(self, alphabet: str)->np.array:
        return np.array([
            ''.join(i) for i in itertools.product(alphabet, repeat=self._kmers_length)
        ])

    def _to_lower(self, sequence: str) -> np.array:
        return sequence.lower() if self._lower else sequence

    def _to_kmers(self, sequence: str)->List[str]:
        return [
            sequence[i:i+self._kmers_length]
            for i in range(len(sequence)-self._kmers_length+1)
        ]

    def _to_array(self, sequence: str) -> np.array:
        return np.array(
            self._to_kmers(self._to_lower(sequence))
        )

    def _task(self, sequence: str) -> np.array:
        return self._onehot_encoder.transform(
            self._to_array(sequence).reshape(-1, 1)
        )

    def _is_new_sequence(self, row: str):
        return row.startswith(">")

    def _task_generator(self, path: str):
        with open(path, "r") as f:
            sequence, line = "", f.readline()
            while line:
                if not (line == "\n" or self._is_new_sequence(line)):
                    sequence += line.strip("\n")
                if line.startswith(">") and sequence:
                    yield sequence
                    sequence = ""
                line = f.readline()
            yield sequence

    def transform(self, path: str, verbose: bool = False) -> np.array:
        """Return numpy array representing one hot encoding of fasta at given path.
            path:str, path to fasta to one-hot encode.
            verbose:bool=False, whetever to show progresses.
        """
        assert isinstance(path, str)
        assert isinstance(verbose, bool)
        assert os.path.exists(path)
        with Pool(self._processes) as p:
            generator = p.imap(self._task, self._task_generator(path))
            if verbose:
                generator = tqdm(generator)
            result =  np.stack(list(generator))
            p.close()
            p.join()
        return result
            

    def transform_to_df(self, path: str, verbose: bool = False) -> pd.DataFrame:
        """Return pandas dataframe representing one hot encoding of fasta at given path.
            path:str, path to fasta to one-hot encode.
            verbose:bool=False, whetever to show progresses.
        """
        return pd.DataFrame(
            np.vstack(self.transform(path, verbose)),
            columns=self.classes,
            dtype='int'
        )
