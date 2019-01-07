Fasta One-Hot Encoder
=================================
|travis| |sonar_quality| |sonar_maintainability| |sonar_coverage| |code_climate_maintainability| |pip|

Simple python to lazily one-hot encode fasta files using multiple processes, either single bases or considering arbitrary kmers.

Installation
---------------
Simply run:

.. code:: bash

    pip installed fasta_one_hot_encoder

Examples
---------------

Bases
~~~~~~~~~~~~~~~~~~
|bases|

One-hot encode to bases.

.. code:: python

    from fasta_one_hot_encoder import FastaOneHotEncoder

    encoder = FastaOneHotEncoder(
        nucleotides = "acgt",
        lower = True,
        sparse = False,
        handle_unknown="ignore"
    )
    path = "test_data/my_test_fasta.fa"
    encoder.transform_to_df(path, verbose=True).to_csv(
        "my_result.csv"
    )

Obtained results should look like:

+---+---+---+---+---+
|   | a | c | g | t |
+===+===+===+===+===+
| 0 | 0 | 0 | 1 | 0 |
+---+---+---+---+---+
| 1 | 0 | 1 | 0 | 0 |
+---+---+---+---+---+
| 2 | 0 | 1 | 0 | 0 |
+---+---+---+---+---+

Kmers
~~~~~~~~~~~~~~~~~~
|kmers|

One-hot encode to kmers of given length.

.. code:: python

    from fasta_one_hot_encoder import FastaOneHotEncoder

    encoder = FastaOneHotEncoder(
        nucleotides = "acgt",
        kmers_length=2,
        lower = True,
        sparse = False,
        handle_unknown="ignore"
    )
    path = "test_data/my_test_fasta.fa"
    encoder.transform_to_df(path, verbose=True).to_csv(
        "my_result.csv"
    )

Obtained results should look like:

+---+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|   | aa | ac | ag | at | ca | cc | cg | ct | ga | gc | gg | gt | ta | tc | tg | tt |
+===+====+====+====+====+====+====+====+====+====+====+====+====+====+====+====+====+
| 0 | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  |
+---+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
| 1 | 0  | 0  | 0  | 0  | 0  | 1  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0  |
+---+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+----+

.. |travis| image:: https://travis-ci.org/LucaCappelletti94/fasta_one_hot_encoder.png
   :target: https://travis-ci.org/LucaCappelletti94/fasta_one_hot_encoder

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_fasta_one_hot_encoder&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_fasta_one_hot_encoder

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_fasta_one_hot_encoder&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_fasta_one_hot_encoder

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_fasta_one_hot_encoder&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_fasta_one_hot_encoder

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/25fb7c6119e188dbd12c/maintainability
   :target: https://codeclimate.com/github/LucaCappelletti94/fasta_one_hot_encoder/maintainability
   :alt: Maintainability

.. |bases| image:: https://github.com/LucaCappelletti94/fasta_one_hot_encoder/blob/master/bases.png?raw=true
   :alt: Bases

.. |kmers| image:: https://github.com/LucaCappelletti94/fasta_one_hot_encoder/raw/master/kmers.png
   :alt: Kmers

.. |pip| image:: https://badge.fury.io/py/fasta_one_hot_encoder.svg
    :target: https://badge.fury.io/py/fasta_one_hot_encoder
