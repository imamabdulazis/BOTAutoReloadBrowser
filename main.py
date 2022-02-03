from selenium import webdriver
import time
from urllib.request import urlopen
    
x = input("URL without http or https :")
try:
    refreshrate = input('Reload time :')
    refreshrate = int(refreshrate)
    driver = webdriver.Firefox(executable_path='/Users/imun/Downloads/geckodriver')
    driver.get("https://"+x)
except ValueError:
    print(ValueError)

while True:
    time.sleep(refreshrate)
    driver.refresh()
