# Pytest Selenium Hybrid Framework

This project contains a hybrid test automation framework built with pytest and Selenium, designed for web testing. It leverages the power of Python's pytest framework for test execution and Selenium for browser automation.

## Features

- Integration of Pytest for test execution and reporting
- Utilizes Selenium for browser automation
- Currently, Supports only UI and API testing(Future)
- Implements page object model (POM) design pattern for improved code maintainability
- Configurable test data management using openpyxl or dict datatype in conftest.py files
- Easily extendable with custom test utilities and helper functions
- Modular architecture for better organization and re-usability
- Easy setup using only a requirement.txt file.
- Provides a hybrid approach, combining data-driven and keyword-driven testing techniques.

## Setup

1. **Install Python:** Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

2. **Install Dependencies:** Run the following command to install the required dependencies:

3. **Configuration:** git clone https://github.com/kranthikp/pythonSelFramework.git

4. **Installation** pip install -r requirements.txt

4. **Run Tests:** Execute the tests using the following command:
    > cd WORKSPACE/tests 
    > py.test

## Project Structure

The project structure is organized as follows:
- `.venv`: virtual env for python interpreter configuration.
- `tests`: Contains the test scripts written using Pytest.
- `pageObjects`: Page objects representing web pages.
- `utilities`: Utility functions and helper classes.
- `config.yml`: Configuration file for test environment settings.
- `requirements.txt`: List of Python dependencies.
- `logfile`: test logs using pytest build in logger library.
- `reports`: test execution report using --html=reports/report.html.

## Writing Tests

**tests:**
- Create test scripts under the `tests` directory.
- Create test scripts under the `tests/<module_name>` directory.
- Use Page Objects from the `pages` directory for interacting with web elements.
- Utilize fixtures for setup and teardown activities in conftest.py

## Reporting

Pytest generates detailed HTML reports after test execution. You can find the reports in the `reports` directory.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.
