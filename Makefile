SHELL=/bin/bash
FILES=tarjan/tarjan.py
PYTHON=/usr/bin/env python

build:
	$(PYTHON) setup.py build

install: build
	sudo $(PYTHON) setup.py install \
		--record installed-files.txt \
		--single-version-externally-managed

uninstall:
	@if [ -e "installed-files.txt" ]; then \
		while read path; do \
			echo $${path}; \
			sudo rm -rf $${path}; \
		done < "installed-files.txt"; \
	fi

test:
	$(PYTHON) setup.py test

tox:
	tox --skip-missing-interpreters --develop

pep8:
	$(PYTHON) -m pep8 $(FILES) --show-source

clean:
	rm -rf .tox
	rm -rf .eggs
	rm -rf tarjan.egg-info
