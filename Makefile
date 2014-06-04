BUILDDIR=_build
MODULE=django_markdown
SPHINXBUILD=sphinx-build
ALLSPHINXOPTS= -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .
VIRTUALENV=$(shell echo "$${VDIR:-'.env'}")

all: $(VIRTUALENV)

$(VIRTUALENV): requirements.txt
	@virtualenv --no-site-packages $(VIRTUALENV)
	@$(VIRTUALENV)/bin/pip install -M -r requirements.txt
	touch $(VIRTUALENV)

.PHONY: help
# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile

.PHONY: clean
# target: clean - Display callable targets
clean:
	@rm -rf build dist docs/_build
	@rm -f *.py[co]
	@rm -f *.orig
	@rm -f */*.py[co]
	@rm -f */*.orig

.PHONY: register
# target: register - Register module on PyPi
register:
	@python setup.py register

.PHONY: sdist
sdist:
	@python setup.py sdist

.PHONY: upload
# target: upload - Upload module on PyPi
upload: docs
	@python setup.py sdist upload || echo 'Upload already'

.PHONY: docs
# target: docs - Compile and upload docs
docs:
	@pip install sphinx sphinx-pypi-upload
	@python setup.py build_sphinx --source-dir=docs/ --build-dir=docs/_build --all-files
	@python setup.py upload_sphinx --upload-dir=docs/_build/html

.PHONY: t
# target: t - Runs tests
t: clean
	$(VIRTUALENV)/bin/python setup.py test

$(CURDIR)/example/db.sqlite3:
	$(VIRTUALENV)/bin/python example/manage.py syncdb --noinput

.PHONY: run
run: $(CURDIR)/example/db.sqlite3
	$(VIRTUALENV)/bin/python example/manage.py runserver

.PHONY: shell
shell: $(CURDIR)/example/db.sqlite3
	$(VIRTUALENV)/bin/python example/manage.py shell
