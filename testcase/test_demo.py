from page.app import App
from utils.utils import *



class TestDemo:

    def setup(self):
        self.main = App().start().main()

    def teardown(self):
        pass

    @recordvideo
    def test_demo(self):
        self.main.search()
