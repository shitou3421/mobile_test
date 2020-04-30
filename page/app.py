# app的共性业务封装
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from page.basepage import BasePage
from page.main import Main


class App(BasePage):

    _appPackage = "com.xueqiu.android"
    _appActivity = ".view.WelcomeActivityAlias"

    # app 启动
    def start(self):
        if self._driver is None:
            caps = {}
            caps["deviceName"] = "demo"
            caps["platformName"] = "android"
            caps["platformVersion"] = "6.0.1"
            caps["udid"] = "127.0.0.1:7555"
            # caps["app"] = ""

            caps["appPackage"] = self._appPackage
            caps["appActivity"] = self._appActivity

            # caps["noreset"] = True
            # caps["dontstopAppOnReset"] = True
            # caps["skipDeviceInitialization"] = True # 动态加入
            # caps["skipServerInstallation"] = True

            caps["unicodeKeyboard"] = True
            caps["resetKeyboard"] = True

            # caps["chromedriverExecutable"] = ""
            # caps["chromedriverExecutableDir"] = ""
            # caps["chromedriverChromeMappingFile"] = ""

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.start_activity(self._appPackage, self._appActivity)
        return self
    # app 重启
    def restart(self):
        pass

    # app 停止
    def stop(self):
        pass

    # app 的主页面
    def main(self):
        def wait_load():
            source = self.driver.page_source

            if "我的" in source:
                return True
            if "行情" in source:
                return True
            if "同意" in source:
                return True
            if "image_cancel" in source:
                return True

        WebDriverWait(self.driver, 60).until(wait_load)
        return Main(self.driver)


