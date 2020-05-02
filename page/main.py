
from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage


class Main(BasePage):

    _search = (MobileBy.ID, "home_search")
    _search_input = (MobileBy.XPATH, "//*[contains(@resource-id, 'search_input_text')]")
    # _content_list = (MobileBy.XPATH, "//*[contains(@resource-id, 'listview')]//[contains(@class, 'RelativeLayout')][1]")

    def search(self):
        self.find(self._search).click()
        self.find(self._search_input).send_keys("jd")
        # self.find(self._content_list).click()

        # self._driver.start_recording_screen()
        # self._driver.stop_recording_screen()

        # self._driver.get_performance_data()
        # self._driver.get_performance_data_types()
