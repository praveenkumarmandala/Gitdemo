from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_link_text("Shop").click()
items_list = driver.find_elements_by_xpath("//div[@class='card h-100']")
for item in items_list:
    item_name = item.find_element_by_xpath("div/h4/a").text
    if item_name == "Blackberry":
        item.find_element_by_xpath("div/button").click()
check1 = driver.find_element_by_xpath("//a[contains(text(),'Blackberry')]").text      #in 1st page
driver.find_element_by_xpath("//div[@class='collapse navbar-collapse']/ul/li/a").click()
check2 = driver.find_element_by_xpath("//div[@class='media-body']/h4/a").text      #in 2nd page
print(check1)
print(check2)
assert check1 == check2
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_xpath("//a[contains(text(),'India')]").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("input[class='btn btn-success btn-lg']").click()
print(driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text)
success_text = (driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text)
assert "Success! Thank you! " in success_text
driver.get_screenshot_as_file("screen.png")