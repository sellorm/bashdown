all: README.md

README.md: README.bashdown bashdown
	bashdown README.bashdown > README.md

build:
	poetry build

test:
	python3 -m unittest
