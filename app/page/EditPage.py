from appium.webdriver.common.mobileby import MobileBy

from app.page.base_page import BasePage


class EditPage(BasePage):
    def choose_name(self, name):
        self.find(MobileBy.XPATH, f"//*[@text='{name}']").click()
        from app.page.EditMemberPage import EditMemberPage
        return EditMemberPage(self.driver)

    def cannot_find_name(self, name):
        return True
