.ONESHELL:
.PHONY: clean clean-test clean-pyc clean-build build help
.DEFAULT_GOAL := help


define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

bootstrap: ## Installs python requirements globally on system. For use only within containerized environements
	python3 -m pip install -r requirements.txt --disable-pip-version-check --break-system-packages

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +
	find . -name '.pytest_cache' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr test_results/
	rm -f *report.html
	rm -f log.html
	rm -f test-results.html
	rm -f output.xml

build: clean ## Build source and wheel package
	echo "Intentionally not implemented"

test: clean ## Run unit tests with pytest
	python3 -m pytest

test-debug: ## Run unit tests with debugging enabled
	python3 -m pytest --pdb

test-coverage: clean ## Run unit tests and check code coverage
	PYTHONPATH=src python3 -m pytest --cov=src tests/ --disable-warnings

test-acceptance: clean ## Run acceptance tests with RobotFramework
	mkdir -p ./test_results/robot; \
	python3 -m robot --pythonpath=./src --outputdir=./test_results/robot tests/robot/;

test-all: test-coverage test-acceptance ## Run both unit and acceptance tests with coverage report

prepare-results:
	cp ./test_results/robot/report.html ./test_results/index.html
	cp ./test_results/robot/log.html ./test_results/log.html
	cp ./test_results/robot/output.xml ./test_results/output.xml

run: ## Run game as-is to explore functionality
	cd src && python3 -m levelup


## 
## DO NOT RUN ANYTHING BELOW THIS LINE !!!!!!!!
## 


## Installs python requirements into virtual environment
bootstrap-venv:
	python3 -m pip install --upgrade pip poetry
	poetry config virtualenvs.in-project true
	- rm -rf ./.venv
	poetry install

## Rebuilds requirements.txt from poetry.lock
bootstrap-venv-reqs:
	poetry export --without-hashes --format=requirements.txt > requirements.txt

## Launches shell within virtual environment if venv is found
shell:
	- @test ! -d ./.venv && echo "Virtual environment not found. Please run 'make bootstrap-venv' to create it"
	- @test -d ./.venv && poetry shell

## Only use within GitHub Actions
ci-build:
	echo "Intentionally not implemented"

## Only use within GitHub Actions
ci-bootstrap:
	python3 -m pip install -r requirements.txt --disable-pip-version-check

## Only use within GitHub Actions
ci-test:
	PYTHONPATH=src python3 -m pytest --cov=src tests/ --disable-warnings

## Only use within GitHub Actions
ci-test-acceptance: clean
	mkdir -p ./test_results/robot; \
	python3 -m robot --pythonpath=./src --outputdir=./test_results/robot tests/robot/;
