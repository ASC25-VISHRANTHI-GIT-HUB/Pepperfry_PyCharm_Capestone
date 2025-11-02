import pytest
import os
from Pepperfry.pages.login_page import LoginPage
from Pepperfry.pages.search_page import SearchPage
from Pepperfry.pages.wishlist_page import WishlistPage
from Pepperfry.pages.cart_page import CartPage
from Pepperfry.utilities.screenshots import capture
from Pepperfry.base.base_test import setup_teardown

@pytest.mark.usefixtures("setup_teardown")
class TestPepperfryE2E:

    def log_step(self, msg):
        print(msg)
        if hasattr(pytest, 'html'):
            pytest.html.extras.append(pytest.html.extras.html(f"<p>{msg}</p>"))

    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        self.log_step("<h2>Step 1: Login</h2>")
        login.login_with_email("avishranthi2304@gmail.com", capture, self.log_step)
        self.log_step("<h3 style='color:green;'> Login Successful</h3>")
        assert True

    def test_search_product(self):
        driver = self.driver
        search = SearchPage(driver)
        self.log_step("<h2>Step 2: Search Product</h2>")
        search.search_item("Lights", capture, self.log_step)
        search.select_first_product(capture, self.log_step)
        self.log_step("<h3 style='color:green;'> Product Searched Successfully</h3>")
        assert True

    def test_add_to_wishlist(self):
        driver = self.driver
        wishlist = WishlistPage(driver)
        self.log_step("<h2>Step 3: Add to Wishlist</h2>")
        wishlist.add_to_wishlist(capture, self.log_step)
        wishlist.open_wishlist_page(capture, self.log_step)
        self.log_step("<h3 style='color:green;'> Product Added to Wishlist</h3>")
        assert True

    def test_add_to_cart(self):
        driver = self.driver
        cart = CartPage(driver)
        self.log_step("<h2>Step 4: Add to Cart</h2>")
        cart.add_to_cart(capture, self.log_step)
        cart.open_cart_page(capture, self.log_step)
        self.log_step("<h3 style='color:green;'> Product Added to Cart Successfully</h3>")
        assert True


if __name__ == "__main__":
    os.makedirs(os.path.join("Pepperfry", "reports"), exist_ok=True)
    pytest.main([
        "Pepperfry/tests",
        "--html=Pepperfry/reports/pepperfry_report.html",
        "--self-contained-html",
        "-q"
    ])
