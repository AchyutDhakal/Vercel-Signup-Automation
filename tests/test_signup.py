import pytest
from pages.signup_page import SignupPage
from utils.test_runner import create_driver
from utils.otp_reader import get_otp_from_email
from utils.file_upload import upload_file
from data.test_data import VALID_DATA
from utils.assertions import assert_true
import time
import allure


class TestSignup:
    def setup_method(self):
        self.driver = create_driver()
        self.signup_page = SignupPage(self.driver)

        self.driver.get("https://authorized-partner.vercel.app/")

    def teardown_method(self):
        self.driver.quit()

    @allure.title("Test User Signup")
    @pytest.mark.parametrize("valid_data",VALID_DATA)
    def test_user_signup(self, valid_data):
        with allure.step("Navigate to Login Page"):
            self.signup_page.click_login_link()
            time.sleep(2)
            assert_true("login" in self.driver.current_url, "Login page did not load correctly", "login_link",self.signup_page)

        with allure.step("Navigate to Signup Page"):
            self.signup_page.click_signup_link()
            time.sleep(2)
            assert_true("register" in self.driver.current_url, "Signup page did not load correctly","signup_link", self.signup_page)
        
        with allure.step("Check privacy policy checkbox and click on continue"):
            self.signup_page.click_privacy_policy_checkbox()
            self.signup_page.click_continue_button()

        with allure.step("Setting up account details and otp verification"):
            self.signup_page.enter_first_name(valid_data["first_name"])
            self.signup_page.enter_last_name(valid_data["last_name"])
            self.signup_page.enter_email(valid_data["email"])
            self.signup_page.enter_phone_number(valid_data["phone_number"])
            self.signup_page.enter_password(valid_data["password"])
            self.signup_page.enter_confirm_password(valid_data["confirm_password"])
            self.signup_page.click_next_button1()
            time.sleep(20)
            self.signup_page.enter_otp(get_otp_from_email())
            self.signup_page.click_verify_code_button()
        
        with allure.step("Filling out Agency Details"):
            self.signup_page.enter_agency_name(valid_data["agency_name"])
            self.signup_page.enter_role_in_agency(valid_data["role_in_agency"])
            self.signup_page.enter_agency_email(valid_data["agency_email"])
            self.signup_page.enter_agency_website(valid_data["agency_website"])
            self.signup_page.enter_agency_address(valid_data["agency_address"])
            self.signup_page.select_region_of_operation()
            self.signup_page.click_next_button2()

        with allure.step("Filling out personal experience"):
            self.signup_page.select_experience_year()
            self.signup_page.enter_students_recruited(valid_data["students_recruited"])
            self.signup_page.enter_focus_area(valid_data["focus_area"])
            self.signup_page.enter_success_metrics(valid_data["success_metrics"])
            self.signup_page.select_services()
            self.signup_page.click_next_button3()

        with allure.step("Uploading a file and finalizing Signup"):
            self.signup_page.enter_business_registration(valid_data["business_registration"])
            self.signup_page.select_preferred_countries()
            self.signup_page.select_preferred_institution()
            time.sleep(5)
            upload_file(self.driver)
            self.signup_page.click_submit_button()

        profile_name = self.signup_page.get_element_text(self.signup_page.PROFILE_NAME) 
        assert_true(valid_data["first_name"]+" "+valid_data["last_name"] == profile_name, "Signup failed or incorrect profile name displayed", "signup", self.signup_page)

        time.sleep(5)

