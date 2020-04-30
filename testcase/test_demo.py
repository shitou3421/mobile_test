from page.app import App


class TestDemo:

    def setup(self):
        self.main = App().start().main()

    def teardown(self):
        pass

    def test_demo(self):
        self.main.search()


