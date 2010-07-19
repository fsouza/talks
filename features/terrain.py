from lettuce import *

import os
import sys
app_path = os.path.dirname(os.path.abspath(__file__)).replace('/features', '')

from selenium import get_driver, FIREFOX
from lxml import html

class SeleniumBrowser(object):
    def __init__(self, host = 'localhost', port = 4444, browser = '*firefox', base_url='http://localhost:8080'):
        self.host = host
        self.port = port
        self.browser = browser
        self.driver = get_driver(FIREFOX)
        self.base_url = base_url

    def go_to_url(self, url):
        url = self.get_url(url)
        self.driver.get(url)

    def get_source(self):
        return self.driver.get_page_source()

    def get_dom(self):
        return html.fromstring(self.get_source())

    def find_element_by_xpath(self, selector):
        return self.driver.find_element_by_xpath(selector)

    def get_current_url(self):
        return self.driver.get_current_url()

    def quit(self):
        self.driver.quit()

    def get_url(self, url):
        if url.find(self.base_url) < 0:
            if url[0] == '/':
                fmt = '%s%s'
            else:
                fmt = '%s/%s'
            return fmt %(self.base_url, url)
        else:
            return url


@before.all
def setup_env():
    sys.path.append(app_path)
    from talks_application import app
    world.browser = SeleniumBrowser()

@after.all
def teardown_env(total):
    sys.path.remove(app_path)
    world.browser.quit()
