from time import sleep

from playwright.sync_api import Page ,expect
from utilities.ConfigReader import ConfigFileReader


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.shopping_cart_icon = page.locator(".shopping_cart_container")
        self.menu_button = page.get_by_role("button", name="Open Menu")
        self.logout_link = page.get_by_role("link", name="Logout")
        self.about_link = page.get_by_role("link", name="About")
        self.all_product_title = page.locator(".inventory_item_name")
        self.product_description = page.locator(".inventory_details_desc")

    def add_first_product_to_cart(self):
        try:
            self.add_to_cart_button.first.click()
            self.shopping_cart_icon.click()
            config_reader = ConfigFileReader()
            cart_URL = config_reader.readConfig("basic_info", "cartURL")
            expect(self.page).to_have_url(cart_URL)
        except:
            print("Error occurred while adding product to cart")

    def logout_from_application(self):
        try:
            self.menu_button.click()
            self.logout_link.click()
        except:
            print("Error occurred while logging out from application")

    def verify_about_page(self):
        try:
            self.menu_button.click()
            self.about_link.click()
            config_reader = ConfigFileReader()
            about_URL = config_reader.readConfig("basic_info", "aboutURL")
            expect(self.page).to_have_url(about_URL)
            sleep(5)
            self.page.go_back()
        except:
            print("Error occurred while verifying about page")

    def navigate_to_product_details(self):
        try:
            for product in self.all_product_title.all():
                product.click()
                expect(self.product_description).to_be_visible()
                print(self.product_description.inner_text())
                sleep(2)
                self.page.go_back()
                # self.page.get_by_alt_text("Go back").click()
        except:
            print("Error occurred while navigating to product details")