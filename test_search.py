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

@pytest.fixture(params=["chrome", "firefox"])  # Thêm firefox vào danh sách tham số
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()  # Sử dụng geckodriver cho Firefox
    driver.maximize_window()
    yield driver
    driver.quit()

def test_search_with_valid_keyword(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)
    # lấy ô search và truyền vào keyword iphone để test cho trường hợp keyword hợp lệ
    search_element = driver.find_element(By.NAME, "search")
    search_element.clear()
    search_element.send_keys("iPhone")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(10)

    # lấy hết tất cả các sản phẩm theo keyword
    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    time.sleep(3)

    assert len(product_items) > 0

def test_search_with_whitespace(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)
    # lấy ô search và truyền vào khoảng trắng để test cho trường hợp keyword = ""
    my_account_link = driver.find_element(By.NAME, "search")
    my_account_link.clear()
    my_account_link.send_keys("")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(3)
    # lấy dòng text khi tìm kiếm bằng khoảng trắng
    message = driver.find_element(By.XPATH,
                                  "//p[normalize-space()='There is no product that matches the search criteria.']")
    # nếu danh sách sản phẩm > 0 và lấy được dòng text thì mới pass search functionality
    assert message.is_displayed()

def test_search_with_special_character(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)
    # lấy ô search và truyền vào khoảng trắng để test cho trường hợp keyword bằng kí tự đặc biệt
    my_account_link = driver.find_element(By.NAME, "search")
    my_account_link.clear()
    my_account_link.send_keys("@@##$")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(3)
    # lấy dòng text khi tìm kiếm bằng khoảng trắng
    message = driver.find_element(By.XPATH,
                                  "//p[normalize-space()='There is no product that matches the search criteria.']")
    # lấy được dòng text không có sản phẩm phù hợp
    assert message.is_displayed()

def test_search_with_lower_keyword(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)
    # lấy ô search và truyền vào keyword iphone để test cho trường hợp keyword viết thường
    search_element = driver.find_element(By.NAME, "search")
    search_element.clear()
    search_element.send_keys("iphone")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(10)

    # lấy hết tất cả các sản phẩm theo keyword
    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    time.sleep(3)

    assert len(product_items) > 0

def test_search_with_uppercase_keyword(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)
    # lấy ô search và truyền vào keyword IPHONE để test cho trường hợp keyword viết hoa
    search_element = driver.find_element(By.NAME, "search")
    search_element.clear()
    search_element.send_keys("IPHONE")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(10)

    # lấy hết tất cả các sản phẩm theo keyword
    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    time.sleep(3)

    assert len(product_items) > 0

def test_search_with_keyword_containing_whitespace(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)
    # lấy ô search và truyền vào keyword HTC Touch để test cho trường hợp keyword chứa khoảng trắng
    search_element = driver.find_element(By.NAME, "search")
    search_element.clear()
    search_element.send_keys("HTC Touch")
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-light.btn-lg").click()
    time.sleep(10)

    # lấy hết tất cả các sản phẩm theo keyword
    product_items = driver.find_elements(By.CSS_SELECTOR, ".product-thumb")
    time.sleep(3)

    assert len(product_items) > 0