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

def create():
    proyectname = str(sys.argv[1])
    os.makedirs(path + proyectname)
    print('Folder created')
    open(path + proyectname + '/README.txt' , 'w+').close()
    print('README created')
    element = browser.find_element_by_xpath("//input[@id='login_field']")
    element.send_keys('jirm2062@gmail.com')
    element = browser.find_element_by_xpath("//input[@id='password']")
    element.send_keys('Cooligna77')
    element = browser.find_element_by_xpath("//input[@name='commit']")
    element.click()
    browser.get('https://github.com/new')
    element = browser.find_element_by_xpath("//*[@id='repository_name']")
    element.send_keys(proyectname)
    element = browser.find_element_by_xpath("//*[@id='new_repository']/div[3]/button")
    element.submit()

    browser.quit()

if __name__ == '__main__':
    create()


#open(r'C:\Users\ignac_000\proyects/README.txt','w+')
