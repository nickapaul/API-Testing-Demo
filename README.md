# Demo API Test Project

This project is a demonstration of how I would automate an API testing suite in a pipeline so that we can run our test on multiple triggers but also get a report back that we can read for our tests. First you can see that this suite is very light weight and is very quick. I like these because we can gate these tests (like I have in this project) in our pipeline. We can set it so that to check into QA, you must pass all the regression tests. Also to get to UAT you must pass all regression and all current sprint tests (those in sprint automated tests can then be moved to regression at sprint end). This is the Assurance in the phrase Quality Assurance. Running as many fast tests as possible at all merge points to get our coverage as high as possible at the speed we want to deploy changes. Thus, shifting left. If a bug were to go to PROD, we will have the tools to remediate it quickly and protect ourselves from losses.

## Getting Started
### Usage


1. **Python**: Make sure Python 3.10 is installed.
2. **Install Dependencies**: Run the following command:
    ```bash
    pip install -r requirements.txt
    ```
3. **Run Tests**: You can do this by debugging and running on your IDE of choice or you can run them in the terminal with the following command:
    ```bash
    pytest
    ```
    If you want to create a XML report, run this command instead:
    ```bash
    pytest --junitxml=Reports/report.xml
    ```

## Test Project Overview
For the test project part of the demonstration:
- **Organization**: I have created test classes that test different groups of endpoints that are related to each other. For example, all the tests that are related to the ‘/auth’ endpoint are grouped together. 
- **Dynamic Configuration**: I have examples of a config file and the configurations being passed from test to test. This can be used with a tool like Vault to keep secrets out of source. 
- **Gherkin**: Also shown, helper methods to abstract the scripting of the tests so the tests can be written as BDD as possible. The goal is that if a business analyst with no coding experience were to look the test name and the code, they could identify what the test is trying to accomplish. 
- **Validate Source Of Truth**: We could also extend this project to add the ability to make SQL queries to the database as well as add message to Kafka topics (and read from them). 

This is a very powerful tool to test the endpoint and validate the data source of truth, making it easier and faster to debug and errors found in the application.  

## Workflow Overview

The `.github/workflows/python-app.yml` file defines the GitHub Actions workflow for this project. The workflow includes the following key features:

- **Trigger Conditions**: The workflow is triggered on `workflow_dispatch` events, allowing manual triggers, and on pull requests to the `master` branch.
- **Python Version**: The workflow uses Python 3.10 for running tests and linting.
- **Dependency Installation**: Dependencies are installed using `pip`, including `pytest` for running tests. Use the following command to install:
- **Test Run**: The code is ran with pytest.
- **Consume Test Report**: Github action then consumes the test report and displays it in the build list summary page.
## Contributing

Contributions to improve the workflow or the Python application are welcome. Please feel free to submit a pull request or open an issue to discuss your proposed changes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Building and Testing Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python)
