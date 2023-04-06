
"""THIS IS ALSO SENDING EMAILS"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pdb
# Read the Excel file into a pandas data frame
df = pd.read_csv("C:/Users/skacar/OneDrive - Indiana University/Desktop/others 2-3-23/PYTHON/VIRTUALENVS/revinv/automatic_review_inv_pro/Revlist3.csv")



# Extract the names, surnames, and email addresses from the data frame
names = df["Name"]
surnames = df["Surname"]
emails = df["Email"]

# Open the web browser and navigate to the website
driver = webdriver.Chrome()
driver.get("https://review.hindawi.com/details/e94a7a9b-f497-48c8-b333-31c2cfcf17e9/8658680b-70f5-4f2e-b9c3-6229279c29b6")
time.sleep(5)


Email_btn = driver.find_element("id", "username")
Email_btn.click()
Email_btn.send_keys(".......")

Password_btn = driver.find_element("id", "password")
Password_btn.click()
Password_btn.send_keys(".......")

login_btn = driver.find_element("id", "kc-login")
login_btn.click()
time.sleep(10)

#click on the ReviewerDetails and Reports
element = driver.find_element("xpath", "//div[@class='sc-ptDSg eYGQDi']/h3[@class='sc-fzoant httpnf']")
element.click()
time.sleep(5)

#click on the ReviewerDetails
element2 = driver.find_element("xpath", "//h3[@class='sc-fzoant dKAzxg']")
element2.click()
time.sleep(5)



for i, (name, surname, email) in enumerate(zip(names, surnames, emails)):
    # Find the form elements on the page
    name_field = driver.find_element("name", "givenNames")
    name_field.click()
    name_field.send_keys(name)

    surname_field = driver.find_element("name", "surname")
    surname_field.click()
    surname_field.send_keys(surname)

    email_field = driver.find_element("name", "email")
    email_field.click()
    email_field.send_keys(email)

    button = driver.find_element("xpath", "//button[@data-type-id='button-invite-reviewer-invite']")
    time.sleep(5)
    button.click()

    time.sleep(10)
    button = driver.find_element("xpath", "//button[@class='ant-btn ant-btn-primary']")
    button.click()
    time.sleep(5)

    # Remove the processed row from the data frame
    df = df.drop(i)
    # Save the updated data frame back to the CSV file
    df.to_csv("C:/Users/skacar/OneDrive - Indiana University/Desktop/others 2-3-23/PYTHON/VIRTUALENVS/revinv/automatic_review_inv_pro/Revlist3.csv", index=False)
    time.sleep(3)
    button = driver.find_element("xpath", "//button[@data-type-id='button-invite-reviewer-clear']")
    button.click()
    time.sleep(3)


    




time.sleep(30)

pdb.set_trace()









