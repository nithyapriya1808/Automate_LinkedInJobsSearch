import webbrowser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

options = Options()
options.binary_location = r'C:\\Users\\VEERANI2\\AppData\\Local\\Mozilla Firefox\\firefox.exe'

driver = webdriver.Firefox(executable_path=r'geckodriver.exe', options=options)
driver.get('http://linkedin.com/')

try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'session_password')))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")
# driver.find_element_by_id('session_password').sendKeys("nithya.v@outlook.com")
# button.click()

username = driver.find_element_by_id("session_key")

password = driver.find_element_by_id("session_password")

username.send_keys("nithya.v@outlook.com")

password.send_keys("Mother21$")

driver.find_element_by_css_selector(".sign-in-form__submit-button").click()
try:
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'remember-me-prompt__form-secondary')))
    driver.find_element_by_css_selector(".btn__primary--large").click()
except TimeoutException:
    pass;

try:
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'ember25')))
    url="/jobs/"
    driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
except TimeoutException:
    print("error")
    
try:
    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.CLASS_NAME, 'msg-overlay-bubble-header__button truncate ml2')))
    driver.find_element_by_css_selector(".msg-overlay-bubble-header__button truncate ml2").click()
except TimeoutException:
    pass;
