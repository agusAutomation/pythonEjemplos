from pytest_bdd import scenarios, given, when, then, parsers
from Pages.HeaderPage import HeaderPage
from Pages.ProductPage import ProductPage


# Scenarios
scenarios('../features/SearchProduct.feature')


# When Steps
@when(parsers.parse('complete "{product}"'))
def complete_product(browser, product):
    header_page = HeaderPage(browser)
    header_page.getSearchInput().send_keys(product)
    print('Complete product in search input')


@when('press the search button')
def click_button(browser):
    header_page = HeaderPage(browser)
    header_page.getLupa().click()
    print('Click lupa button')

# Then Steps
@then(parsers.parse('can check the product "{title}"'))
def check_product_title(browser, title):
    product_page = ProductPage(browser)

    assert product_page.getProductTitle().text == title
    print('Check product title')

