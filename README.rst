fasta_one_hot_encoder
=========================================================================================
|travis| |sonar_quality| |sonar_maintainability| |codacy| |code_climate_maintainability| |pip| |downloads|

Simple python to lazily one-hot encode fasta files using multiple processes, either single bases or considering arbitrary kmers.

How do I install this package?
----------------------------------------------
As usual, just download it using pip:

.. code:: shell

    pip install fasta_one_hot_encoder

Tests Coverage
----------------------------------------------
Since some software handling coverages sometime get slightly different results, here's three of them:

|coveralls| |sonar_coverage| |code_climate_coverage|

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

Handling anonymous nucleotides
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
|anonymous_nucleotides|

In many datasets you will encounter either :code:`"n"` or :code:`"N"`, depending on the strand.
Just add an :code:`"n"` to the code

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

+---+---+---+---+---+---+
|   | a | c | g | t | n |
+===+===+===+===+===+===+
| 0 | 0 | 0 | 1 | 0 | 0 |
+---+---+---+---+---+---+
| 1 | 0 | 0 | 0 | 0 | 1 |
+---+---+---+---+---+---+
| 2 | 0 | 1 | 0 | 0 | 0 |
+---+---+---+---+---+---+

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

.. |bases| image:: https://github.com/LucaCappelletti94/fasta_one_hot_encoder/blob/master/bases.png?raw=true
   :alt: Bases

.. |anonymous_nucleotides| image:: https://github.com/LucaCappelletti94/fasta_one_hot_encoder/raw/master/anonymous_nucleotide.jpg
   :alt: Anonymous nucleotides

.. |kmers| image:: https://github.com/LucaCappelletti94/fasta_one_hot_encoder/raw/master/kmers.png
   :alt: Kmers

.. |travis| image:: https://travis-ci.org/LucaCappelletti94/fasta_one_hot_encoder.png
   :target: https://travis-ci.org/LucaCappelletti94/fasta_one_hot_encoder
   :alt: Travis CI build

.. |sonar_quality| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_fasta_one_hot_encoder&metric=alert_status
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_fasta_one_hot_encoder
    :alt: SonarCloud Quality

.. |sonar_maintainability| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_fasta_one_hot_encoder&metric=sqale_rating
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_fasta_one_hot_encoder
    :alt: SonarCloud Maintainability

.. |sonar_coverage| image:: https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_fasta_one_hot_encoder&metric=coverage
    :target: https://sonarcloud.io/dashboard/index/LucaCappelletti94_fasta_one_hot_encoder
    :alt: SonarCloud Coverage

.. |coveralls| image:: https://coveralls.io/repos/github/LucaCappelletti94/fasta_one_hot_encoder/badge.svg?branch=master
    :target: https://coveralls.io/github/LucaCappelletti94/fasta_one_hot_encoder?branch=master
    :alt: Coveralls Coverage

.. |pip| image:: https://badge.fury.io/py/fasta-one-hot-encoder.svg
    :target: https://badge.fury.io/py/fasta-one-hot-encoder
    :alt: Pypi project

.. |downloads| image:: https://pepy.tech/badge/fasta-one-hot-encoder
    :target: https://pepy.tech/badge/fasta-one-hot-encoder
    :alt: Pypi total project downloads 

.. |codacy|  image:: https://api.codacy.com/project/badge/Grade/b95f6c430646485c82a1f674253f4d42
    :target: https://www.codacy.com/app/LucaCappelletti94/fasta_one_hot_encoder?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=LucaCappelletti94/fasta_one_hot_encoder&amp;utm_campaign=Badge_Grade
    :alt: Codacy Maintainability

.. |code_climate_maintainability| image:: https://api.codeclimate.com/v1/badges/7c5ae881132b6622be2b/maintainability
    :target: https://codeclimate.com/github/LucaCappelletti94/fasta_one_hot_encoder/maintainability
    :alt: Maintainability

.. |code_climate_coverage| image:: https://api.codeclimate.com/v1/badges/7c5ae881132b6622be2b/test_coverage
    :target: https://codeclimate.com/github/LucaCappelletti94/fasta_one_hot_encoder/test_coverage
    :alt: Code Climate Coverate
