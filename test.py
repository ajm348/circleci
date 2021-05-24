import re
import threading
import time
import unittest
import xmlrunner
import os
from selenium import webdriver


class SeleniumTestCase(unittest.TestCase):
    client = None
    
    @classmethod
    def setUpClass(cls):
        # start Chrome
        try:
            cls.client = webdriver.Chrome(service_args=["--verbose", "--log-path=test-reports/chrome.log"])
        except:
            pass

        # skip these tests if the browser could not be started
        if cls.client:

            # suppress logging to keep unittest output clean
            import logging
            logger = logging.getLogger('werkzeug')
            logger.setLevel("ERROR")

            # start the http server in a thread
            # from https://riptutorial.com/python/example/8570/start-simple-httpserver-in-a-thread-and-open-the-browser

            def start_server(path, port=8000):
                '''Start a simple webserver serving path on port'''
                os.chdir(path)
                httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
                httpd.serve_forever()

            # Start the server in a new thread
            port = 8000
            daemon = threading.Thread(name='daemon_server',
                                      target=start_server,
                                      args=('.', port))
            daemon.setDaemon(True) # Set as a daemon so it will be killed once the main thread is dead.
            daemon.start()

            # give the server a second to ensure it is up
            time.sleep(1) 

    @classmethod
    def tearDownClass(cls):
        if cls.client:
            # stop the the browser
            cls.client.close()

    def setUp(self):
        if not self.client:
            self.skipTest('Web browser not available')

    def tearDown(self):
        pass
    
    def test_text_change(self):
        # navigate to home page
        self.client.get('http://localhost:8000/')

        # check for original text
        self.assertTrue(re.search('Hello,\s+world',
                                  self.client.page_source))

        # click button
        self.client.find_element_by_xpath('//button[text()="Click me!"]').click()

        # check for new text
        self.assertTrue(re.search('Goodbye,\s+world',
                                  self.client.page_source))

if __name__ == "__main__":
    """Run the unit tests."""
    tests = unittest.TestLoader().discover('.')
    xmlrunner.XMLTestRunner(output=os.environ.get('CIRCLE_TEST_REPORTS', 'test-reports')).run(tests)
