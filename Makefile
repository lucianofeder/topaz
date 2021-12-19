SHELL := /bin/bash
VENV := source venv/bin/activate

all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

install: ## Install all dependecies and change to venv
	python -m venv venv --upgrade-deps && $(VENV) && pip install -r requirements.txt

run:	## Runs main.py
	$(VENV) && python main.py

test: ## Run tests
	$(VENV) && coverage run -m unittest discover tests/ -v

coverage: ## Test coverage
	$(VENV) && coverage run -m unittest discover tests/ && coverage report

coverage_html: ## Creates html for coverage
	$(VENV) && coverage run -m unittest discover tests/ && coverage html