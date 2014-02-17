ENVDIR = ./env
ENVBIN = $(ENVDIR)/bin
COVERAGE = $(ENVBIN)/coverage
FLAKE8 = $(ENVBIN)/flake8
PYTEST = $(ENVBIN)/py.test
PIP = C_INCLUDE_PATH="/opt/local/include:/usr/local/include" $(ENVBIN)/pip
PYTHON = $(ENVBIN)/python
PYTHON_VERSION = python2.7
TOX = $(ENVBIN)/tox
VIRTUALENV = virtualenv
VIRTUALENVOPTS = --python=$(PYTHON_VERSION)

.PHONY: help clean clean-pyc clean-build list test test-all coverage docs release sdist requirements req virtualenv

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "lint - check style with flake8"
	@echo "release - package and upload a release"
	@echo "requirements - install requirements from requirements.txt"
	@echo "sdist - package"
	@echo "test - run tests quickly with the default Python"
	@echo "testall - run tests on every Python version with tox"
	@echo "virtualenv - create project virtualenv"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint: .req
	$(FLAKE8) {{ cookiecutter.repo_name }} test

test: .req
	$(PYTEST) --ignore $(ENVDIR)

test-all: .req
	$(TOX)

coverage: .req
	$(COVERAGE) run --source {{ cookiecutter.repo_name }} setup.py test
	$(COVERAGE) report -m
	$(COVERAGE) html
	open htmlcov/index.html

docs:
	rm -f docs/{{ cookiecutter.repo_name }}.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ {{ cookiecutter.repo_name }}
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

release: clean
	$(PYTHON) setup.py sdist upload
	$(PYTHON) setup.py bdist_wheel upload

sdist: clean
	$(PYTHON) setup.py sdist
	$(PYTHON) setup.py bdist_wheel upload
	ls -l dist

virtualenv: $(ENVDIR)
$(ENVDIR):
	$(VIRTUALENV) $(VIRTUALENVOPTS) $(ENVDIR)

requirements:
	@rm -f .req
	$(MAKE) .req

req: .req
.req: $(ENVDIR) requirements.txt
	$(PIP) install -r requirements.txt
	@touch .req
