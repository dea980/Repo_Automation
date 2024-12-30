from datetime import datetime
import logging
import os
from typing import Dict, List
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('form_automation.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class GoogleFormAutomation:
    def __init__(self):
        """Initialize the Google Form automation class."""
        self.form_url = "https://docs.google.com/forms/d/1gN1V6N_vohFx8kszFmqDU8570pgAU_ViST7yCVohgF4/viewform"
        self.driver = None

    def setup_driver(self):
        """Set up the Chrome WebDriver."""
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # Uncomment to run in headless mode
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)

    def close_driver(self):
        """Close the WebDriver."""
        if self.driver:
            self.driver.quit()

    def submit_form(self, common_data: Dict[str, str], blog_link: str) -> bool:
        """
        Submit a single form entry.
        
        Args:
            common_data: Dictionary containing:
                - name: 이름
                - til_date: TIL 작성 일자
                - weather: 오늘의 날씨
            blog_link: The blog link to submit
        
        Returns:
            bool: True if submission was successful, False otherwise
        """
        try:
            # Initialize driver if not already initialized
            if not self.driver:
                self.setup_driver()

            # Navigate to form
            self.driver.get(self.form_url)
            wait = WebDriverWait(self.driver, 10)

            # Fill name (이름)
            name_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
            name_field.send_keys(common_data['name'])

            # Fill blog link (블로그링크)
            blog_fields = self.driver.find_elements(By.XPATH, "//input[@type='text']")
            blog_fields[1].send_keys(blog_link)

            # Fill TIL date (TIL 작성 일자)
            date_input = self.driver.find_element(By.XPATH, "//input[@type='date']")
            date_input.send_keys(common_data['til_date'])

            # Select weather (오늘의 날씨)
            weather_mapping = {
                '맑음': "//div[contains(., '맑음 (기분 좋아요)')]",
                '흐림': "//div[contains(., '흐림 (그냥 그래요)')]",
                '비': "//div[contains(., '비 (힘들어요)')]",
                '천둥': "//div[contains(., '천둥/번개 (궂일이에요)')]"
            }
            
            weather_option = wait.until(EC.element_to_be_clickable(
                (By.XPATH, weather_mapping.get(common_data['weather'], weather_mapping['맑음']))
            ))
            weather_option.click()

            # Submit form
            submit_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@role='button']//span[contains(text(), '제출')]")
            ))
            submit_button.click()

            # Wait for confirmation message
            wait.until(EC.presence_of_element_located(
                (By.XPATH, "//div[contains(text(), '응답이 기록되었습니다')]")
            ))

            logger.info(f"Form submitted successfully for blog link: {blog_link}")
            return True

        except TimeoutException as e:
            logger.error(f"Timeout while submitting form: {e}")
            return False
        except Exception as e:
            logger.error(f"Error submitting form: {e}")
            return False

    def submit_multiple_links(self, common_data: Dict[str, str], blog_links: List[str]) -> bool:
        """
        Submit multiple blog links with the same common data.
        
        Args:
            common_data: Dictionary containing common form data (name, date, weather)
            blog_links: List of blog links to submit
        
        Returns:
            bool: True if all submissions were successful, False otherwise
        """
        try:
            self.setup_driver()
            success = True

            for link in blog_links:
                if not self.submit_form(common_data, link):
                    success = False
                    logger.error(f"Failed to submit entry for link: {link}")

            return success

        finally:
            self.close_driver()

def main():
    """Example usage of the GoogleFormAutomation class."""
    # Initialize the automation class
    form_automation = GoogleFormAutomation()

    # Common data that will be used for all submissions
    common_data = {
        'name': '홍길동',
        'til_date': '2024-12-30',
        'weather': '맑음'
    }

    # List of blog links to submit
    blog_links = [
        'https://blog.example.com/post1',
        'https://blog.example.com/post2',
        'https://blog.example.com/post3'
    ]

    # Submit multiple blog links with the same common data
    success = form_automation.submit_multiple_links(common_data, blog_links)
    if success:
        logger.info("All blog links submitted successfully")
    else:
        logger.error("Some blog links failed to submit")

if __name__ == '__main__':
    main()