This project is intended to be used as a type _hinting_ system for a related project, `practical_astronomy`, and has been developed in conjunction with that project. It may be useful for other projects as well.

It is a defined vocabulary of commonly used astronomical terms represented in code.

It felt plausible that it would be useful in other projects as well, so it has been spun off into an indepdenent file.

# Install

`pip install astronomy-types`

# How to use?

`import astronomy_types`

See `astronomy_types.py` for currently implemented types.

## Set a return type for a function

`def degrees_to_decimal_degrees(degrees: astronomy_types.Degrees) -> astronomy_types.DecimalDegrees`

# Updating and Repackaging the Project with `setuptools`

To update and repackage this Python project using `setuptools` on macOS, follow these steps:

## 1. Install or Activate the Virtual Environment

It's recommended to use a virtual environment for isolation. If you don't already have a virtual environment, create and activate one:

### Create and start virtual environment:

```bash
python3 -m venv
```

```bash
source venv/bin/activate
```

## 2. Install Required Dependencies

Ensure that setuptools and wheel are installed in your environment:

```bash
pip install setuptools wheel twine
```

or

```bash
pip install -r requirements.txt
```

## 3. Update version number

```bash
setup(
    name="astronomy_types",
    version="0.2.0",  # Update this to the new version number
    ...
)
```

## 4. Build the dist

```bash
python3 setup.py sdist bdist_wheel
```

## 5. Upload with `twine`

```bash
twine upload dist/*
```

And enter in the API token when prompted
