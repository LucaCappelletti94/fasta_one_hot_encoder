from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from multiprocessing import Pool, cpu_count
import numpy as np
from tqdm import tqdm


class FastaOneHotEncoder:
    def __init__(self, nucleotides: str, lower: bool = True, processes: int = -1):
        """Create a new fasta one hot encoder.
            nucleotides:str, list of nucleotides to encode for.
            lower:bool = True, whetever to convert sequences to lowercase.
            processes:int = -1, number of processes to use, -1 to use all available cores.
        """
        self._processes = processes
        self._lower = lower
        if self._processes == -1:
            self._processes = cpu_count()
        self._label_encoder = LabelEncoder()
        self._onehot_encoder = OneHotEncoder(sparse=False)
        self._label_encoder.fit(self._to_array(nucleotides))
        self._onehot_encoder.fit(self._transform(nucleotides))

    def _to_lower(self, sequence: str) -> np.array:
        return sequence.lower() if self._lower else sequence

    def _to_array(self, sequence: str) -> np.array:
        return np.array(
            list(self._to_lower(sequence))
        )

    def _transform(self, sequence: str) -> np.array:
        return self._label_encoder.transform(
            self._to_array(sequence)
        ).reshape(-1, 1)

    def _task(self, sequence: str) -> np.array:
        return self._onehot_encoder.transform(
            self._transform(sequence)
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

    def transform(self, path: str, verbose: bool=False) -> np.array:
        """Return numpy array representing one hot encoding of fasta at given path.
            path:str, path to fasta to one-hot encode.
            verbose:bool=False, whetever to show progresses.
        """
        with Pool(self._processes) as p:
            generator = p.imap(self._task, self._task_generator(path))
            if verbose:
                generator = tqdm(generator)
            return np.stack(list(generator))
