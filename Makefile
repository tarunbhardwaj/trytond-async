test: test-sqlite test-postgres test-flake8

test-postgres: install-dependencies
	python setup.py test

test-flake8:
	pip install flake8
	flake8 .

install-dependencies:
	CFLAGS=-O0 pip install lxml
	pip install --upgrade -r dev_requirements.txt
