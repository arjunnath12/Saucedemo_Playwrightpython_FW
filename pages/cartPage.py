from playwright.sync_api import Page ,expect
from utilities.ConfigReader import ConfigFileReader


class CartPage():
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.get_by_role("button", name="Checkout")


    def proceed_to_checkout(self):
        try:
            self.checkout_button.click()
            config_reader = ConfigFileReader()
            info_URL = config_reader.readConfig("basic_info", "yourInfoURL")
            expect(self.page).to_have_url(info_URL)
        except:
            print("Error occurred while proceeding to checkout")