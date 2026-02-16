from playwright.sync_api import Page ,expect
from utilities.ConfigReader import ConfigFileReader

class OverviewPage():
    def __init__(self, page:Page):
        self.page = page
        self.finish_button = page.get_by_role("button",name="Finish")
        self.back_home_button = page.get_by_role("button",name="Back Home")


    def placeOrder(self):
        try:
            self.finish_button.click()
            self.back_home_button.click()
            config_reader = ConfigFileReader()
            # overview_URL = config_reader.readConfig("basic_info", "overviewURL")
            # # self.page.wait_for_url(overview_URL)
            # expect(self.page).to_have_url(overview_URL)
            dashboard_URL = config_reader.readConfig("basic_info", "dashboardURL")
            self.page.wait_for_url(dashboard_URL)
            expect(self.page).to_have_url(dashboard_URL)
        except:
            print("Error occurred while placing the order")