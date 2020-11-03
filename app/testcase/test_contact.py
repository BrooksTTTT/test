from app.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_man()

    def test_appcontact(self):
        name = "Hogwarts_001"
        gender = "男"
        phonenum = "16325578903"
        result = self.main.goto_address().click_addmember().add_member_menual().add_contact(name, gender,
                                                                                            phonenum).get_toast()
        assert '添加成功' == result

    def test_delcontact(self):
        name = "Hogwarts_001"
        result = self.main.goto_address().click_editicon().choose_name(
            name).click_delete_button().click_confirm_button().cannot_find_name(name)
        assert True == result
