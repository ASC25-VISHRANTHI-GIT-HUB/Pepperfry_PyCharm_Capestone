import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="class")
def setup_teardown(request):
    """Setup and teardown for Pepperfry automation tests."""
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # suppress ChromeDriver logs
    chrome_options.add_experimental_option('useAutomationExtension', False)

    # Optional: Run headless if you want silent runs (uncomment below)
    # chrome_options.add_argument("--headless=new")

    # Initialize driver
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(10)
    driver.get("https://www.pepperfry.com/")

    request.cls.driver = driver
    yield
    driver.quit()
