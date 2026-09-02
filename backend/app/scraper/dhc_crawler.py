import logging
import time 

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from app.config import Config

class DelhiHighCourtScraper:
    BASE_URL = Config.BASE_URL
    SEARCH_PATH = Config.SEARCH_PATH

    def __init__(self,driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

        self.last_request_time=0

    def respect_rate_limit(self):
        elapsed = time.time() - self.last_request_time

        if elapsed < Config.RATE_LIMIT_SECONDS:
            sleep_time = Config.RATE_LIMIT_SECONDS - elapsed

            self.logger.info(
                f"Rate limiting: sleeping {sleep_time:.2f} seconds"
            )

            time.sleep(sleep_time)
        
        self.last_request_time = time.time()

    def open_search_page(self):

        self.respect_rate_limit()

        full_url =f"{self.BASE_URL}{self.SEARCH_PATH}"

        self.logger.info(
            f"Opening search page:{full_url}"
        )

        self.driver.get(full_url)

        try:

            WebDriverWait(
                self.driver,
                Config.FORM_WAIT_TIMEOUT
            ).until(
                EC.presence_of_element_located(
                    (By.ID, "case_type")
                )
            )

            self.logger.info(
                "Delhi High Court search form loaded - SUCCESS"
            )

            return True

        except TimeoutException:
            self.logger.warning(
                f"Delhi High Court search form loaded - FAILED [within time limit]"
            )

            return False    
        
    def get_current_url(self):
        return self.driver.current_url

    def get_page_title(self):
        return self.driver.title

    def get_page_source(self):
        return self.driver.page_source    