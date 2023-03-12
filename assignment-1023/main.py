# get upcoming matches(web-scraping) using selenium webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
   
# create webdriver object
driver = webdriver.Chrome()

driver.get("https://www.cricbuzz.com/cricket-match/live-scores/upcoming-matches")

elements = driver.find_elements(By.CSS_SELECTOR,"a.text-hvr-underline.text-bold")
print("---------Upcoming Matches---------------")
for element in elements:
    text = element.text.strip()
    if text :
        print(text)
