import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def search_item(self, item, capture, log_step):
        try:
            search_box = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='search']")))
            search_box.clear()
            search_box.send_keys(item)
            search_box.send_keys(Keys.ENTER)
            log_step(f"Searched for '{item}'.")
            capture(self.driver, f"search_{item}")
        except Exception as e:
            capture(self.driver, "search_failed")
            pytest.fail(f"Search failed: {e}")

    def select_first_product(self, capture, log_step):
        try:
            first_item = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='scroller']/div/div[2]/div/pf-clip-product-card/div/div[1]/div[1]/a/pf-image/div/img")
            ))
            self.driver.execute_script("arguments[0].click();", first_item)
            log_step("Clicked first product.")
            capture(self.driver, "first_product")
        except Exception as e:
            capture(self.driver, "click_product_failed")
            pytest.fail(f"Failed to click first product: {e}")

        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[-1])
