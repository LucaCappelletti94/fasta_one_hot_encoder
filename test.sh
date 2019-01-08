rm -rf .coverage
coverage erase
pytest --cov=fasta_one_hot_encoder --cov-report xml:coverage.xml 
coverage combine --append
coverage report
coverage xml