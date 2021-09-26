from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import random

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options, executable_path=r"chromedriver.exe")
actions = ActionChains(driver)
actions2 = ActionChains(driver)
actions3 = ActionChains(driver)

tunnel = "https://www.tunnelbear.com/account/login"
yopmail = "https://yopmail.com/en"

driver.get(tunnel)

driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/section/div/div/div/div/div/div[3]/p/button").click()

email = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789") + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789") + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789") + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789") + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789") + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789") + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789") + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789") + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789") + "@cool.fr.nf"
password = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!@#$%^&*()_+") + random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!@#$%^&*()_+") +random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!@#$%^&*()_+") +random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!@#$%^&*()_+") +random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!@#$%^&*()_+") +random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!@#$%^&*()_+") +random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!@#$%^&*()_+") +random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!@#$%^&*()_+") +random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!@#$%^&*()_+") +random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!@#$%^&*()_+") +random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!@#$%^&*()_+") +random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!@#$%^&*()_+") +random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ13456789!@#$%^&*()_+")

driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/section/div/div/div/div/div/div[2]/div/form/div[1]/div[2]/input").click() 
driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/section/div/div/div/div/div/div[2]/div/form/div[1]/div[2]/input").send_keys(email)

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div/div/div[2]/div/form/div[2]/div[2]/input").click() 
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div/div/div[2]/div/form/div[2]/div[2]/input').send_keys(password)

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div/div/div[2]/div/form/button/span").click()

created = f"""
╔═╗╔═╗╔═╗╔═╗╦ ╦╔╗╔╔╦╗  ╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗╔╦╗
╠═╣║  ║  ║ ║║ ║║║║ ║   ║  ╠╦╝║╣ ╠═╣ ║ ║╣  ║║
╩ ╩╚═╝╚═╝╚═╝╚═╝╝╚╝ ╩   ╚═╝╩╚═╚═╝╩ ╩ ╩ ╚═╝═╩╝\n
"""

email1 = email.split(':')[0]

driver.get(yopmail)

driver.find_element_by_xpath("/html/body/div/div[2]/main/div[3]/div/div[1]/div[2]/div/div/form/div/div[1]/div[2]/div/input").click()
driver.find_element_by_xpath("/html/body/div/div[2]/main/div[3]/div/div[1]/div[2]/div/div/form/div/div[1]/div[2]/div/input").send_keys(email1)
driver.find_element_by_xpath("/html/body/div/div[2]/main/div[3]/div/div[1]/div[2]/div/div/form/div/div[1]/div[4]/button/i").click()

os.system("cls")
print(created)
print(f"{email}:{password}\n")

print("Refresh Until You See The Verification Email :)")

# https://github.com/Greycefulz
