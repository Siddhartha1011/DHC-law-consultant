import logging

from selenium.webdriver.common.by import By

class CaptchaCode:

    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def find_captcha_text(self):

        try:
            captcha_elements=(

                self.driver.find_elements(
                    By.ID,"captcha-code"
                )

                or self.driver.find_elements(
                        By.CLASS_NAME,
                        "captcha-code"
                    )
            )

            if not captcha_elements:

                self.logger.warning(
                    "CAPTCHA code element not found"
                )

            captcha_element=captcha_elements[0]

            captcha_text=captcha_element.text.strip()

            if captcha_text:
                self.logger.info(
                    "CAPTCHA text found successfully."
                )

                return captcha_text
            
        except Exception as e:
            self.logger.error(
                f"Error finding CAPTCHA text: {e}"
            )

            return None