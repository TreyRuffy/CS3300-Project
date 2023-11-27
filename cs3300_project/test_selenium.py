from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class SeleniumTesting(LiveServerTestCase):
    def test_create_horse(self):
        service = Service()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(self.live_server_url + "/logout")
        driver.implicitly_wait(0.5)
        driver.get(self.live_server_url + "/login")
        driver.implicitly_wait(0.5)
        driver.set_window_size(787, 816)
        driver.find_element(By.CSS_SELECTOR, ".h-5").click()
        driver.find_element(By.NAME, "username").send_keys("testing123")
        driver.find_element(By.NAME, "password").send_keys("happypass1")
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        driver.implicitly_wait(0.5)
        driver.find_element(By.LINK_TEXT, "+").click()
        driver.find_element(By.ID, "id_name").click()
        driver.find_element(By.ID, "id_name").send_keys("horse test")
        driver.find_element(By.ID, "id_short_description").send_keys("short description")
        driver.find_element(By.ID, "id_long_description").send_keys("long horse description")
        driver.find_element(By.CSS_SELECTOR, ".btn-neutral").click()
        driver.implicitly_wait(0.5)
    
    def test_delete_horse(self):
        driver = webdriver.Chrome()
        driver.get(self.live_server_url + "/logout")
        driver.implicitly_wait(0.5)
        driver.get(self.live_server_url + "/login")
        driver.implicitly_wait(0.5)
        driver.set_window_size(787, 816)
        driver.find_element(By.CSS_SELECTOR, ".h-5").click()
        driver.find_element(By.NAME, "username").send_keys("testing123")
        driver.find_element(By.NAME, "password").send_keys("happypass1")
        driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        driver.implicitly_wait(0.5)
        driver.find_element(By.LINK_TEXT, "horse test").click()
        driver.find_element(By.LINK_TEXT, "Delete").click()
        driver.implicitly_wait(0.5)
