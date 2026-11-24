PYTHON ?= python

.PHONY: install test demos all

install:
	$(PYTHON) -m pip install -r requirements-research.txt

test:
	$(PYTHON) -m pytest research_lab/tests -q

demos:
	$(PYTHON) -m research_lab.run_all

all: test demos
