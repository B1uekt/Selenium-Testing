import pytest
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_data_validation_with_random_quantity(driver):
    driver.get("https://demo.opencart.com/")
    # thêm sản phẩm bằng cách tìm từ khóa
    my_account_link = driver.find_element(By.NAME, "search")
    my_account_link.clear()
    my_account_link.send_keys("iphone")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(10)

    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    driver.execute_script("arguments[0].scrollIntoView();", product_items[0])
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "iPhone").click()
    time.sleep(5)
    quantity = driver.find_element(By.ID, "input-quantity")
    quantity.clear()
    # nhập random quantity để tính toán tổng tiền có chính xác hay không
    random_integer = random.randint(1, 100)
    random_integer_str = str(random_integer)

    quantity.send_keys(random_integer_str)
    time.sleep(3)
    # lấy giá hiển thị trong trang thông tin chi tiết sản phẩm
    price = driver.find_element(By.CLASS_NAME, "price-new")
    # tách để lấy phần giá
    numeric_value = float(price.text.replace("$", ""))

    driver.find_element(By.ID, "button-cart").click()
    time.sleep(10)
    # sau khi thêm sản phẩm thì chọn vào nút giỏ hàng để xem giỏ hàng thu nhỏ bên góc trên phải
    cart_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    driver.execute_script("arguments[0].scrollIntoView();", cart_button)
    cart_button.click()
    time.sleep(3)
    # lấy ra tổng giá trị đã tính toán
    total_value_element = driver.find_element(By.XPATH, "//td[.='Total']/following-sibling::td")
    total_value = total_value_element.text

    # Lấy giá trị số từ chuỗi actual_value và làm tròn
    total = random_integer*numeric_value
    formatted_value = f"${total:,.2f}"
    # so sánh xem tổng giá trị có khớp khi lấy quantity nhân với giá sản phẩm hay không
    assert total_value == formatted_value, f"Expected {formatted_value} but got {total_value}"

def test_data_validation_with_fixed_quantity(driver):
    driver.get("https://demo.opencart.com/")
    # thêm sản phẩm bằng cách tìm từ khóa
    my_account_link = driver.find_element(By.NAME, "search")
    my_account_link.clear()
    my_account_link.send_keys("iphone")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(10)

    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    driver.execute_script("arguments[0].scrollIntoView();", product_items[0])
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "iPhone").click()
    time.sleep(5)
    quantity = driver.find_element(By.ID, "input-quantity")
    quantity.clear()
    # nhập quantity cố định
    quantity.send_keys("2")
    time.sleep(3)
    # lấy giá hiển thị trong trang thông tin chi tiết sản phẩm
    price = driver.find_element(By.CLASS_NAME, "price-new")
    # tách để lấy phần giá
    numeric_value = float(price.text.replace("$", ""))

    driver.find_element(By.ID, "button-cart").click()
    time.sleep(10)
    # sau khi thêm sản phẩm thì chọn vào nút giỏ hàng để xem giỏ hàng thu nhỏ bên góc trên phải
    cart_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    driver.execute_script("arguments[0].scrollIntoView();", cart_button)
    cart_button.click()
    time.sleep(3)
    # lấy ra tổng giá trị đã tính toán
    total_value_element = driver.find_element(By.XPATH, "//td[.='Total']/following-sibling::td")
    total_value = total_value_element.text

    # Lấy giá trị đã cho trước * với giá tiền trên trang web
    total = 2*numeric_value
    formatted_value = f"${total:,.2f}"
    # so sánh xem tổng giá trị có khớp giá trị đã tính hay không
    assert total_value == formatted_value, f"Expected {formatted_value} but got {total_value}"