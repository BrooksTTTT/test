"""
存放app相关的操作
比如启动 重启 停止 进入到首页
"""
from appium import webdriver

from app.page.MainPage import MainPage
from app.page.base_page import BasePage


class App(BasePage):
    def start(self):
        if self.driver == None:
            # 启动app
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "hogwarts"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["skipServerInstallation"] = 'true'
            caps["skipDeviceInitialization"] = 'true'
            caps["noReset"] = "True"
            # caps["settings[waitForIdleTimeout]"] = 0
            # 关键  localhost:4723  本机ip:server端口
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
            # self.driver.start_activity(package,activity)
        return self

    def restart(self):
        # 重启app
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def stop(self):
        # 停止app
        self.driver.quit()

    def goto_man(self) -> MainPage:
        #  进入到首页
        return MainPage(self.driver)
