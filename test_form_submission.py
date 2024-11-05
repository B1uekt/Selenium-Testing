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

def test_form_submission_with_valid_data(driver):

    driver.get("https://demo.opencart.com/")
    # lấy ra my return element dưới phần footer
    return_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/returns.add')]")
    # thực hiện câu lệnh này để cuộn trang đến element được chỉ định
    driver.execute_script("arguments[0].scrollIntoView();", return_link)

    # xử lý popup đã ngăn chặn hành động click vào return element
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
        )
        close_button.click()
    except Exception:
        pass  # Nếu không có popup, tiếp tục

    return_link.click()
    time.sleep(20)

    # truyền data vào form
    driver.find_element(By.ID, "input-firstname").send_keys("Zoe")
    driver.find_element(By.ID, "input-lastname").send_keys("Nguyen")
    driver.find_element(By.ID, "input-email").send_keys("testZoe@gmail.com")
    driver.find_element(By.ID, "input-telephone").send_keys("0123456789")
    driver.find_element(By.ID, "input-order-id").send_keys("11111")
    order_date = driver.find_element(By.ID, "input-date-ordered")
    driver.execute_script("arguments[0].scrollIntoView();", order_date)
    order_date.send_keys("2024-10-26")
    time.sleep(3)
    driver.find_element(By.ID, "input-product").send_keys("iphone")
    driver.find_element(By.ID, "input-model").send_keys("product 11")
    driver.find_element(By.XPATH, "//input[@name='return_reason_id' and @value='2']").click()
    driver.find_element(By.ID, "input-opened-yes").click()
    time.sleep(3)
    # chọn nút submit
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    time.sleep(5)
    # Nếu sau khi click vào log out hiển thị Product Returns thì thành công
    product_returns = driver.find_element(By.XPATH, "//h1[normalize-space()='Product Returns']")
    assert product_returns.is_displayed()

def test_form_submission_with_invalid_orderdate(driver):

    driver.get("https://demo.opencart.com/")
    # lấy ra my return element dưới phần footer
    return_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/returns.add')]")
    # thực hiện câu lệnh này để cuộn trang đến element được chỉ định
    driver.execute_script("arguments[0].scrollIntoView();", return_link)

    # xử lý popup đã ngăn chặn hành động click vào return element
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
        )
        close_button.click()
    except Exception:
        pass  # Nếu không có popup, tiếp tục

    return_link.click()
    time.sleep(20)

    # truyền data vào form
    driver.find_element(By.ID, "input-firstname").send_keys("Zoe")
    driver.find_element(By.ID, "input-lastname").send_keys("Nguyen")
    driver.find_element(By.ID, "input-email").send_keys("testZoe@gmail.com")
    driver.find_element(By.ID, "input-telephone").send_keys("0123456789")
    driver.find_element(By.ID, "input-order-id").send_keys("11111")
    order_date = driver.find_element(By.ID, "input-date-ordered")
    driver.execute_script("arguments[0].scrollIntoView();", order_date)
    # chọn 1 ngày của tương lai
    order_date.send_keys("2024-11-10")
    time.sleep(3)
    driver.find_element(By.ID, "input-product").send_keys("iphone")
    driver.find_element(By.ID, "input-model").send_keys("product 11")
    driver.find_element(By.XPATH, "//input[@name='return_reason_id' and @value='2']").click()
    driver.find_element(By.ID, "input-opened-yes").click()
    time.sleep(3)
    # chọn nút submit
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    time.sleep(5)
    # lấy ra tiêu đề
    product_returns = driver.find_element(By.XPATH, "//h1[normalize-space()='Product Returns']")
    # nếu như vẫn hiển thị Product Returns thì fail do ngày đặt của đơn hàng trước thời gian hiện tại
    assert not product_returns.is_displayed()

def test_form_submission_with_invalid_info(driver):

    driver.get("https://demo.opencart.com/")
    # lấy ra my return element dưới phần footer
    return_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/returns.add')]")
    # thực hiện câu lệnh này để cuộn trang đến element được chỉ định
    driver.execute_script("arguments[0].scrollIntoView();", return_link)

    # xử lý popup đã ngăn chặn hành động click vào return element
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
        )
        close_button.click()
    except Exception:
        pass  # Nếu không có popup, tiếp tục

    return_link.click()
    time.sleep(20)

    # truyền data vào form
    driver.find_element(By.ID, "input-firstname").send_keys("@@@@")
    driver.find_element(By.ID, "input-lastname").send_keys("@@@@@@")
    driver.find_element(By.ID, "input-email").send_keys("testZoe@gmail.com")
    driver.find_element(By.ID, "input-telephone").send_keys("0123456789")
    driver.find_element(By.ID, "input-order-id").send_keys("11111")
    order_date = driver.find_element(By.ID, "input-date-ordered")
    driver.execute_script("arguments[0].scrollIntoView();", order_date)
    order_date.send_keys("2024-11-10")
    time.sleep(3)
    driver.find_element(By.ID, "input-product").send_keys("iphone")
    driver.find_element(By.ID, "input-model").send_keys("product 11")
    driver.find_element(By.XPATH, "//input[@name='return_reason_id' and @value='2']").click()
    driver.find_element(By.ID, "input-opened-yes").click()
    time.sleep(3)
    # chọn nút submit
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    time.sleep(5)
    # lấy ra tiêu đề
    product_returns = driver.find_element(By.XPATH, "//h1[normalize-space()='Product Returns']")
    # nếu như vẫn hiển thị Product Returns thì fail do First Name và Last Name đều không hợp lệ
    assert not product_returns.is_displayed()