.PHONY: tests docs

env:
	@echo "Activating virtual environment..."
	poetry shell

dependencies:
	git config --global init.defaultBranch main 
	@echo "Initializing Git..."
	git init
	@echo "Installing dependencies..."
	poetry install
	poetry run pre-commit install

install:
	pip3 install --upgrade pip &&\
	pip3 install --upgrade setuptools &&\
	pip3 install -r requirements.txt

base: env dependencies

tests:
	pytest

docs:
	@echo Save documentation to docs... 
	pdoc src -o docs --force
	@echo View API documentation... 
	pdoc src --http localhost:8080