VERSION=$(shell cat logger/VERSION)

.DEFAULT_GOAL = help
.PHONY = help
help:
	@echo "Commands:
	@echo "- build						: builds container images ."
	@echo "- kube						: runs kubernetes resources ."	
	@echo "- pkg						: installs package without dev dependencies ."
	@echo "- install					: installs package ."
	@echo "- install-dev				: installs package with all dependencies and precommit ."
	@echo "- check						: check if package is ready to commit (test and format) ."
	@echo "- check-format				: runs code static analysis ."
	@echo "- test						: runs code tests ."
	@echo "- badge						: runs badge generation ."
	@echo "- build-docs					: build docs ."
	@echo "- clean						: cleans side effects from commands ."

.PHONY = build
build:
	docker build -f ./container/hr-scraper/hr-scraper.Dockerfile -t hr-scraper .

.PHONY = prereq
prereq:
	sh ./scripts/file-handler.sh
	sh ./scripts/logger.sh

.PHONY = pkg
pkg: prereq
	poetry install --no-dev

.PHONY = install
install: prereq
	poetry install
	poetry run python -m pre_commit install

.PHONY = check
check: install check-format test badge clean

.PHONY = check-format
check-format:
	poetry run python -m black .
	poetry run python -m flake8
	poetry run isort .

.PHONY = test
test:
	poetry run pytest --cov-config=.coveragerc --cov=logger --cov-report html tests

.PHONY = badge
badge:
	poetry run coverage-badge -o badges/coverage.svg -f
	poetry run anybadge --value=$(VERSION) --file=badges/version.svg --label version -o

.PHONY = build-docs
build-docs:
	poetry run make -C docs html

.PHONY = clean
clean:
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '*.pytest_cache' -exec rm -rf {} +
	find . -name '*.pyo' -exec rm -rf {} +
	find . -name '*.ipynb_checkpoints' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name 'htmlcov' -exec rm -rf {} +
	find . -name '.coverage*' -exec rm -rf {} +
