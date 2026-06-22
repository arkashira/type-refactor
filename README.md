**🛠️ type-refactor**


<div align="center">
  <a href="https://shields.io/">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT">
  </a>
  <a href="https://shields.io/">
    <img src="https://img.shields.io/badge/Python-3.9-blue.svg" alt="Python 3.9">
  </a>
  <a href="https://shields.io/">
    <img src="https://img.shields.io/badge/Build-Python%203.9-blue.svg" alt="Build: Python 3.9">
  </a>
  <a href="https://shields.io/">
    <img src="https://img.shields.io/github/stars/axentx/type-refactor" alt="Stars: 0">
  </a>
</div>


---
# 🚀 type-refactor
**Power Python developers with automated code refactoring.** A lightweight Python library that analyzes Python source files to identify potential rename refactor opportunities and produces safe change proposals for developers.


## Why type-refactor?
- **Lightweight**: 100% Python, no external dependencies.
- **Fast**: Real-time analysis of Python source files.
- **Accurate**: Safe change proposals generated with precision.
- **Flexible**: Supports medium-sized codebases.
- **Easy to use**: Simple API for developers to integrate.


## Feature Overview

| Feature | Description |
| --- | --- |
| RefactorEngine | Analyzes Python source files to identify potential rename refactor opportunities. |
| Proposal Generation | Generates safe change proposals for developers. |
| Unit Tests | Validates detection logic and proposal generation. |
| Python Support | Supports Python 3.9 and later versions. |


## Tech Stack

- **Python**: The project is built using Python 3.9.
- **ast**: The built-in Python module for parsing source code.
- **typing**: Used for type hints and documentation.


## Project Structure

```
type-refactor/
business/
docs/
src/
tests/
README.md
pyproject.toml
requirements.txt
```


## Getting Started

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```
2. **Run the project**:
```bash
python -m src.refactor_engine
```
3. **Test the project**:
```bash
python -m tests.test_refactor_engine
```


## Deploy

1. **Build the project**:
```bash
python -m build
```
2. **Package the project**:
```bash
python -m sdist
```
3. **Upload to PyPI**:
```bash
twine upload dist/*
```


## Status

Last updated: 2026-06-22T08:19:01.785336Z
Recent commit: feat(type-refactor): real, sandbox-tested implementation


## Contributing

Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on contributing to this project.


## License

This project is licensed under the MIT License.