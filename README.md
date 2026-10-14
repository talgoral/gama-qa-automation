# GAMA QA Automation

## Overview

A Python-based UI test automation project using
Playwright and pytest.

The project aims to build a maintainable test
automation framework through a risk-based testing
approach and gradual expansion of test coverage.

## Technology Stack

- Python
- Playwright
- pytest
- Git and GitHub

## Project Status

Initial project setup completed.

Test planning, website exploration, and framework
development are in progress.

## Safety and Scope

Automated tests against GAMA environments will only
be executed after the required authorization and
test environment have been confirmed.

## Installation

Create and activate a Python virtual environment,
then install the dependencies:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

## Running Tests

```powershell
python -m pytest -v
```