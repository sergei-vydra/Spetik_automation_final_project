from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#registration_link")
    SHOW_BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-group>a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators(object):
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, ".content p")


class LoginPageLocators(object):
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#login_form input[name="login-username"]')
    LOGIN_PW = (By.CSS_SELECTOR, '#login_form input[name="login-password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#register_form input[name="registration-email"]')
    REGISTER_PW1 = (By.CSS_SELECTOR, '#register_form input[name="registration-password1"]')
    REGISTER_PW2 = (By.CSS_SELECTOR, '#register_form input[name="registration-password2"]')
    REGISTER_BTN = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    ALERT_PRICE_IN_BASKET = (By.CSS_SELECTOR, '#messages .alert .alertinner strong')
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages .alert .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert .alertinner')
