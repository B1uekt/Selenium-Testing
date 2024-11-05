import pytest
import time
import requests
import random
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

def test_add_single_products(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)
    # thêm sản phẩm bằng cách tìm từ khóa
    my_account_link = driver.find_element(By.NAME, "search")
    my_account_link.clear()
    my_account_link.send_keys("iphone")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(5)

    # lấy ra danh sách sản phẩm và cuộn trang đến sản phẩm hiển thị đầu tiên
    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    driver.execute_script("arguments[0].scrollIntoView();", product_items[0])
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "iPhone").click()
    time.sleep(5)
    # xóa ô quantity và nhập số lượng sau đó chọn thêm sản phẩm
    quantity = driver.find_element(By.ID, "input-quantity")
    quantity.clear()
    quantity.send_keys("1")
    time.sleep(5)
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(10)
    # sau khi thêm sản phẩm thì chọn vào nút giỏ hàng để xem giỏ hàng thu nhỏ bên góc trên phải
    cart_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    driver.execute_script("arguments[0].scrollIntoView();", cart_button)
    cart_button.click()
    time.sleep(3)
    # chọn vào nút View Cart để chuyển qua trang chi tiết giỏ hàng
    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
    time.sleep(5)
    # lấy tên sản phẩm vừa thêm vào giỏ hàng
    td_element = driver.find_element(By.CSS_SELECTOR, "td.text-start.text-wrap")
    td_text = td_element.text
    # so sánh xem tên sản phẩm đã đúng hay chưa
    assert td_text == "iPhone"

def test_add_multiple_products(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)
    # thêm sản phẩm bằng cách tìm từ khóa
    search_input = driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys("iphone")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(5)

    # lấy ra danh sách sản phẩm và cuộn trang đến sản phẩm hiển thị đầu tiên
    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    driver.execute_script("arguments[0].scrollIntoView();", product_items[0])
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "iPhone").click()
    time.sleep(5)
    # xóa ô quantity và nhập số lượng sau đó chọn thêm sản phẩm
    quantity = driver.find_element(By.ID, "input-quantity")
    quantity.clear()
    quantity.send_keys("1")
    time.sleep(5)
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(10)
    # tìm tiếp sản phẩm thứ 2
    search_input = driver.find_element(By.NAME, "search")
    search_input.clear()
    search_input.send_keys("macbook")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(5)

    # lấy ra danh sách sản phẩm và cuộn trang đến sản phẩm hiển thị đầu tiên
    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    driver.execute_script("arguments[0].scrollIntoView();", product_items[0])
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "MacBook").click()
    time.sleep(5)
    # xóa ô quantity và nhập số lượng sau đó chọn thêm sản phẩm
    quantity = driver.find_element(By.ID, "input-quantity")
    quantity.clear()
    quantity.send_keys("1")
    time.sleep(5)
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(10)

    # sau khi thêm sản phẩm thì chọn vào nút giỏ hàng để xem giỏ hàng thu nhỏ bên góc trên phải
    cart_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    driver.execute_script("arguments[0].scrollIntoView();", cart_button)
    cart_button.click()
    time.sleep(3)
    # chọn vào nút View Cart để chuyển qua trang chi tiết giỏ hàng
    driver.find_element(By.CSS_SELECTOR, ".fa-solid.fa-cart-shopping").click()
    time.sleep(5)
    # lấy tên các sản phẩm vừa thêm vào giỏ hàng thêm vào trong list
    cart_product_elements = driver.find_elements(By.CSS_SELECTOR, "td.text-start.text-wrap")
    cart_product_names = [element.text for element in cart_product_elements]
    # so sánh xem 2 tên sản phẩm đã đúng hay chưa
    assert any("iPhone" in name for name in cart_product_names), "iPhone is not in the cart."
    assert any("MacBook" in name for name in cart_product_names), "MacBook is not in the cart."

def test_add_product_with_negative_quantity(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)
    # thêm sản phẩm bằng cách tìm từ khóa
    my_account_link = driver.find_element(By.NAME, "search")
    my_account_link.clear()
    my_account_link.send_keys("iphone")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(5)

    # lấy ra danh sách sản phẩm và cuộn trang đến sản phẩm hiển thị đầu tiên
    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    driver.execute_script("arguments[0].scrollIntoView();", product_items[0])
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "iPhone").click()
    time.sleep(5)
    # xóa ô quantity và nhập số lượng sau đó chọn thêm sản phẩm
    quantity = driver.find_element(By.ID, "input-quantity")
    quantity.clear()
    # nhập quantity <0 để kiểm tra
    quantity.send_keys("-1")
    time.sleep(5)
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(3)
    # lấy thông báo lỗi
    error_message_element = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    error_message = error_message_element.text
    time.sleep(3)
    # so sánh với nội dung của message đã lấy ra
    assert "Success: You have added" in error_message

def test_add_same_product_multiple_times(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)
    # thêm sản phẩm bằng cách tìm từ khóa
    my_account_link = driver.find_element(By.NAME, "search")
    my_account_link.clear()
    my_account_link.send_keys("iphone")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(5)

    # lấy ra danh sách sản phẩm và cuộn trang đến sản phẩm hiển thị đầu tiên
    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    driver.execute_script("arguments[0].scrollIntoView();", product_items[0])
    time.sleep(3)
    driver.find_element(By.LINK_TEXT, "iPhone").click()
    time.sleep(5)
    # xóa ô quantity và nhập số lượng sau đó chọn thêm sản phẩm
    quantity = driver.find_element(By.ID, "input-quantity")
    quantity.clear()
    quantity.send_keys("1")
    time.sleep(5)
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(5)
    # chọn thêm sản phẩm 1 lần nữa
    driver.find_element(By.ID, "button-cart").click()
    time.sleep(10)
    # sau khi thêm sản phẩm thì chọn vào nút giỏ hàng để xem giỏ hàng thu nhỏ bên góc trên phải
    cart_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    driver.execute_script("arguments[0].scrollIntoView();", cart_button)
    cart_button.click()
    time.sleep(3)

    quantity_in_cart = driver.find_element(By.XPATH, "//td[@class='text-end'][1]")
    quantity_value = quantity_in_cart.text
    # so sánh xem số lượng có phải bằng 2 khi thêm 2 lần 1 sản phẩm không
    assert quantity_value == "x 2"