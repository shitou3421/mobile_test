# 通用方法的封装
import logging

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utils.utils import attach

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class BasePage():
    _driver: WebDriver
    _black_list = [
        (MobileBy.XPATH, "//*[contains(@resource-id, 'tv_agree')]"),
        (MobileBy.XPATH, "//*[contains(@text, '下次再说')]"),
        # (MobileBy.XPATH, "//*[contains(@text, '暂不设置')]"),
        # (MobileBy.XPATH, "//*[contains(@text, '跳过广告')]"),
        # (MobileBy.XPATH, "//*[contains(@resource-id, 'image_cancel']"),
    ]

    _error_max = len(_black_list)
    _error_count = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def __wait(self, locator:tuple):
        # WebDriverWait(self._driver, 10).until(expected_conditions.visibility_of_all_elements_located(locator))
        attach(self._driver, name=locator)  # 做到每一步都截图记录到allure报告上


    # 处理异常弹窗
    def find(self, locator, value=None):
        logger.info("本次查找控件元素：locator：{locator}, value：{value}".format(locator=locator, value=value))
        try:
            # 寻找控件
            if isinstance(locator, tuple):
                self.__wait(locator)
                element = self._driver.find_element(*locator)
            else:
                self.__wait((locator, value))
                element = self._driver.find_element(locator, value)
            self._error_count = 0
            return element

        except Exception as e:
            if self._error_count > self._error_max:
                raise e
            self._error_count += 1
            for black_ele in self._black_list:
                logger.info("本次查找黑名单中：{black_ele}".format(black_ele=black_ele))
                elements = self._driver.find_elements(*black_ele)
                if len(elements) > 0:
                    self.__wait((locator, value))
                    elements[0].click()
                    return self.find(locator, value)
            # 如果黑名单没有就报错
            logger.info("黑名单没有找到元素")
            pagesource = self._driver.page_source
            logger.info("本轮黑名单没找到目标元素， 当前pagesource为：\n{pagesource}".format(pagesource=pagesource))
            raise e

    def get_toast(self):
        return self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text

    def get_text(self, key):
        return self.find(MobileBy.XPATH, "//*[@text='{key}']".format(key=key))

    def steps(self):
        '''
        用例步骤的数据驱动，
        :return:
        '''
        pass

    def long_press(self, ele: WebElement, time):
        '''
        长按
        :return:
        '''
        TouchAction(self._driver).long_press(el=ele, duration=time).perform()

    def _scroll_down_to_up(self, x, y):
        '''
        从下往上滑动
        :return:
        '''
        TouchAction(self._driver).long_press(x=x*0.5, y=y*0.8).move_to(x=x*0.8, y=y*0.2).release().perform()

    def _scroll_up_to_down(self, x, y):
        '''
        从上往下滑动
        :return:
        '''
        TouchAction(self._driver).long_press(x=x*0.5, y=y*0.8).move_to(x=x*0.8, y=y*0.2).release().perform()


    def _scroll_right_to_left(self, x, y):
        '''
        从右往左滑动
        :return:
        '''
        TouchAction(self._driver).long_press(x=x*0.2, y=y*0.5).move_to(x=x*0.8, y=y*0.5).release().perform()

    def _scroll_left_to_right(self, x, y):
        '''
        从左往右滑动
        :return:
        '''
        TouchAction(self._driver).long_press(x=x*0.8, y=y*0.5).move_to(x=x*0.2, y=y*0.5).release().perform()

    def scroll(self, postion:str):
        '''
        滑动方法
        :param postion:
        :return:
        '''
        size = self._driver.get_window_size()
        x = size.get("width")
        y = size.get("height")
        postion = postion.lower()
        if postion == "up":
            self._scroll_down_to_up(x, y)
        elif postion == "down":
            self._scroll_up_to_down(x, y)
        elif postion == "left":
            self._scroll_right_to_left(x, y)
        elif postion == "right":
            self._scroll_left_to_right(x, y)
        else:
            raise Exception("不支持的滚动类型")

