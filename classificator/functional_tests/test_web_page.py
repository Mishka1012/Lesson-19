from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time



class TestHomePage(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome('functional_tests/chromedriver')

    def tearDown(self) -> None:
        self.browser.close()

    def test_case(self):
        self.browser.get(self.live_server_url)
        time.sleep(20)