import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_checkout_with_info_available(driver):
    driver.get("https://demo.opencart.com/")
    # đăng nhập vào tài khoản đã có địa chỉ sẵn trước khi thanh toán
    my_account_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/account')]")

    driver.execute_script("arguments[0].scrollIntoView();", my_account_link)

    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
        )
        close_button.click()
    except Exception:
        pass  # Nếu không có popup, tiếp tục

    my_account_link.click()
    time.sleep(10)
    driver.find_element(By.ID, "input-email").send_keys("testZoe@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(3)
    # thêm sản phẩm vào giỏ hàng bằng cách tìm từ khóa
    search_input = driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys("HTC Touch")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(10)

    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    driver.execute_script("arguments[0].scrollIntoView();", product_items[0])
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "HTC Touch HD").click()
    time.sleep(5)
    quantity = driver.find_element(By.ID, "input-quantity")
    quantity.clear()
    quantity.send_keys("2")
    time.sleep(3)
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(10)
    # sau khi thêm sản phẩm thì chọn vào nút giỏ hàng để xem giỏ hàng thu nhỏ bên góc trên phải
    cart_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    driver.execute_script("arguments[0].scrollIntoView();", cart_button)
    cart_button.click()
    time.sleep(3)
    # chọn vào checkout element
    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-share").click()
    time.sleep(5)
    # chọn địa chỉ đã có sẵn trước đó
    select = Select(driver.find_element(By.CSS_SELECTOR, "#input-shipping-address"))
    select.select_by_value("561")
    # chọn phương thức giao hàng
    driver.find_element(By.ID, "button-shipping-methods").click()
    time.sleep(5)
    driver.find_element(By.ID, "input-shipping-method-flat-flat").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='text-end']/button[@id='button-shipping-method']").click()
    # chọn phương thức thanh toán
    time.sleep(7)
    driver.find_element(By.ID, "button-payment-methods").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-payment-method-cod-cod").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='text-end']/button[@id='button-payment-method']").click()
    # cuộn trang để có thể chọn vào confirm button
    td_element = driver.find_element(By.XPATH, "//td[@class='text-start' and text()='Product Name']")
    driver.execute_script("arguments[0].scrollIntoView();", td_element)
    time.sleep(3)
    driver.find_element(By.ID, "button-confirm").click()
    time.sleep(3)
    # sẽ lấy được thông báo nếu đơn hàng đã được đặt
    account_header = driver.find_element(By.XPATH, "//h1[normalize-space()='Your order has been placed!']")
    assert account_header.is_displayed()

def test_checkout_with_new_info(driver):
    driver.get("https://demo.opencart.com/")
    # đăng nhập vào tài khoản chưa có địa chỉ sẵn
    my_account_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/account')]")

    driver.execute_script("arguments[0].scrollIntoView();", my_account_link)

    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
        )
        close_button.click()
    except Exception:
        pass  # Nếu không có popup, tiếp tục

    my_account_link.click()
    time.sleep(10)
    driver.find_element(By.ID, "input-email").send_keys("admin123567890@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(3)
    # thêm sản phẩm vào giỏ hàng bằng cách tìm từ khóa
    search_input = driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys("HTC Touch")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(10)

    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    driver.execute_script("arguments[0].scrollIntoView();", product_items[0])
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "HTC Touch HD").click()
    time.sleep(5)
    quantity = driver.find_element(By.ID, "input-quantity")
    quantity.clear()
    quantity.send_keys("2")
    time.sleep(3)
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(10)
    # sau khi thêm sản phẩm thì chọn vào nút giỏ hàng để xem giỏ hàng thu nhỏ bên góc trên phải
    cart_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    driver.execute_script("arguments[0].scrollIntoView();", cart_button)
    cart_button.click()
    time.sleep(3)
    # chọn vào checkout element
    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-share").click()
    time.sleep(5)
    # chọn tạo địa chỉ mới
    driver.find_element(By.ID, "input-shipping-new").click()
    time.sleep(3)
    # nhập các thông tin
    driver.find_element(By.ID, "input-shipping-firstname").send_keys("Zoeee")
    driver.find_element(By.ID, "input-shipping-lastname").send_keys("Nguyen")
    driver.find_element(By.ID, "input-shipping-company").send_keys("abc")
    driver.find_element(By.ID, "input-shipping-address-1").send_keys("HCM")
    driver.find_element(By.ID, "input-shipping-city").send_keys("HCM")
    driver.find_element(By.ID, "input-shipping-postcode").send_keys("1111")
    dropdown = Select(driver.find_element(By.ID, "input-shipping-country"))
    dropdown.select_by_value("230")
    time.sleep(5)
    dropdown_region = Select(driver.find_element(By.ID, "input-shipping-zone"))
    dropdown_region.select_by_value("3780")
    time.sleep(3)
    driver.find_element(By.ID, "button-shipping-address").click()
    time.sleep(3)
    # cuộn trang để không bị khuất các element
    legend_element = driver.find_element(By.XPATH, "//legend[contains(text(), 'Shipping Method')]")
    driver.execute_script("arguments[0].scrollIntoView();", legend_element)
    time.sleep(3)
    # chọn phương thức giao hàng
    driver.find_element(By.ID, "button-shipping-methods").click()
    time.sleep(5)
    driver.find_element(By.ID, "input-shipping-method-flat-flat").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='text-end']/button[@id='button-shipping-method']").click()
    # chọn phương thức thanh toán
    time.sleep(7)
    driver.find_element(By.ID, "button-payment-methods").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-payment-method-cod-cod").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='text-end']/button[@id='button-payment-method']").click()
    # cuộn trang để có thể chọn vào confirm button
    td_element = driver.find_element(By.XPATH, "//td[@class='text-start' and text()='Product Name']")
    driver.execute_script("arguments[0].scrollIntoView();", td_element)
    time.sleep(3)
    driver.find_element(By.ID, "button-confirm").click()
    time.sleep(3)
    # sẽ lấy được thông báo nếu đơn hàng đã được đặt
    account_header = driver.find_element(By.XPATH, "//h1[normalize-space()='Your order has been placed!']")
    assert account_header.is_displayed()

def test_checkout_with_guest(driver):
    driver.get("https://demo.opencart.com/")
    # tìm kiếm và thêm sản phẩm vào giỏ hàng
    search_input = driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys("HTC Touch")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(10)

    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    driver.execute_script("arguments[0].scrollIntoView();", product_items[0])
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "HTC Touch HD").click()
    time.sleep(5)
    quantity = driver.find_element(By.ID, "input-quantity")
    quantity.clear()
    quantity.send_keys("2")
    time.sleep(3)
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(10)
    # sau khi thêm sản phẩm thì chọn vào nút giỏ hàng để xem giỏ hàng thu nhỏ bên góc trên phải
    cart_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    driver.execute_script("arguments[0].scrollIntoView();", cart_button)
    cart_button.click()
    time.sleep(3)
    # chọn vào checkout element
    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-share").click()
    time.sleep(5)
    # chọn hình thức Guest checkout
    driver.find_element(By.ID, "input-guest").click()
    time.sleep(3)
    # điền thông tin
    driver.find_element(By.ID, "input-firstname").send_keys("Zoeee")
    driver.find_element(By.ID, "input-lastname").send_keys("Nguyen")
    driver.find_element(By.ID, "input-email").send_keys("admin123567890@gmail.com")

    driver.find_element(By.ID, "input-shipping-address-1").send_keys("HCM")
    driver.find_element(By.ID, "input-shipping-city").send_keys("HCM")
    driver.find_element(By.ID, "input-shipping-postcode").send_keys("1111")

    dropdown = Select(driver.find_element(By.ID, "input-shipping-country"))
    dropdown.select_by_value("230")
    time.sleep(5)
    dropdown_region = Select(driver.find_element(By.ID, "input-shipping-zone"))
    dropdown_region.select_by_value("3780")
    time.sleep(3)
    driver.find_element(By.ID, "button-register").click()
    time.sleep(3)
    # cuộn trang để không bị khuất các element
    legend_element = driver.find_element(By.XPATH, "//legend[contains(text(), 'Shipping Method')]")
    driver.execute_script("arguments[0].scrollIntoView();", legend_element)
    time.sleep(3)
    # chọn phương thức giao hàng
    driver.find_element(By.ID, "button-shipping-methods").click()
    time.sleep(5)
    driver.find_element(By.ID, "input-shipping-method-flat-flat").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='text-end']/button[@id='button-shipping-method']").click()
    # chọn phương thức thanh toán
    time.sleep(7)
    driver.find_element(By.ID, "button-payment-methods").click()
    time.sleep(3)
    driver.find_element(By.ID, "input-payment-method-cod-cod").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//div[@class='text-end']/button[@id='button-payment-method']").click()
    # cuộn trang để có thể chọn vào confirm button
    td_element = driver.find_element(By.XPATH, "//td[@class='text-start' and text()='Product Name']")
    driver.execute_script("arguments[0].scrollIntoView();", td_element)
    time.sleep(3)
    driver.find_element(By.ID, "button-confirm").click()
    time.sleep(3)
    # sẽ lấy được thông báo nếu đơn hàng đã được đặt
    account_header = driver.find_element(By.XPATH, "//h1[normalize-space()='Your order has been placed!']")
    assert account_header.is_displayed()