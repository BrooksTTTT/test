from appium.webdriver.common.mobileby import MobileBy

from app.page.EditPage import EditPage
from app.page.base_page import BasePage


class ConfirmPage(BasePage):
    def click_confirm_button(self):
        self.find(MobileBy.XPATH, "//*[@text='确定']").click()
        return EditPage(self.driver)
