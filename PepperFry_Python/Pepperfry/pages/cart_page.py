import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def add_to_cart(self, capture, log_step):
        try:
            self.driver.get("https://www.pepperfry.com/product/modern-contemporary-spiral-led-3-ring-chandelier-adjustable-height-with-3-color-2255357.html")
            add_btn = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/app-root/main/app-vip/div/div[2]/div[2]/div[2]/section/div[4]/pf-vip-cta/div/div/div[1]/pf-button/button")
            ))
            self.driver.execute_script("arguments[0].click();", add_btn)
            log_step("Added item to Cart.")
            capture(self.driver, "cart_added")
        except Exception as e:
            capture(self.driver, "cart_failed")
            pytest.fail(f"Failed to add to Cart: {e}")

    def open_cart_page(self, capture, log_step):
        try:
            cart_icon = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/app-root/pf-header/header/div[2]/pf-header-main/div/div[1]/div/div[4]/pf-header-icons/div/div[4]/a/img")
            ))
            self.driver.execute_script("arguments[0].click();", cart_icon)
            log_step("Opened Cart page.")
            capture(self.driver, "cart_page")
        except Exception as e:
            capture(self.driver, "cart_page_failed")
            pytest.fail(f"Failed to open Cart page: {e}")
