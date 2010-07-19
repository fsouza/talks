all: unit

unit:
	@echo 'Running unit tests...'
	@nosetests -s --verbosity=2 -w tests/unit --with-coverage --cover-package=talks_application
