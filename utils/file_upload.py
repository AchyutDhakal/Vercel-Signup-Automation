from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

UPLOAD_FILE_INPUT = (By.XPATH, "(//input[@type='file'])[1]")

def upload_file(driver, file_path=r"G:\Downloads\Achyut_CV.pdf"):
    wait = WebDriverWait(driver, 20)

    file_input = wait.until(
        EC.presence_of_element_located(UPLOAD_FILE_INPUT)
    )

    driver.execute_script(
        "arguments[0].style.display='block'; arguments[0].style.opacity=1;",
        file_input
    )

    file_input.send_keys(file_path)


