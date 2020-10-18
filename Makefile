THIS_FILE := $(lastword $(MAKEFILE_LIST))

.DEFAULT_GOAL := help

python-version: ## Provides the Python version
	pipenv run python --version
.PHONY: python-version

run: ## Run the app
	poetry run my-script
.PHONY: run

async-example: ## Run the async example
	poetry run async-example
.PHONY: async-example

test: ## Run the tests
	poetry run pytest -s tests
.PHONY: test

spec: ## Run the specs
	poetry run mamba spec --format=documentation
.PHONY: spec

repl: ## Fire up the Repl
	poetry run python
.PHONY: repl

help: ## Prints this help message
	@grep -h -E '^[a-zA-Z0-9\._-]+:.*?## .*$$' $(MAKEFILE_LIST) |\
		sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help
