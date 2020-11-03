"""
添加联系人界面
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

# from app.page.MemberInviteMenuPage import MemberInviteMenuPage
from app.page.base_page import BasePage


class ContactAddPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add_contact(self, name, gender, phonenum):
        self.find(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.find(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']").click()

        if gender == '男':
            WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='女']"))
            self.find(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.find(MobileBy.XPATH, "//*[@text='女']").click()

        self.find(MobileBy.XPATH,
                  "//*[contains(@text,'手机') and contains(@class,'android.widget.EditText')]").send_keys(
            phonenum)
        self.find(MobileBy.XPATH, "//*[@text='保存']").click()
        from app.page.MemberInviteMenuPage import MemberInviteMenuPage
        return MemberInviteMenuPage(self.driver)
