**pytest** used for run the program
- **pip install pytest** for installing the pytest
- file name should be **test_name.py**
- test name **test_name_of_test():**
- Assert means assertion 
- **Assert expected result= actual result**
## Pytest command
- **pytest -h** used for help
- **pytest -k "18"** means i want the file to run who  contain 18 number
- **pytest -m "smoke" path of the file** to run specific file who has smoke in it
- to find path right click-- copy path/reference --- path from content root 
- why we mark, because if there 100 test case 20 mark as smoke, 25 sanity test case, 55 regression
- to divide test case into smoke- create, regression-put, patch, , snaity test
-  pip install allure-pytest
## how to install allure 

pytest Automation_testing_july/test_lab180.py --alluredir=allure_result
allure serve allure_result



