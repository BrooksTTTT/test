import yaml
from appium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from frame.hand_black import hand_black


class BasePage:
    black_list = [(By.XPATH, "//*[@resource-id = 'com.xueqiu.android:id/iv_close']")]
    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        """
        初始化
        """
        if driver is None:
            caps = {}
            caps["platformName"] = "android"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    @hand_black
    def find(self, by, locator=None):
        """
        查找元素
        :return:
        """

        if locator is None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, locator)
        return result

    def parse(self, steps):

        for step in steps:
            if 'click' == step['action']:
                self.find(step['by'], step['locator']).click()

    def parse_yaml(self, path, func_name):

        with open(path, encoding="utf-8") as f:
            data = yaml.load(f)
        self.parse(data[func_name])
