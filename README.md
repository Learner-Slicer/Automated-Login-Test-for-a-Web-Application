# Task 3 – Login Page Testing (Manual + Automated)

## Overview:

This project was created as part of my internship assignment for **Prodigy InfoTech**. The goal of Task 3 was to:

> **Write a test suite using any library of choice that automates login functionality testing on a website.**  
> It should include both **positive test cases** (valid credentials) and **negative test cases** (invalid or empty inputs).

Instead of using an existing website, I decided to **create my own simple login page**, like how a student might build one using HTML and CSS. Then I used **Selenium with Python** to write a test script that checks if login works properly — but it lets the user enter the login manually, instead of filling it automatically.

Once the correct credentials are entered, the page redirects to [Flipkart.com](https://www.flipkart.com), just to simulate what a real login might do.

> As a visual reference, I looked at [https://www.saucedemo.com](https://www.saucedemo.com), but I did **not use any code** or content from it.

---

## Features:

- A basic login page with medium-sized input fields
- Username and password boxes are centered on the screen
- A green login button placed below the inputs
- A blue box below the form that shows sample usernames and the correct password (so users know what to type)
- Redirection to Flipkart.com when login is successful
- A test script that waits for the user to log in manually, then checks if the redirection was successful

---

## How to Use:

1. Clone or download this repository
2. Make sure you have the following installed:
   - Python
   - Selenium (`pip install selenium`)
   - Microsoft Edge WebDriver set up correctly
3. Open the terminal inside the project folder
4. Run the test script:
python student_login_test.py
5. When the browser opens, enter one of the valid usernames and the password shown on the page
6. Click the green login button
7. If login is successful, the script checks if you were redirected to Flipkart

## Folder Structure:
Prodigy-Task3-Login-Test/
├── login.html              → The login page I built
├── success.html            → Redirects to Flipkart after login
├── student_login_test.py   → Python script that tests login (manual input)
└── README.md               → This file

## Valid Credentials:
These are shown on the page itself too, but here they are again:

# Username  # Password
student101  pass123
learner02  pass123
testuser03  pass123
guest04  pass123
demo05  pass123
trial06  pass123

## Testing Strategy:
The test is mostly manual, but still automated in terms of checking the outcome.

## Positive Test Case:
Enter a valid username and password → should redirect to Flipkart

## Negative Test Cases:
Leave both fields empty → nothing should happen
Enter a wrong username or password → no redirection
Only fill one field → login should not succeed
The script uses Selenium to wait for the user and checks if the page changed to Flipkart after login. If not, it considers the login unsuccessful.

## Manual Test Case Format:
For all the test cases, I followed this format:
Test Case ID
Description
Preconditions
Test Steps
Expected Result
I tested all of these by opening the HTML file and using the browser directly.

## Browser Used:
Microsoft Edge (with Edge WebDriver)

## Author:
# Rathun Rajeevan
BCA Student – Jain (Deemed-to-be) University
Software Testing Intern – Prodigy InfoTech

## Acknowledgements:
This project was done as part of the Prodigy InfoTech Software Testing Internship.
Thanks to the team for providing tasks that helped me improve both my testing and development skills in a practical way.

## Reference:
The login layout idea was based on common login UIs and inspired by saucedemo.com — but everything was built manually from scratch using basic HTML and CSS.
