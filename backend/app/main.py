import logging

from app.scraper.browser import Browser
from app.scraper.dhc_crawler import DelhiHighCourtScraper

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def main():
    
    browser = Browser(headless=False)
    
    try:

        scraper = DelhiHighCourtScraper(
            browser.driver
        )

        success = scraper.open_search_page()

        if success:

            print("\n========================")
            print("Delhi High Court Search Page")
            print("========================")

            print(
                "URL:",
                scraper.get_current_url()
            )

            print(
                "TITLE:",
                scraper.get_page_title()
            )

            print(
                "PAGE LOADED:",
                success
            )

        else:

            print("Failed to load search page.")

    finally:

        browser.close()

if __name__=="__main__":
    main()