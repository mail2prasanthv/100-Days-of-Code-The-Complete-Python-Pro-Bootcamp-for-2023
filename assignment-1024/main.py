# get internet speed info
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
   
# create webdriver object
driver = webdriver.Chrome()

driver.get("https://www.speedtest.net/")
driver.maximize_window()

try:
    go_botton_xpath = "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a"
    ip_xpath = "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[1]/div[3]/div[3]"
    isp_xpath ="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[1]/div[3]/div[2]"
    download_speed_xpath ="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span"
    upload_speed_xpath ="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span"
    ping_xpath = "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[2]/span"
    download_latency_xpath = "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[3]/span"
    upload_latency_xpath="//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[2]/div/span[4]/span"
    finished_msg_xpath = "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[2]/div/div/h3"
    
    element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, go_botton_xpath)))
    element.click()
    
    element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, finished_msg_xpath)))
    
    isp = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, isp_xpath)))
    ip = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, ip_xpath)))
    download_speed = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, download_speed_xpath)))
    upload_speed = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, upload_speed_xpath)))
    download_latency = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, download_latency_xpath)))
    upload_latency = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, upload_latency_xpath)))

    print("isp:",isp.text)
    print("ip:",ip.text)
    print("download_speed:",download_speed.text)
    print("upload_speed:",upload_speed.text)
    print("download_latency:",download_latency.text)
    print("upload_latency:",upload_latency.text)


    
except NoSuchElementException:
    print('No element of that id present!')
