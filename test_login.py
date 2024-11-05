import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_with_valid_data_and_logout(driver):

    driver.get("https://demo.opencart.com/")
    # lấy ra my account element dưới phần footer
    my_account_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/account')]")
    # thực hiện câu lệnh này để cuộn trang đến element được chỉ định
    driver.execute_script("arguments[0].scrollIntoView();", my_account_link)

    # xử lý popup đã ngăn chặn hành động click vào my account element
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
        )
        close_button.click()
    except Exception:
        pass  # Nếu không có popup, tiếp tục

    my_account_link.click()
    time.sleep(20)

    # truyền vào email và password
    driver.find_element(By.ID, "input-email").send_keys("testZoe@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(3)

    # chọn ra subscriptions element để cuộn trang sao cho không bị mất logout element
    subscriptions = driver.find_element(By.XPATH, "//a[@class='list-group-item' and normalize-space()='Subscriptions']")
    driver.execute_script("arguments[0].scrollIntoView();", subscriptions)
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[@class='list-group-item' and normalize-space()='Logout']").click()

    # Nếu sau khi click vào log out hiển thị Account Logout thì thành công
    account_header = driver.find_element(By.XPATH, "//h1[normalize-space()='Account Logout']")
    assert account_header.is_displayed()

def test_login_with_invalid_email(driver):

    driver.get("https://demo.opencart.com/")

    # lấy ra my account element dưới phần footer
    my_account_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/account')]")
    # thực hiện câu lệnh này để cuộn trang đến element được chỉ định
    driver.execute_script("arguments[0].scrollIntoView();", my_account_link)
    # xử lý popup đã ngăn chặn hành động click vào my account element
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
        )
        close_button.click()
    except Exception:
        pass  # Nếu không có popup, tiếp tục

    my_account_link.click()
    time.sleep(20)
    # truyền vào email không đúng và password
    driver.find_element(By.ID, "input-email").send_keys("admin@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(3)
    # chọn ra message element
    error_message_element = driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")
    error_message = error_message_element.text
    time.sleep(3)
    # so sánh với nội dung của message đã lấy ra
    assert "Warning: No match for E-Mail Address and/or Password." in error_message

def test_login_with_invalid_password(driver):

    driver.get("https://demo.opencart.com/")

    # lấy ra my account element dưới phần footer
    my_account_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/account')]")
    # thực hiện câu lệnh này để cuộn trang đến element được chỉ định
    driver.execute_script("arguments[0].scrollIntoView();", my_account_link)
    # xử lý popup đã ngăn chặn hành động click vào my account element
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
        )
        close_button.click()
    except Exception:
        pass  # Nếu không có popup, tiếp tục

    my_account_link.click()
    time.sleep(20)
    # truyền vào email và password không đúng
    driver.find_element(By.ID, "input-email").send_keys("testZoe@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("1")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(3)
    # chọn ra message element
    error_message_element = driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")
    error_message = error_message_element.text
    time.sleep(3)
    # so sánh với nội dung của message đã lấy ra
    assert "Warning: No match for E-Mail Address and/or Password." in error_message

def test_login_with_empty_email(driver):
    driver.get("https://demo.opencart.com/")

    # lấy ra my account element dưới phần footer
    my_account_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/account')]")
    # thực hiện câu lệnh này để cuộn trang đến element được chỉ định
    driver.execute_script("arguments[0].scrollIntoView();", my_account_link)
    # xử lý popup đã ngăn chặn hành động click vào my account element
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
        )
        close_button.click()
    except Exception:
        pass  # Nếu không có popup, tiếp tục

    my_account_link.click()
    time.sleep(20)
    # truyền vào email rỗng và password
    driver.find_element(By.ID, "input-email").send_keys("")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(3)
    # chọn ra message element
    error_message_element = driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")
    error_message = error_message_element.text
    time.sleep(3)
    # so sánh với nội dung của message đã lấy ra
    assert "Warning: No match for E-Mail Address and/or Password." in error_message

def test_login_with_empty_password(driver):
    driver.get("https://demo.opencart.com/")

    # lấy ra my account element dưới phần footer
    my_account_link = driver.find_element(By.XPATH, "//a[contains(@href, 'route=account/account')]")
    # thực hiện câu lệnh này để cuộn trang đến element được chỉ định
    driver.execute_script("arguments[0].scrollIntoView();", my_account_link)
    # xử lý popup đã ngăn chặn hành động click vào my account element
    try:
        close_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'close-button-class')]"))
        )
        close_button.click()
    except Exception:
        pass  # Nếu không có popup, tiếp tục

    my_account_link.click()
    time.sleep(20)
    # truyền vào email và password rỗng
    driver.find_element(By.ID, "input-email").send_keys("testZoe@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]").click()
    time.sleep(3)
    # chọn ra message element
    error_message_element = driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")
    error_message = error_message_element.text
    time.sleep(3)
    # so sánh với nội dung của message đã lấy ra
    assert "Success: " in error_message
