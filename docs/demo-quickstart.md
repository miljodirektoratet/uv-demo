# Demo - Quick Start Guide

This demo walks you through the different functionality available in this project. Ensure to complete the [setup guide](setup-guide.md) first. It is recommended to use VS Code as IDE and to install Task.

- [1. Test the Package](#1-test-the-package)
- [2. Explore Development Commands](#2-explore-development-commands)
- [Testing Different Features](#testing-different-features)
- [Next Steps](#next-steps)
- [Command Reference](#command-reference)

## 1. Test the Package

```bash
# Run the main CLI command
task run
# → "Hello from uv-demo!"
# → "Version: xxxx"

# Alternative without Task
uv run uv_demo
```

## 2. Explore Development Commands

```bash
# See all available tasks
task --list

# Complete development setup (one-time)
task dev-setup

# Run development checks
task check
# This runs: formatting, linting, type checking, tests, and dependency analysis

# single commands:
task lint-fix           # Format and lint code
task build              # Build the package
```

For complete command reference, see [Command Cheatsheet](./command-cheatsheet.md).

### 3. Try the Jupyter Notebook

- Open `notebooks/demo.ipynb` and select the `.venv` kernel.
- Run the cells to see how to use the package inside a notebook.

## Testing Different Features

### 1. Code Quality Tools

```bash
# See linting in action (introduce an error first)
echo "import os  # unused import" >> src/uv_demo/__init__.py
task check  # Should show the linting error

# Fix it automatically
task lint-fix
```

### 2. Testing Framework

```bash
# Run tests with coverage
task test-html

# Open coverage report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
```

### 3. Pre-commit Hooks

```bash
# Test pre-commit hooks
echo "test_bad_code = 'not formatted'" >> src/uv_demo/__init__.py
git add .
git commit -m "Test commit"  # Should trigger pre-commit checks
```

### 4. Package Building

```bash
# Build and inspect the package
task build
ls dist/  # Should show .tar.gz and .whl files

# Test installation
pip install dist/uv_demo-*.whl
uv_demo
pip uninstall uv_demo
```

## Next Steps

1. **Learn development workflow**: Read the [Setup Guide](./setup-guide.md)
2. **Understand code quality**: Check out [Code and Security Standards](./code-and-security-standards.md)
3. **Contribute**: Follow the development practices in the guides

## Command Reference

See [Command Cheatsheet](./command-cheatsheet.md) for all available commands organized by tool.

### Common Taskfile Commands

```bash
# Development
task install          # Install dependencies
task format           # Format code with Ruff
task lint-fix          # Fix linting issues
task test-html         # Run tests with HTML coverage report

# Code quality
task check            # Run all quality checks (lint, typecheck, test, deps)
task pre-commit       # Run pre-commit hooks on all files

# Build and release
task build            # Build the package
task clean            # Clean build artifacts
task tag VERSION=v1.0.0  # Create and push version tag

# Help
task help             # Show detailed workflow help
```
