import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WishlistPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def add_to_wishlist(self, capture, log_step):
        try:
            wishlist_btn = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id='vip-img-gallery-container']/div/div/div[2]/div[5]/div")
            ))
            self.driver.execute_script("arguments[0].click();", wishlist_btn)
            log_step("Added item to Wishlist.")
            capture(self.driver, "wishlist_added")
            time.sleep(3)
        except Exception as e:
            capture(self.driver, "wishlist_failed")
            pytest.fail(f"Failed to add to Wishlist: {e}")



    def open_wishlist_page(self, capture, log_step):
        try:
            wishlist_icon = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/app-root/pf-header/header/div[2]/pf-header-main/div/div[1]/div/div[4]/pf-header-icons/div/div[3]/a/img")
            ))
            self.driver.execute_script("arguments[0].click();", wishlist_icon)
            log_step("Opened Wishlist page.")
            capture(self.driver, "wishlist_page")
        except Exception as e:
            capture(self.driver, "wishlist_page_failed")
            pytest.fail(f"Failed to open Wishlist page: {e}")
