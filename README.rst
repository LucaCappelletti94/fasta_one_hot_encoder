Fasta One-Hot Encoder
=================================
|travis| |sonar_quality| |sonar_maintainability| |sonar_coverage| |code_climate_maintainability| |pip|

Simple python to lazily one-hot encode fasta files using multiple processes.

Installation
---------------
Simply run:

.. code:: bash

    pip installed fasta_one_hot_encoder

Example
---------------

.. code:: python

    from fasta_one_hot_encoder import FastaOneHotEncoder
    import numpy as np

    encoder = FastaOneHotEncoder(
        nucleotides = "acgtn",
        lower = False
    )
    path = "test_data/my_test_fasta.fa"
    encoded = encoder.transform(path, verbose=True)
    np.save(path, encoded)


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

.. |pip| image:: https://badge.fury.io/py/fasta_one_hot_encoder.svg
    :target: https://badge.fury.io/py/fasta_one_hot_encoder
