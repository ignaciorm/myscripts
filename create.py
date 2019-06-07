import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("Python runing")

path = r'C:\Users\ignac_000\proyects/'
browser = webdriver.Firefox(executable_path=r'C:\Users\ignac_000\proyects\scripts\geckodriver.exe');
browser.get('https://github.com/login')

def navtype(where, what):
    element = browser.find_element_by_xpath(where)
    element.send_keys(what)

def navclick(where):
    element = browser.find_element_by_xpath(where)
    element.click()

def create():
    proyectname = "this is only a test"
    os.makedirs(path + proyectname)
    print('Folder created')
    open(path + proyectname + '/README.txt' , 'w+').close()
    print('README created')
    navtype("//input[@id='login_field']",'jirm2062@gmail.com')
    navtype("//input[@id='password']",'Cooligna77')
    navclick("//input[@name='commit']")
    browser.get('https://github.com/new')
    navtype("//*[@id='repository_name']",proyectname)
    element = browser.find_element_by_xpath("//*[@id='new_repository']/div[3]/button")
    element.submit()

    browser.quit()

if __name__ == '__main__':
    create()


#open(r'C:\Users\ignac_000\proyects/README.txt','w+')
