
from appium.webdriver.common.mobileby import MobileBy

from page.basepage import BasePage


class Main(BasePage):

    _search = (MobileBy.ID, "home_search")
    _search_input = (MobileBy.ID, "search_input_text")
    _content_list = (MobileBy.XPATH, "//*[contains(@resource-id, 'listview')]//[contains(@class, 'RelativeLayout')][1]")

    def search(self):
        self.find(self._search).click()
        self.find(self._search).send_keys("alibaba")
        self.find(self._content_list).click()



