MODULE=django_markdown

clean:
	sudo rm -rf build dist django_markdown.egg-info
	find . -name "*.pyc" -delete
	find . -name "*.orig" -delete

install: remove _install clean

register: _register clean

remove:
	sudo pip uninstall $(MODULE)

upload: _upload clean _commit

test:
	cd example_project && ./manage.py test main

_install:
	sudo pip install -U .

_upload:
	python setup.py sdist upload

_commit:
	git add .
	git add . -u
	git commit
	git push origin
	git push intaxi

_register:
	python setup.py register
