from selenium import webdriver
from getpass import getpass
import time
from selenium.webdriver.chrome.options import Options

import requests
from bs4 import BeautifulSoup

#输入账号密码及登录
username = input("Enter in your username: ")
password = getpass("Enter your password: ")

#chrome_options=Options()
#chrome_options.add_experimental_option("detach",True)

options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(chrome_options=options)
driver = webdriver.Chrome("C:\\Users\\Lenovo\\Desktop\\chromedriver.exe")
driver.maximize_window()    #浏览器最大化
driver.get("https://cas.whu.edu.cn/authserver/login?service=http://hqfwdt.whu.edu.cn/cas&deployType=private&schoolCode=10486&root=\
http%3A%2F%2Fhqfwdt.whu.edu.cn%2Flogin&failCount=0&schoolName=%E6%AD%A6%E6%B1%89%E5%A4%A7%E5%AD%A6&showQrCode=false&source=\
http%3A%2F%2Fhqfwdt.whu.edu.cn%2Fpc%3Fsid%3Dhttp%3A%2F%2Fhqfwdt.whu.edu.cn%2Frepair%2Fredirect%2Fwebsite%2Findex")
time.sleep(1)   #强制等待两秒

username_textbox = driver.find_element_by_id("username")
username_textbox.send_keys(username)
password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)
login_button = driver.find_element_by_xpath("//*[@type='submit']")  ##寻找type=submit的元素
login_button.submit()
time.sleep(1)


driver.get("http://hqfwdt.whu.edu.cn/repair/redirect/website/index")
time.sleep(1)
#search_driver = driver.current_window_handle      # 此行代码用来定位当前页面
#driver.switch_to.window(driver.window_handles[0])

repair_link=driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/a")
url=repair_link.get_attribute("href")
driver.get(url)
time.sleep(2)
driver.refresh()
time.sleep(1)


#!巨坑
#address_textbox = driver.switch_to.frame("section")
iframe=driver.find_element_by_id("section") #定位到iframe
driver.switch_to_frame(iframe)  #切换到iframe
#driver.switch_to.frame("section")
#driver.switch_to_frame("section")
time.sleep(1)
'''
repair_link=driver.find_element_by_id("myWant")
repair_link.click()
time.sleep(1)
#search_window = driver.current_window_handle
n = driver.window_handles  # 这个时候会生成一个新窗口或新标签页的句柄，代表这个窗口的模拟driver
print('当前句柄: ', n)  # 会打印所有的句柄
driver.switch_to_window(n[-1])  # driver切换至最新生产的页面
print(driver.current_window_handle)
time.sleep(1)
#driver.get("http://hqfwdt.whu.edu.cn/pc/?typeName=repair&linkUrl=\
#http://hqfwdt.whu.edu.cn/repair/redirect/publish/repairs&isShow=1")     #我要报修界面
'''

#driver.get("http://hqfwdt.whu.edu.cn/pc/?typeName=repair")
my_address = input("Enter in your address: ")
my_discription = input("Enter in your discription: ")
my_telephone = input("Enter in your telephone: ")


#address_textbox = driver.find_element_by_id("address")
address_textbox = driver.find_element_by_xpath("//input[@name='address']")
address_textbox.send_keys(my_address)
discription_textbox = driver.find_element_by_name("content")
discription_textbox.send_keys(my_discription)
telephone_textbox = driver.find_element_by_name("userMobile")
telephone_textbox.send_keys(my_telephone)



#driver.refresh()   #刷新界面
time.sleep(5)
driver.quit()



