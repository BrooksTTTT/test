from frame.main import Main


class TestMain:
    def test_main(self):
        main = Main().goto_market().goto_search()
