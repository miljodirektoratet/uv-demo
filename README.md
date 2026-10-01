# UV demo

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![TestPyPI](https://img.shields.io/badge/TestPyPI-latest-blue)](https://test.pypi.org/project/uv_demo/) [![Coverage](https://codecov.io/gh/miljodirektoratet/uv_demo/branch/main/graph/badge.svg)](https://codecov.io/gh/miljodirektoratet/uv_demo) [![Safety](https://img.shields.io/badge/Safety-Dashboard-blue)](https://platform.safetycli.com/codebases/uv_demo/findings)

A demo repository showcasing Python project development and packaging best practices using [uv](https://docs.astral.sh/uv/getting-started/installation/). This project demonstrates project structure, dependency management, containerization with Docker and automated code quality, security scanning and deployment workflows using GitHub Actions (GHA).

**Table of Contents:**

- [Project Overview](#project-overview)
  - [Key Features](#key-features)
  - [Repository Structure](#repository-structure)
  - [Docker Configuration](#docker-configuration)
  - [Workflow Statuses](#workflow-statuses)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Development](#development)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Development Workflow](#development-workflow)
  - [Code Quality Standards](#code-quality-standards)
  - [GHA Workflows](#gha-workflows)
  - [Local Development Commands](#local-development-commands)
  - [Branch Protection](#branch-protection)
- [Documentation](#documentation)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Project Overview

This repository serves as a demonstration and learning resource. To use this as a template for new projects, refer to the [setup guide](./docs/setup-guide.md) in the documentation.

### Key Features

<!-- List key features and capabilities -->

- **Python packaging**:
  - Dependency management with uv
  - Automated versioning using setuptools-scm
- **GHA** workflows for CI/CD and security:
  - Code quality checks with pre-commit, ruff, mypy, and pytest
  - Security scans with Safety, CodeQL, Dependabot, and Zizmor
  - Python package deployment to Test PyPI
  - Container image deployment to GitHub Container Registry
- **Developer tools**: VS Code integration, development containers, Taskfile automation

### Repository Structure

<!-- Directory layout -->

Important configurations files are listed below, full overview of the repository structure is available in the [Repository Structure](./docs/repo-structure.md) documentation.

| File/Directory       | Purpose                                                                                                                                                                                                  |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `.devcontainer/`     | VS Code dev container configuration                                                                                                                                                                      |
| `.github/workflows/` | GitHub Actions for CI/CD (see [GitHub Actions Workflows](#github-actions-workflows)).                                                                                                                    |
| `pyproject.toml`     | Python package configuration, dependencies, and build settings                                                                                                                                           |
| `Taskfile.yml`       | Automated tasks for setting up the dev environment, running code quality checks and more. Run `task help` to see all available tasks or refer to the [Command Cheatsheet](./docs/command-cheatsheet.md). |

### Docker Configuration

<!-- Add only if applicable -->

This project includes multiple Docker configurations to support development, testing and deployment:

- **Development Container**: Configured via `.devcontainer/devcontainer.json` for use with VS Code Dev Containers and GitHub Codespaces
- **Testing Container**: Docker Compose setup for local testing that reproduces the production environment. Start with `docker-compose up --build`
- **Production Container**: [Dockerfile](./Dockerfile) for building production-ready container images, automatically deployed to GitHub Container Registry (GHCR) via GitHub Actions workflow: [./github/workflows/cd-docker.yml](./.github/workflows/cd-docker.yml)

For detailed development container configuration and customization instructiosn, see the[setup-guide](./docs/setup-guide.md).

### Workflow Statuses

| Job                        | Status                                                                                                                                       | Description                             |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| **CI Python**              | ![Status](https://img.shields.io/github/actions/workflow/status/miljodirektoratet/uv-demo/ci-python.yml?branch=main&label=&style=flat)   | Code quality checks, testing, coverage  |
| **CD Python**              | ![Status](https://img.shields.io/github/actions/workflow/status/miljodirektoratet/uv-demo/cd-python.yml?label=&style=flat)               | Package deployment to Test PyPI         |
| **CI Docker**              | ![Status](https://img.shields.io/github/actions/workflow/status/miljodirektoratet/uv-demo/ci-docker.yml?branch=main&label=&style=flat)   | Build and test Docker image             |
| **CD Docker**              | ![Status](https://img.shields.io/github/actions/workflow/status/miljodirektoratet/uv-demo/cd-docker.yml?label=&style=flat)               | Container deployment to GitHub Registry |
| **Security Scan - CodeQL** | ![Status](https://img.shields.io/github/actions/workflow/status/miljodirektoratet/uv-demo/scan-codeql.yml?branch=main&label=&style=flat) | Python and GHA security analysis        |
| **Dependabot**             |                                                                                                                                              | Automated dependency updates            |

Results of the security scans are visible in the [Security](https://github.com/miljodirektoratet/uv-demo/security/code-scanning) tab of the GitHub repository.

## Getting Started

The **uv-demo** package is a minimal package with a single function that prints the package name. You can install this package from [Test PyPI](https://test.pypi.org/project/uv-demo/) or pull the containerized version from [GHCR](https://github.com/miljodirektoratet/uv-demo/pkgs/container/uv-demo). The main purpose of this repository is to explore development tools and observe the CI/CD pipeline in action. To get started, follow the steps in the [Development Workflow](#development-workflow) section..

### Installation

> [!NOTE]
> This package is published to Test PyPI for demonstration purposes. Test PyPI is a testing environment for package deployment without affecting the official PyPI index. If you're using this package in production, ensure it's published to the official PyPI index.

Install the package from Test PyPI:

```bash
pip install -i https://test.pypi.org/simple/ uv-demo
```

```python
import uv_demo
uv_demo.main()
# > Hello from uv-demo!
# > Version: x.x.x
```

Or pull and run the container:

```bash
docker pull ghcr.io/miljodirektoratet/uv-demo:latest

docker run --rm ghcr.io/miljodirektoratet/uv-demo:latest
# > Hello from uv-demo!
# > Version: x.x.x
```

## Development

> [!TIP]
> **Recommended Setup:** Use [GitHub Codespaces](https://github.com/features/codespaces) or [VS Code Devcontainers](https://code.visualstudio.com/docs/devcontainers/containers) for a consistent environment. Alternative option is to install the project locally using uv.

The following steps configure your development environment using VS Code Dev Containers. For local setup without containers, refer to the [setup guide](./docs/setup-guide.md) in the documentation.

### Prerequisites

- [Docker](https://docs.docker.com/engine/install/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [VS Code Dev Containers](https://code.visualstudio.com/docs/devcontainers/containers) extension

### Setup

1. **Open the project**: Clone and open the project folder in VS Code or use [GitHub Codespaces](https://docs.github.com/en/codespaces).

2. **Start the devcontainer**: When prompted, reopen the folder in the Devcontainer. If not prompted, manually trigger it via the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`) and select "Dev Containers: Reopen in Container".

3. **Automatic setup**: The devcontainer automatically:
   - Configures VS Code with recommended settings and extensions per [devcontainer.json](.devcontainer/devcontainer.json)
   - Installs development tools: [Git](https://git-scm.com/), [uv](https://docs.astral.sh/uv/), [pre-commit](https://pre-commit.com/), [Task](https://taskfile.dev/installation/)
   - Sets up the Python environment with dependencies in `.venv` via `task dev-setup`, which runs `uv sync --dev` and executes code quality checks and test coverage

4. **Test the installation with Task commands**:

   Task is used to automate common development tasks _(see [Taskfile.yml](Taskfile.yml))_.

   ```bash
   # Test the package
   task run
   # or
   uv run uv-demo

   # Run quality checks
   task check

   # Run local CI workflow
   task ci-local

   # Clean up
   task clean
   ```

5. **Test the notebook**: Open `notebooks/demo.ipynb` and select the `.venv` kernel. If you have problems activating the `.venv` refer to the [setup guide](./docs/setup-guide.md).

6. **Configure the GitHub Repository**: If you fork this repository or use it to create a new repository from scratch, you'll need to configure your GitHub repository to connect with **Test PyPI**, **Safety** and **Code Coverage**. Also, verify that your **security scans** are properly set up. See the **GitHub Repository Configuration** section in the [setup guide](./docs/setup-guide.md) for instructions.

## Development Workflow

1. **Setup**:
   - Follow the setup instructions above or refer to the [Installation Guide](docs/installation.md).
   - Follow the demo walkthrough in the [Quick Start Guide](docs/demo-quickstart.md)

2. **Develop**:
   - Create a branch for your feature or bug fix: `feat/<name>` or `fix/<name>`.
   - Make your changes.For example develop package functions in `src/` or add notebooks to `notebooks/`.
   - Ensure code meets the quality standards by running `task check`.
   - Ensure tests are written for new features and pass `task test`.

3. **Integrate**:
   - Check that all CI tests pass locally with `task ci-local`.
   - Push your branch to GitHub.
   - Create a pull request against the `main` branch.
   - Await review and merge; your branch will be automatically deleted after merging.

4. **Deploy**:
   - Create a git tag for releases (e.g., `0.0.1`) using `task tag`.
   - Create a PR from `release/<version>` to `main` to deploy the new release.
   - Once merged to `main`, the CD workflows are triggered:
     - CD Python automatically builds and publishes the package to Test PyPI.
     - CD Docker builds and pushes the container image to GitHub Container Registry.

5. **Clean up**:
   - Clean up dev files and artifacts with `task clean`.
   - Clean up local git:
     - enable pruning: `git config --global fetch.prune true`
     - delete merged branch locally: `git branch -d <branch-name>`

### Code Quality Standards

Follow PEP8, use type hints, and include docstrings in reStructuredText format. All quality checks are automated through Task commands, pre-commit hooks and CI workflows.

See the [Code Quality and Security Standards](./docs/code-and-security-standards.md) guide to see which rules are enforced in this repo.

### GHA Workflows

The repository includes automated workflows for code quality, security, and deployment:

| Workflow            | Trigger                            | Purpose                                 |
| ------------------- | ---------------------------------- | --------------------------------------- |
| **CI Python**       | `push`, `pull_request` to `main`   | Code quality checks, testing, coverage  |
| **CD Python**       | `push` to `main` with version tags | Package deployment to Test PyPI         |
| **CD Docker**       | `push` to `main` with version tags | Container deployment to GitHub Registry |
| **CodeQL Analysis** | `push`, `pull_request`, `schedule` | Code security analysis                  |

The demo workflows can be customized or removed based on your specific project requirements. At minimum, I recommend including the **CI Python** workflow for code quality and testing, as well as the Security workflow: **CodeQL**.

### Local Development Commands

Use these commands for local development and testing:

```bash
# Setup and quality checks
task install          # Install dependencies and setup environment
task check            # Run all quality checks
task ci-local         # Simulate CI pipeline locally

# Testing and running
task test             # Run test suite
task run              # Run the demo package
task run-docker       # Run in Docker container


# Code formatting and security
task format           # Format code with ruff
task security         # Run security scans

# Build and release
task build            # Build Python package
task tag 0.0.1        # Prepare a new release (create git tag)
```

For more commands see: [Command Cheatsheet](./docs/command-cheatsheet.md)

### Branch Protection

The `main` branch is protected with the following rules:

- Require pull request reviews before merging
- Require status checks to pass before merging
- Require branches to be up to date before merging

## Documentation

- [Setup Guide](./docs/setup-guide.md)
- [Demo Quick Start Guide](./docs/demo-quickstart.md)
- [Code Quality and Security Standards](./docs/code-and-security-standards.md)
- [Command Cheatsheet](./docs/command-cheatsheet.md)
- [Repository Structure](./docs/repo-structure.md)
- [Troubleshooting Guide](./docs/troubleshooting.md)

## Acknowledgements

This project incorporates best practices from the Python and DevOps communities, including:

- Astral-sh's [uv Documentation](https://docs.astral.sh/uv/) and Docker configuration example [astral-sh/uv-docker-example](https://github.com/astral-sh/uv-docker-example)
- GitHub Template: [uv-template](https://github.com/miljodirektoratet/uv-template)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
