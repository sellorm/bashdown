all: README.md

README.md: README.bashdown bashdown
	bashdown README.bashdown > README.md
