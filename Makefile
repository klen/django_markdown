MODULE=django_markdown
VIRTUALENV=$(shell echo "$${VDIR:-'.env'}")

all: $(VIRTUALENV)

.PHONY: help
# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile

.PHONY: clean
# target: clean - Clean repo
clean:
	@rm -rf build dist docs/_build
	find $(CURDIR) -name "*.pyc" -delete
	find $(CURDIR) -name "*.orig" -delete
	find $(CURDIR) -name "__pycache__" | xargs rm -rf


# ==============
#  Bump version
# ==============

.PHONY: release
VERSION?=minor
# target: release - Bump version
release:
	@pip install bumpversion
	@bumpversion $(VERSION)
	@git checkout master
	@git merge develop
	@git checkout develop
	@git push --all
	@git push --tags

.PHONY: minor
minor: release

.PHONY: patch
patch:
	make release VERSION=patch

.PHONY: major
major:
	make release VERSION=major


# ===============
#  Build package
# ===============

.PHONY: register
# target: register - Register module on PyPi
register:
	@python setup.py register

.PHONY: upload
# target: upload - Upload module on PyPi
upload: clean docs
	@pip install twine wheel
	@python setup.py sdist bdist_wheel
	@twine upload dist/*

.PHONY: docs
# target: docs - Compile and upload docs
docs:
	@pip install sphinx sphinx-pypi-upload
	@python setup.py build_sphinx --source-dir=docs/ --build-dir=docs/_build --all-files
	@python setup.py upload_sphinx --upload-dir=docs/_build/html


# =============
#  Development
# =============


$(VIRTUALENV): requirements.txt
	[ -d $(VIRTUALENV) ] || @virtualenv --no-site-packages $(VIRTUALENV)
	@$(VIRTUALENV)/bin/pip install -r requirements.txt
	touch $(VIRTUALENV)

$(VIRTUALENV)/bin/py.test: requirements-tests.txt $(VIRTUALENV)
	@$(VIRTUALENV)/bin/pip install -r requirements-tests.txt
	touch $(VIRTUALENV)/bin/py.test

.PHONY: t
# target: t - Runs tests
t: clean $(VIRTUALENV)/bin/py.test
	@$(VIRTUALENV)/bin/py.test

$(CURDIR)/example/db.sqlite3: $(VIRTUALENV)
	$(VIRTUALENV)/bin/python example/manage.py syncdb --noinput

.PHONY: run
run: $(CURDIR)/example/db.sqlite3
	$(VIRTUALENV)/bin/python example/manage.py runserver

.PHONY: shell
shell: $(CURDIR)/example/db.sqlite3
	$(VIRTUALENV)/bin/python example/manage.py shell
