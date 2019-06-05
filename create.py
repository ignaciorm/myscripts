import sys
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("Python runing")

path = r'C:\Users\ignac_000\proyects/'
browser = webdriver.Firefox(executable_path=r'C:\Users\ignac_000\proyects\scripts\geckodriver.exe');
browser.get('https://github.com/login')

def create():
    foldername = str(sys.argv[1])
    os.makedirs(path + foldername)
    print(path + foldername + '---created')
    element = browser.find_element_by_xpath("//input[@id='login_field']")
    element.click()
    element.send_keys('ignacio.r.m.falcon@gmail.com')

if __name__ == '__main__':
    create()
