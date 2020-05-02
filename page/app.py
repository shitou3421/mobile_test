# app的共性业务封装
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
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
            caps["platformVersion"] = "10"
            # caps["udid"] = "127.0.0.1:7555"
            # caps["app"] = ""

            caps["appPackage"] = self._appPackage
            caps["appActivity"] = self._appActivity

            caps["noreset"] = True
            caps["dontstopAppOnReset"] = True
            caps["skipServerInstallation"] = True
            # caps["skipDeviceInitialization"] = True # 动态加入

            caps["unicodeKeyboard"] = True
            caps["resetKeyboard"] = True

            caps["newCommandTimeout"] = 300
            caps["adbExecTimeout"] = 50000
            caps["uiautomator2ServerLaunchTimeout"] = 50000

            caps["chromedriverExecutable"] = ""
            caps["chromedriverExecutableDir"] = ""
            caps["chromedriverChromeMappingFile"] = ""

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
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
        return Main(self.driver)


