from appium.webdriver.common.mobileby import MobileBy

from app.page.ConfirmPage import ConfirmPage
from app.page.base_page import BasePage


class EditMemberPage(BasePage):
    def click_delete_button(self):
        self.find_by_scroll("删除成员").click()
        return ConfirmPage(self.driver)
