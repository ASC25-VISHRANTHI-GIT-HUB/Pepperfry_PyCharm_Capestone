import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def login_with_email(self, email, capture, log_step):
        try:
            email_input = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='take-mobile-email-container']/form/div/div/div/div[2]/input"))
            )
            email_input.clear()
            email_input.send_keys(email)
            log_step("Entered email address.")
            capture(self.driver, "entered_email")

            cont_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH,
                    "/html/body/pf-modal[1]/div/div[1]/div/pf-authentication/div/section/pf-signup-login/section[2]/div[1]/section/form/pf-button/button/div"))
            )
            self.driver.execute_script("arguments[0].click()", cont_btn)
            log_step("Clicked Continue.")
            capture(self.driver, "clicked_continue")
        except Exception as e:
            capture(self.driver, "email_failed")
            pytest.fail(f"Login failed at email entry: {e}")

        log_step("Waiting 30 seconds for manual OTP entry.")
        time.sleep(30)
