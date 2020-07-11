THIS_FILE := $(lastword $(MAKEFILE_LIST))

.DEFAULT_GOAL := help

python-version: ## Provides the Python version
	pipenv run python --version
.PHONY: python-version

run: ## Run the app
	pipenv run python __main__.py
.PHONY: run

test: ## Run the tests
	pipenv run pytest -s
.PHONY: test

spec: ## Run the specs
	@pipenv run mamba spec --format=documentation
.PHONY: spec

repl: ## Fire up the Repl
	pipenv run python
.PHONY: repl

help: ## Prints this help message
	@grep -h -E '^[a-zA-Z0-9\._-]+:.*?## .*$$' $(MAKEFILE_LIST) |\
		sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help
