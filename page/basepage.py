# 通用方法的封装
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage():

    _driver :WebDriver
    _black_list = [
        (MobileBy.XPATH, "//*[contains(@resource-id, 'tv_agree')]"),
        (MobileBy.XPATH, "//*[contains(@text='下次再说')]"),
        (MobileBy.XPATH, "//*[contains(@text='暂不设置')]"),
        (MobileBy.ID, 'image_cancel'),
    ]

    def __init__(self, driver:WebDriver=None):
        self._driver = driver

    # 处理异常弹窗
    def find(self, locator, value=None):
        try:
            # 寻找控件
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)
            return element
        except Exception as e:
            for black_ele in self._black_list:
                elements = self._driver.find_elements(*black_ele)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(locator, value)
            # 如果黑名单没有就报错
            raise e

    def get_toast(self):
        return self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text

    def get_text(self, key):
        return self.find(MobileBy.XPATH, "//*[@text='{key}']".format(key=key))



