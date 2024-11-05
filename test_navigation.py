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

def test_navigation(driver):
    driver.get("https://demo.opencart.com/")
    time.sleep(3)
    # Chọn vào desktop element để chuyển sang trang Desktop
    desktop_menu = driver.find_element(By.LINK_TEXT, "Desktops")
    desktop_menu.click()
    mac_option = driver.find_element(By.LINK_TEXT, "Mac (1)")
    mac_option.click()
    time.sleep(10)

    # Chọn vào desktop element để chuyển sang trang Desktop
    lap_note_menu = driver.find_element(By.LINK_TEXT, "Laptops & Notebooks")
    lap_note_menu.click()
    time.sleep(5)


    # Chọn vào desktop element để chuyển sang trang Desktop
    components_menu = driver.find_element(By.LINK_TEXT, "Components")
    components_menu.click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Show All Components").click()
    time.sleep(5)

    # Chọn vào desktop element để chuyển sang trang Desktop
    tablets_menu = driver.find_element(By.LINK_TEXT, "Tablets")
    tablets_menu.click()
    time.sleep(5)

    # Chọn vào desktop element để chuyển sang trang Desktop
    tablets_menu = driver.find_element(By.LINK_TEXT, "Software")
    tablets_menu.click()
    time.sleep(5)

    # Chọn vào desktop element để chuyển sang trang Desktop
    p_PDA_menu = driver.find_element(By.LINK_TEXT, "Phones & PDAs")
    p_PDA_menu.click()
    time.sleep(5)

    # Chọn vào desktop element để chuyển sang trang Desktop
    p_PDA_menu = driver.find_element(By.LINK_TEXT, "Cameras")
    p_PDA_menu.click()
    time.sleep(5)

    # Chọn vào desktop element để chuyển sang trang Desktop
    mp3_menu = driver.find_element(By.LINK_TEXT, "MP3 Players")
    mp3_menu.click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Show All MP3 Players").click()
    time.sleep(5)
    # nếu như tiêu đề cuối cùng là MP3 Players" thì chuyển trang đúng
    assert "MP3 Players" in driver.title