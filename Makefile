MASTER_VERSION := $(shell grep '^version = .*$$' pyproject.toml | awk '{print $$3}')
all: README.md

README.md: README.bashdown bashdown
	bashdown README.bashdown > README.md

build:
	-rm -r ./dist/*
	poetry build

test:
	python3 -m unittest

version:
	sed -i "s/^__version__ = .*$$/__version__ = \"$(MASTER_VERSION)\"/g" bashdown/__init__.py

upload:
	twine upload dist/*
