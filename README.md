### Summary of Hybrid-Driven Framework Development

1. **Test Scenarios and Cases**
   - Wrote test scenarios and cases for account registration.

2. **Project Setup**
   - Created a new project in Pycharm.
   - Installed required packages via a requirements.txt file:
     - `pytest`, `selenium`, `webdriver-manager`, `pytest-html`, `pytest-xdist`, `openpyxl`, `allure-pytest`.

3. **Folder Structure Creation**
   - Organized the project into folders:
     - Configurations
     - Logs
     - PageObjects (Python classes)
     - Reports
     - Screenshots
     - Testcases (Python scripts)
     - Testdata
     - Utilities (Python utilities)

4. **WebDriver Setup**
   - Created `conftest.py` under the Testcases folder for driver management.

5. **Automated Account Registration Test Case**
   - Developed page object classes for the homepage and account registration.
   - Created test cases for account registration.
   - Included registration fields and wrote a utility to generate random email strings.

6. **Failure Handling**
   - Added functionality to capture screenshots on test failures.

7. **Common Configuration File**
   - Added `config.ini` under Configurations.
   - Created a "read properties" utility to read common data.
   - Replaced hardcoded values in the account registration test case with values from `config.ini`.

8. **Logging**
   - Created `customlogger.py` under Utilities.
   - Integrated logging into the account registration test case.

9. **Multi-browser Support**
   - Updated `conftest.py` to include Edge and Firefox drivers.

10. **Report Generation**
    - Configured pytest HTML report generation via pytest hooks in `conftest.py`.

11. **Test Grouping**
    - Created `pytest.ini` for test grouping.
    - Added markers to test methods:
      - `@pytest.mark.sanity`
      - `@pytest.mark.regression`

12. **Automation Scripts**
    - Created `requirements.bat` and `install_packages.bat` for package installations.

13. **Version Control**
    - Pushed the code to Git and GitHub repository.

14. **Continuous Integration**
    - Ran the tests on Jenkins.
   
**Future Projects**
    - Build on test scenarios and cases for Login and Data Driven testing
    - Develop the page object class for Login
    - Create a test case to login successfully
    - Expand on the login page by creating a data-driven testing
