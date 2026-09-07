import logging

from selenium.webdriver.common.by import By

class CaptchaFinder:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def find_captcha_input(self):
        try:
            captcha_input=self.driver.find_element(
                By.ID,
                "captchaInput"
            )

            self.logger.info(
                "CAPTCHA input field found - SUCCESS"
            )

            return captcha_input
        
        except Exception as e:
            self.logger.info(
                f"CAPTCHA input field not found: {e}"
            )

            return None