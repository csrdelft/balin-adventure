mkenv:
	pyvenv-3.4 .virtualenv

install:
	test -d .virtualenv || ${MAKE} mkenv
	. .virtualenv/bin/activate; pip install -r requirements

test:
	. .virtualenv/bin/activate; cd src && python manage.py test --keepdb

travis-install:
	pip install -r requirements

# do not use --keepdb here, unnecessary and complicates stuff if a test doesn't clean up
travis-test:
	cd src && python manage.py test
