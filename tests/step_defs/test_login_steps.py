from pytest_bdd import scenarios, given, when, then, parsers
from Pages.LoginPage import LoginPage
from Pages.AccountPage import AccountPage
import json
import xlrd

# Scenarios
scenarios('../features/Login.feature')


# When Steps
@when(parsers.parse('complete "{username}" and "{password}"'))
def complete_user_pass(browser, username, password):
    login_page = LoginPage(browser)

    #login_page.login(username, password)
    login_page.getUserInput().send_keys(username)
    login_page.getPassInpu().send_keys(password)
    login_page.getLoginBtn().click()
    print('User and password are completed')


@when('complete user and pass')
def complete_user_pass_json(browser):
    login_page = LoginPage(browser)

    file = open('../../Data/users.json', "r")
    data = file.read()
    obj = json.loads(data)
    list = obj['users']

    login_page.getUserInput().send_keys(list[0].get("user"))
    login_page.getPassInpu().send_keys(list[0].get("pass"))
    login_page.getLoginBtn().click()
    print('User and password are completed')


@when('complete user and pass from excel')
def complete_user_pass_excel(browser):
    login_page = LoginPage(browser)

    path = '../../Data/Users.xlsx'
    inputWorkbook = xlrd.open_workbook(path)
    inputWorksheet = inputWorkbook.sheet_by_index(0)
    ### ERROR: La última versión de xlrd no es muy estable... Es conveniente hacer un pip install xlrd==1.2.0

    user = inputWorksheet.cell_value(2, 1)
    password = inputWorksheet.cell_value(2, 2)

    login_page.getUserInput().send_keys(user)
    login_page.getPassInpu().send_keys(password)
    login_page.getLoginBtn().click()
    print('User and password are completed')

# Then Steps
@then('my account page is displayed')
def check_account(browser):
    account_page = AccountPage(browser)

    assert 'MY ACCOUNT' in account_page.getTitle().text
    print('Account page is displayed')


@then(parsers.parse('the error "{error_message}" is displayed'))
def error_login(browser, error_message):
    login_page = LoginPage(browser)

    assert error_message in login_page.getErrorMessage().text
    print('The error is: '+error_message)
