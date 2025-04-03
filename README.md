### Summary of Keyword-Driven Framework Development

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
   - Developed page object class for account registration.
   - Created a test case to register an account.
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

    **Continuous Integration**

15. **Automated Login Test Case**
    - Developed page object class for the login "CustomerLogin".
    - Created a test case "Test_002_Login" to check that a user can log in.

16. **Automated Logout Test Case**
    - Developed page object class for the logout "MyAccount".
    - Created a test case "Test_003_Logout" to check that a user can log out.

17. **Automated Login DDT Test Case**
    - Developed test class for Data-Driven Testing (DDT) login.
    - Created a test case "Test_004_Login_DDT" to perform login using data from an Excel sheet.
    - Iterated through multiple test cases in Excel, reading email, password, and expected result.
    - Determined pass/fail status based on the expected result and logged the results.
    - Asserted the final result based on the overall status of test cases.

18. **Automated Adding To The Cart**
    - Developed the following page object files "EchoFit", "ShoppingCart" and "YogaCollection"
    - Created test case "Test_005_AddToCart" to check that a user can add items to a cart.

19. **Automated Adding To Compare**
    - Developed the following page object files "CompareProducts"
    - Created test case "Test_006_AddToCompare" to check that a user can add items to list and compare. 

20. **Automated Adding To Wish List**
    - Developed the following page object files "WishList"
    - Created test case "Test_007_AddToWishList" to check that a user can add items to a Wish List. 

21. **Automated Checking Out Items**
    - Developed the page object files "Order Summary" and "Order Confirmation"
    - Created test case "Test_008_OrderItem" to check that a user can purchase an item

22. **Automated Resetting Password**
    - Developed the page object files "Forgot Your Password"
    - Created test case "Test_009_ResetPassword" to check that a user can reset their password

##. **Current Project**
    - Clearing items from "Wish List", "Cart" and "Compare"
    - Opening up a gmail account to check for reset links
       
**Future Projects**
    - Validate login functionality - COMPLETE
    - Validate logout functionality - COMPLETE
    - Validate the add to cart functionality - COMPLETE
    - Validate compare functionality - COMPLETE
    - Validate the wish list functionality - COMPLETE
    - Verify checkout functionality - COMPLETE
    - Validate reset password functionality - CURRENT
    - Validate search functionality 
    - Validate Home Page functionality
    - Validate 'What's New' functionality
    - Validate 'Women' functionality
    - Validate 'Men' functionality
    - Validate 'Gear' functionality
    - Validate 'Training' functionality
    - Validate 'Sale' functionality
    - Validate 'My Account' functionality
    - Expand on the login page by creating a data-driven test
