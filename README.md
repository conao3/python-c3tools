# c3tools

A collection of command-line utilities for everyday development tasks. Built with Python and Typer for a clean, intuitive interface.

## Features

- **JSON/YAML Processing** - Transform and query data using JMESPath expressions
- **String Manipulation** - Convert between naming conventions (camelCase, PascalCase)
- **Random Generation** - Generate UUIDs and random character strings
- **OpenAPI Utilities** - Generate OpenAPI schemas from sample data

## Installation

```bash
pip install c3tools
```

Or install from source using Poetry:

```bash
git clone https://github.com/conao3/python-c3tools.git
cd python-c3tools
poetry install
```

## Usage

### JSON Processing

Convert JSON to JSON or YAML with optional JMESPath queries:

```bash
# Pretty print JSON
echo '{"name": "example"}' | c3tools json json

# Query with JMESPath
echo '{"items": [1, 2, 3]}' | c3tools json json --query "items[0]"

# Convert JSON to YAML
echo '{"name": "example"}' | c3tools json yaml
```

### YAML Processing

Convert YAML to JSON or YAML with optional JMESPath queries:

```bash
# Convert YAML to JSON
echo 'name: example' | c3tools yaml json

# Query YAML data
echo 'items: [1, 2, 3]' | c3tools yaml yaml --query "items"
```

### String Transformation

Convert strings between different naming conventions:

```bash
# Convert to camelCase
echo "hello_world" | c3tools string camel
# Output: helloWorld

# Convert to PascalCase
echo "hello_world" | c3tools string pascal
# Output: HelloWorld
```

### Random Generation

Generate random values:

```bash
# Generate a UUID
c3tools random uuid

# Generate random hex characters
c3tools random chars --length 16
c3tools random chars --length 8 --prefix "id_" --suffix "_v1"
```

### OpenAPI Schema Generation

Generate OpenAPI components from sample data:

```bash
# Generate response schema from JSON
echo '{"id": 1, "name": "test"}' | c3tools glams oas-response

# Parse and format parameters
echo 'id:path:string' | c3tools glams oas-parse-parameter
```

## Requirements

- Python 3.10+
- Dependencies: typer, jmespath, pyyaml, jinja2, pydantic

## Development

```bash
# Install development dependencies
poetry install

# Format code
poetry run black src/
poetry run isort src/

# Lint
poetry run flake8 src/
```

## License

MIT License

## Author

Naoya Yamashita (conao3@gmail.com)
