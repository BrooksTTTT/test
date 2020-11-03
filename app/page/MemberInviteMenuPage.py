"""
邀请界面
"""
from appium.webdriver.common.mobileby import MobileBy

# from app.page.ContactAddPage import ContactAddPage
from app.page.base_page import BasePage


class MemberInviteMenuPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_member_menual(self):
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        from app.page.ContactAddPage import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result
