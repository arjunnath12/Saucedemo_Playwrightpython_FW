
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.infoPage import InfoPage
from pages.cartPage import CartPage
from pages.overviewPage import OverviewPage
from utilities.ExcelData import getCellData


def test_firstScript(page):
    login_Page = LoginPage(page)
    home_Page = HomePage(page)
    cart_Page = CartPage(page)
    info_Page = InfoPage(page)
    overview_page = OverviewPage(page)

    username=getCellData("testData/userInfo.xlsx","Sheet1",2,1)
    password = getCellData("testData/userInfo.xlsx", "Sheet1", 2, 2)

    login_Page.login_to_application(username ,password)
    home_Page.add_first_product_to_cart()
    cart_Page.proceed_to_checkout()
    info_Page.enter_checkout_information()
    overview_page.placeOrder()