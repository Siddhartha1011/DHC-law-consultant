import logging

from typing import Dict, List, Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class CaseOptions:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def get_case_types_and_years(
        self
    ) -> Tuple[Dict[str, str], List[str]]:

        case_types = {}
        years = []

        # -----------------------------------------
        # CASE TYPES
        # -----------------------------------------

        try:

            case_type_elem = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.presence_of_element_located(
                    (By.NAME, "case_type")
                )
            )

            select = Select(case_type_elem)

            for opt in select.options:

                value = opt.get_attribute("value")
                text = opt.text.strip()

                if value and value.strip() and text:
                    case_types[value.strip()] = text

            self.logger.info(
                f"Found {len(case_types)} case types"
            )

        except TimeoutException:

            self.logger.warning(
                "Case type select not found or timed out"
            )

        except Exception as e:

            self.logger.error(
                f"Error extracting case types: {e}"
            )

        # -----------------------------------------
        # YEARS
        # -----------------------------------------

        try:

            year_elem = WebDriverWait(
                self.driver,
                10
            ).until(
                EC.presence_of_element_located(
                    (By.ID, "case_year")
                )
            )

            select = Select(year_elem)

            for opt in select.options:

                value = opt.get_attribute("value")

                if value and value.strip().isdigit():

                    years.append(
                        value.strip()
                    )

            # Remove duplicates
            years = list(dict.fromkeys(years))

            self.logger.info(
                f"Found {len(years)} years"
            )

        except TimeoutException:

            self.logger.warning(
                "Year select not found or timed out"
            )

        except Exception as e:

            self.logger.error(
                f"Error extracting years: {e}"
            )

        return case_types, years



