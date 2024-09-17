from pages.checkoutpage import CheckoutPage
from pages.mainpage import MainPage
from pages.registpage import RegistPage
from pages.cartpage import CartPage
from pages.finishpage import FinishPage


def test_site(driver):
    errors = []

    registration = RegistPage(driver)

    registration.open()

    registration.auth()

    main_page = MainPage(driver)

    main_page.add_to_cart()

    cart_page = CartPage(driver)

    cart_page.confirm_cart(errors)

    checkout_page = CheckoutPage(driver)

    checkout_page.complete(errors)

    finish = FinishPage(driver)

    finish.check(errors)
