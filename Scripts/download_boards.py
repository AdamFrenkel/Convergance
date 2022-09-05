import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

def Monday_Process(driver):
    Switch_To_Onboarding(driver)
    time.sleep(5)
    download_Monday_Sheet(driver)
    Switch_To_Progressing(driver)
    time.sleep(5)
    download_Monday_Sheet(driver)

def Start_System():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("detach", True)
    options.add_argument("window-size=1200x600")
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    return driver

def OpenMondayPage(driver):
    driver.get("https://convergence-workforce.monday.com/boards/2530982973/views/57298038?finish_wizard=true")
    search = driver.find_element(By.ID, "user_email")
    search.send_keys("********@gmail.com")
    search = driver.find_element(By.ID, "user_password")
    search.send_keys("******")
    # Automated enter button pressed
    search.send_keys(Keys.RETURN)

WAITTIME = 30

def download_Monday_Sheet(driver):
    # Clicks menu button in corner
    menu = WebDriverWait(driver, WAITTIME).until(
        EC.element_to_be_clickable(
            (By.ID, "current-board-menu-button"))
    )
    menu.click()

    WebDriverWait(driver, WAITTIME).until(EC.element_to_be_clickable(
        (By.CLASS_NAME, "icon.icon-more-dots"))).click()
    
    exportToExcel = WebDriverWait(driver, WAITTIME).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "icon.icon-import-from-excel-template-outline"))
    )
    exportToExcel.click()

    checkbox = WebDriverWait(driver, WAITTIME).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[text()='Include updates']"))
    )
    try:
        checkbox = driver.find_element(By.XPATH, "//*[text()='Include subitems']")
        checkbox.click()
    except NoSuchElementException:
        pass

    export = WebDriverWait(driver, WAITTIME).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "export-button.monday-style-button.monday-style-button--size-medium.monday-style-button--kind-primary.monday-style-button--color-primary.has-style-size"))
    )
    export.click()

def Switch_To_Progressing(driver):
    progressing = WebDriverWait(driver, WAITTIME).until(
            EC.element_to_be_clickable(
                (By.ID, "board_item_2530983055"))
        )
    progressing.click()

def Switch_To_Onboarding(driver):
    onboarding = WebDriverWait(driver, WAITTIME).until(
        EC.element_to_be_clickable(
            (By.ID, "board_item_2530982973"))
    )
    onboarding.click()

def OpenApploiWindow(driver):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get("https://apploi-prod.sisense.com/app/main#/dashboards/5d24ff457a191329ac218927?l=true&r=true&embed=true")
    username = driver.find_element(By.NAME, "email")
    username.send_keys("*****@gmail.com")
    password = driver.find_element(By.NAME, "password")
    password.send_keys("****")

    submit = driver.find_element(By.XPATH, "//*[text()='Sign In']")
    submit.click()

    Applicants = WebDriverWait(driver, WAITTIME).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//*[text()='Applicant Details']"))
    )
    Applicants.click()

def download_Apploi_Sheet(driver):
    spacer = WebDriverWait(driver, WAITTIME).until(
        EC.visibility_of_any_elements_located((By.CLASS_NAME, "spacer"))
        )[-1]
    spacer.click()

    options = driver.find_elements(By.XPATH, "//button[@title='Options']")[-1]
    options.click()

    download = WebDriverWait(driver, WAITTIME).until(
        EC.element_to_be_clickable(
            (By.CLASS_NAME, "menu-item-arrow-holder"))
    )
    download.click()

    CSVfile = WebDriverWait(driver, WAITTIME).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='CSV File']"))
    )
    CSVfile.click()

# def changeDateFilter():
    # filterAttention = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((By.XPATH, "//*[text()='Application Date (Month)']"))
    # )
    # filterAttention.click()
    # print("click filter")

    # applicationDate = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((By.XPATH, "//*[text()='Application Date (Month)']"))
    # )
    # ActionChains(driver).move_to_element(applicationDate).perform()
    # print("move to element")

    # editDates = WebDriverWait(driver, 30).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, "//*[text()='Edit Filter']"))
    # )
    # editDates.click()
    # print("click edit filter")
    # print(len(editDates))
    # for btn in editDates:
    #     btn.click()
    #     time.sleep(15)
    #editDates[-2].click()
    # print("click filter")

    # last180days = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((By.XPATH, "//*[text()='Last 180 Days']"))
    # )
    # last180days.click()
    # print("click last 180 days")

    # OKbtn = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((By.XPATH, "//*[text()='OK']"))
    # )
    # OKbtn.click()
    # print("click OK")
