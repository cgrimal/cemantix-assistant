# Cemantix Assistant

[Cémantix](https://cemantix.herokuapp.com/)

## Installation

You should create a virtual environment first with your preferred tool.

Then install the project with [poetry](https://python-poetry.org/):

```bash
poetry install
```

## Usage

Extraire ses "guesses" en allant dans le local storage de son navigateur, et extraire la valeur de la clé "guesses" et la coller telle-quelle dans un fichier, comme `input/guesses.json`.

```bash
cemantix-assistant -g ./input/guesses.json
```

## Contributing

### Dependencies

Adding dependencies to the project can be done with a simple:

```bash
poetry add <package-name>
```

### Formatting

Always run `black` and `isort` on all the code of the package (including the example project):

```bash
black src
isort src
```

### Additional linter

Even though `black` does a great job a formatting the code, some lint warnings can sneak through it, so
we also use `flake8` (with a custom configuration):

```bash
flake8 src
```

### Type hinting

To check the type hinting is correct, simply run:

```bash
mypy --pretty src
```
