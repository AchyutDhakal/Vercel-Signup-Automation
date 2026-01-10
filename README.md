# **Vercel App Signup Automation**

This project automates the signup flow of a web application using Python, Selenium WebDriver, and PyTest.
It covers user registration, OTP verification via email, multi-step form submission, and file upload.

## Tech Stack & Environment

- Programming Language: Python 3.12
- Automation Framework: Selenium WebDriver
- Test Framework: PyTest
- Browser: Google Chrome (v143 or compatible)
- OS: Windows
- For Report: Java, Scoop and Allure
- Design Pattern: Page Object Model (POM)

## Prerequisites

- Python 3.10 or above installed
- Google Chrome installed
- Git installed
- Java, Scoop and Allure installed for reports
- Virtual environment (venv)

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/AchyutDhakal/VercelAppSignupAutomation.git

   ```

2. Navigate to project directory:

   ```bash
   cd VercelAppSignupAutomation

   ```

3. Create and activate virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate

   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt

   ```

## How to Run the Tests

To execute test cases, run:

```bash
pytest -v

```

To generate report, run:

```bash
pytest --alluredir=allure-results

```

To view report, run:

```bash
allure serve allure-results
```

## Test Scenarios Covered

- User signup with valid details
- Privacy policy acceptance validation
- OTP verification via email
- Multi-step agency information form
- File upload validation
- Successful account creation flow

## Test Data & Accounts

- Test email accounts were used for OTP verification.
- Dummy data is used for user and agency details.
- OTP is fetched automatically from the test email inbox using IMAP.

## Note

If you run test more than once, make sure to change the email address after the plus to something unique on otp_reader.py which is on utils and test_data.py which is on data and also change the phone number to something unique which is on test_data.py
