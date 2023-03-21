# bashdown

A markdown pre-processor for inline bash.

Have you ever written a command line tool and wanted to include it's output
in your documentation?

Then bashdown is for you.

Write your markdown files as usual and include bash code sections as normal
using "```bash".

When you pass this file through bashdown, it will run the code in the
code block and include that output inside the rest of the markdown.

This README.md was generated using bashdown.
Check README.bashdown for the file that's used to generate README.md

This project was inspired by tools like quarto and Rmarkdown, but has
significantly fewer dependencies due to it's much more limited scope.

## Usage

Basic usage is as follows:

```bash
# bashdown README.bashdown > README.md
```

Full usage information can be obtained from the built in help.

```bash
bashdown --help
```

```output
usage: bashdown [-h] filename

Processes in-line bash in markdown files

positional arguments:
  filename

optional arguments:
  -h, --help  show this help message and exit

For more information please see the docs
```


## License

MIT © Mark Sellors

