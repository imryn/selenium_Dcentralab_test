developed several tests using selenium in pytest 
# Automation for tokensfarm
- find the dropdown by using CSS SELECTOR
- find the dropdown by using XPATH

# Automation for hord
- verify sidebar is expanded
- verify collpsing the sidebar
- verify the FAQ section

## installation guide
 - download the repository
 - install python to your computer
 - after you open the project in pycharm or another tool, run this on your terminal:
``` pip install -r requirements.txt ```
 - create a file .env and enter the value I send you in the email

### running the tests

- run this on your terminal: ```pytest tests```
- if you get any error while running the tests related urllib3, please uninstall it. and than run this: 
``` pip install 'urllib3<2.0' ``` and than try to run the tests once again.
- after you running the tests, use this: ```allure serve report```. it will create the tests report for you
