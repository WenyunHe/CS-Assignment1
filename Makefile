SHELL = /usr/bin/env bash -o pipefail

default: help

.PHONY: help
help:
	# Usage:
	@sed -n '/^\([a-z][^:]*\).*/s//    make \1/p' $(MAKEFILE_LIST)

.PHONY: backend/install
backend/install:
	cd backend; \
	python3 -m venv env; \
	source env/bin/activate; \
	pip install -r requirements.txt; \

.PHONY: backend/test
backend/test: 
	cd backend; \
	source env/bin/activate; \
	python -m unittest; \

.PHONY: backend/run
backend/run:
	cd backend; \
	source env/bin/activate; \
	source .env; \
	python app.py; \

.PHONY: frontend/lint
frontend/lint:
	cd frontend && npm run lint

.PHONY: frontend/install
frontend/install:
	cd frontend && npm install

.PHONY: frontend/run
frontend/run:
	cd frontend && npm run dev

.PHONY: install
install: backend/install frontend/install 

.PHONY: unittest
unittest: backend/test 
