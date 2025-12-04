# Automation Test using Selenium for Swag Labs mock website

## Prerequisite
1. Python 3.X
2. Pytest 3.8.x
3. Selenium

## Descriptions
This automation test is build using Selenium and Pytest using POM framework. There are two directories, namely *sauce_pages* and *sauce_test*. 
- Inside *sauce_pages* there are currently three files, namely __login_page.py__, __main_page.py__, and __cart_page.py__. 
- Inside *sauce_test* lies testing files named __test_login.py__ and __test_mainpage.py__. **__init.py__** is created to guide pytest to include *sauce_pages* folder.
- Several markers have been configured,
  a. login: test for login flow,
  b. buy_products: test for buying products flow,
  c. cart: test for checking cart page (TBA), and
  d. confirm_buy: test for buying specific products (TBA).

## License
Since it is a personal project, I listed this with no license.

## Thanks for reading!
