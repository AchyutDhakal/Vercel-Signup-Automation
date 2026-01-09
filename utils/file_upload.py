# import os
# from selenium.webdriver.common.by import By

# # Absolute path is REQUIRED
# def upload_file(driver):
#     UPLOAD_FILE_INPUT=(By.XPATH,"(//span[normalize-space()='Upload a file'])[1]")
#     file_path = os.path.abspath("G:\Downloads\Achyut_CV.pdf")

#     upload_input = driver.find_element(*UPLOAD_FILE_INPUT)
#     upload_input.send_keys(file_path)

# import os
# from selenium.webdriver.common.by import By

# UPLOAD_FILE_INPUT = (By.XPATH, "(//span[normalize-space()='Upload a file'])[1]")

# def upload_file(driver, file_name="G:\Downloads\Achyut_CV.pdf"):
#     base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     file_path = os.path.join(base_dir, "data", file_name)

#     upload_input = driver.find_element(*UPLOAD_FILE_INPUT)
#     upload_input.send_keys(file_path)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

UPLOAD_FILE_INPUT = (By.XPATH, "(//input[@type='file'])[1]")

def upload_file(driver, file_path=r"G:\Downloads\Achyut_CV.pdf"):
    wait = WebDriverWait(driver, 20)

    file_input = wait.until(
        EC.presence_of_element_located(UPLOAD_FILE_INPUT)
    )

    # Force-enable hidden input
    driver.execute_script(
        "arguments[0].style.display='block'; arguments[0].style.opacity=1;",
        file_input
    )

    file_input.send_keys(file_path)


