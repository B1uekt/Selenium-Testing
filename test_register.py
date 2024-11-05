import pytest
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_register_with_valid_data(driver):

    driver.get("https://demo.opencart.com/en-gb?route=account/register")
    time.sleep(5)
    # truyền vào firstname, lastname, email và password hợp lệ
    driver.find_element(By.ID, "input-firstname").send_keys("Zoe")
    driver.find_element(By.ID, "input-lastname").send_keys("Nguyen")
    driver.find_element(By.ID, "input-email").send_keys("testZoe12@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")

    legend_element = driver.find_element(By.XPATH, "//legend[contains(text(), 'Newsletter')]")
    driver.execute_script("arguments[0].scrollIntoView();", legend_element)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name='agree' and @class='form-check-input']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
    time.sleep(3)

    register_header = driver.find_element(By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']")
    assert register_header.is_displayed()

def test_register_with_specical_name(driver):

    driver.get("https://demo.opencart.com/en-gb?route=account/register")
    time.sleep(5)
    # truyền vào firstname, lastname với kí tự đặc biệt
    driver.find_element(By.ID, "input-firstname").send_keys("@@@@")
    driver.find_element(By.ID, "input-lastname").send_keys("#####")
    driver.find_element(By.ID, "input-email").send_keys("testZoe1223@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")

    legend_element = driver.find_element(By.XPATH, "//legend[contains(text(), 'Newsletter')]")
    driver.execute_script("arguments[0].scrollIntoView();", legend_element)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name='agree' and @class='form-check-input']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
    time.sleep(3)

    register_header = driver.find_element(By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']")
    assert not register_header.is_displayed()

def test_register_with_existing_email(driver):

    driver.get("https://demo.opencart.com/en-gb?route=account/register")
    time.sleep(5)
    # truyền vào email đã có sẵn
    driver.find_element(By.ID, "input-firstname").send_keys("Zoe")
    driver.find_element(By.ID, "input-lastname").send_keys("Nguyen")
    driver.find_element(By.ID, "input-email").send_keys("testZoe@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")

    legend_element = driver.find_element(By.XPATH, "//legend[contains(text(), 'Newsletter')]")
    driver.execute_script("arguments[0].scrollIntoView();", legend_element)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name='agree' and @class='form-check-input']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
    time.sleep(3)

    error_message_element = driver.find_element(By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")
    error_message = error_message_element.text
    time.sleep(3)
    # so sánh với nội dung của message đã lấy ra
    assert "Warning: E-Mail Address is already registered!" in error_message

def test_register_with_empty_name(driver):

    driver.get("https://demo.opencart.com/en-gb?route=account/register")
    time.sleep(5)
    # truyền vào firstname, lastname rỗng
    driver.find_element(By.ID, "input-firstname").send_keys("")
    driver.find_element(By.ID, "input-lastname").send_keys("")
    driver.find_element(By.ID, "input-email").send_keys("testZoe122223@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")

    legend_element = driver.find_element(By.XPATH, "//legend[contains(text(), 'Newsletter')]")
    driver.execute_script("arguments[0].scrollIntoView();", legend_element)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name='agree' and @class='form-check-input']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
    time.sleep(3)

    error_message_element = driver.find_element(By.ID, "error-firstname")
    error_message = error_message_element.text
    time.sleep(3)
    # so sánh với nội dung của message đã lấy ra
    assert "First Name must be between 1 and 32 characters!" in error_message

def test_register_with_full_name(driver):
    driver.get("https://demo.opencart.com/en-gb?route=account/register")
    time.sleep(5)
    long_firstname = "A" * 33  # 33 ký tự
    long_lastname = "B" * 33
    # truyền vào firstname, lastname với 33 ký tự
    driver.find_element(By.ID, "input-firstname").send_keys(long_firstname)
    driver.find_element(By.ID, "input-lastname").send_keys(long_lastname)
    driver.find_element(By.ID, "input-email").send_keys("testZoe122223@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")

    legend_element = driver.find_element(By.XPATH, "//legend[contains(text(), 'Newsletter')]")
    driver.execute_script("arguments[0].scrollIntoView();", legend_element)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name='agree' and @class='form-check-input']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
    time.sleep(3)

    error_message_element = driver.find_element(By.ID, "error-firstname")
    error_message = error_message_element.text
    time.sleep(3)
    # so sánh với nội dung của message đã lấy ra
    assert "First Name must be between 1 and 32 characters!" in error_message

def test_register_with_exact_32_characters(driver):
    driver.get("https://demo.opencart.com/en-gb?route=account/register")
    time.sleep(5)
    long_firstname = "A" * 32
    long_lastname = "B" * 32
    # truyền vào firstname, lastname với 32 ký tự
    driver.find_element(By.ID, "input-firstname").send_keys(long_firstname)
    driver.find_element(By.ID, "input-lastname").send_keys(long_lastname)
    driver.find_element(By.ID, "input-email").send_keys("testZoe122223@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123456")

    legend_element = driver.find_element(By.XPATH, "//legend[contains(text(), 'Newsletter')]")
    driver.execute_script("arguments[0].scrollIntoView();", legend_element)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name='agree' and @class='form-check-input']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
    time.sleep(3)

    register_header = driver.find_element(By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']")
    assert register_header.is_displayed()

def test_register_with_error_email(driver):
    driver.get("https://demo.opencart.com/en-gb?route=account/register")
    time.sleep(5)
    long_firstname = "A" * 32
    long_lastname = "B" * 32
    # truyền vào email không đúng định dạng
    driver.find_element(By.ID, "input-firstname").send_keys(long_firstname)
    driver.find_element(By.ID, "input-lastname").send_keys(long_lastname)
    driver.find_element(By.ID, "input-email").send_keys("testZoe122223")
    driver.find_element(By.ID, "input-password").send_keys("123456")
    # cuộn trang để không bị khuất element
    legend_element = driver.find_element(By.XPATH, "//legend[contains(text(), 'Newsletter')]")
    driver.execute_script("arguments[0].scrollIntoView();", legend_element)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name='agree' and @class='form-check-input']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
    time.sleep(3)

    try:
        error_message_element = driver.find_element(By.ID, "error-email")
        error_message = error_message_element.text
        print(f"Error message: {error_message}")  # In ra thông báo lỗi nếu có
    except NoSuchElementException:
        assert False, "Error message for email not found. Test failed!"

def test_register_with_short_password(driver):

    driver.get("https://demo.opencart.com/en-gb?route=account/register")
    time.sleep(5)
    short_password = "123"  # Mật khẩu chỉ 3 ký tự
    # truyền vào password có 3 kí tự
    driver.find_element(By.ID, "input-firstname").send_keys("Zoe")
    driver.find_element(By.ID, "input-lastname").send_keys("Nguyen")
    driver.find_element(By.ID, "input-email").send_keys("testZoe122223@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys(short_password)

    legend_element = driver.find_element(By.XPATH, "//legend[contains(text(), 'Newsletter')]")
    driver.execute_script("arguments[0].scrollIntoView();", legend_element)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name='agree' and @class='form-check-input']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
    time.sleep(3)

    error_message_element = driver.find_element(By.ID, "error-password")
    error_message = error_message_element.text
    time.sleep(3)
    # so sánh với nội dung của message đã lấy ra
    assert "Password must be between 4 and 20 characters!" in error_message

def test_register_with_long_password(driver):

    driver.get("https://demo.opencart.com/en-gb?route=account/register")
    time.sleep(5)
    long_password = "1" * 25  # Mật khẩu chỉ 3 ký tự
    # truyền vào password có 25 kí tự
    driver.find_element(By.ID, "input-firstname").send_keys("Zoe")
    driver.find_element(By.ID, "input-lastname").send_keys("Nguyen")
    driver.find_element(By.ID, "input-email").send_keys("testZoe12333@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys(long_password)

    legend_element = driver.find_element(By.XPATH, "//legend[contains(text(), 'Newsletter')]")
    driver.execute_script("arguments[0].scrollIntoView();", legend_element)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name='agree' and @class='form-check-input']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
    time.sleep(3)

    register_header = driver.find_element(By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']")
    # nếu như vẫn hiển thị Your Account Has Been Created! thì fail do password chỉ từ 4-20 kí tự
    assert not register_header.is_displayed()

def test_register_with_password_exact_4_characters(driver):
    driver.get("https://demo.opencart.com/en-gb?route=account/register")
    time.sleep(5)
    short_password = "1234"  # Mật khẩu chỉ 3 ký tự
    # truyền vào firstname, lastname, email và password
    driver.find_element(By.ID, "input-firstname").send_keys("Zoe")
    driver.find_element(By.ID, "input-lastname").send_keys("Nguyen")
    driver.find_element(By.ID, "input-email").send_keys("testZoeabc@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys(short_password)

    legend_element = driver.find_element(By.XPATH, "//legend[contains(text(), 'Newsletter')]")
    driver.execute_script("arguments[0].scrollIntoView();", legend_element)
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@name='agree' and @class='form-check-input']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Continue')]").click()
    time.sleep(3)

    register_header = driver.find_element(By.XPATH, "//h1[normalize-space()='Your Account Has Been Created!']")
    # nếu như vẫn hiển thị Your Account Has Been Created! thì pass do password chỉ từ 4-20 kí tự
    assert register_header.is_displayed()