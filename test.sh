coverage erase
pytest --cov=fasta_one_hot_encoder --cov-report xml:coverage.xml -s ./tests/
coverage combine --append
coverage report
coverage xml
#coveralls