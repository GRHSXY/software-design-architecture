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

#login_button = driver.find_element_by_id("Sign in")
login_button = driver.find_element_by_xpath("//*[@type='submit']")  ##寻找type=submit的元素
login_button.submit()

time.sleep(1)

#登录之后获取信息
driver.get("http://hqfwdt.whu.edu.cn/pc/?typeName=repair&linkUrl=\
http://hqfwdt.whu.edu.cn/repair/redirect/publish/repairs&isShow=1")     #我要报修界面

hands = driver.window_handles  # 获取所有的句柄
driver.switch_to.window(hands[-1])  # 直接获取hands这个list数据里面最后1个hand的值,切换到最后一个窗口

time.sleep(1)

address = input("Enter in your address: ")
discription = input("Enter in your discription: ")
telephone = input("Enter in your telephone: ")

address_textbox = driver.find_element_by_id("address")
address_textbox.send_keys(address)
discription_textbox = driver.find_element_by_name("content")
discription_textbox.send_keys(discription)
telephone_textbox = driver.find_element_by_name("userMobile")
telephone_textbox.send_keys(telephone)

'''
a_url = 'http://hqfwdt.whu.edu.cn/pc/?typeName=repair&linkUrl=http://hqfwdt.whu.edu.cn/repair/redirect/publish/repairs&isShow=1'
html = requests.get(a_url)
pagesource = html.text
print(pagesource)
'''

#driver.refresh()   #刷新界面
time.sleep(5)
driver.quit()
'''

#driver.get("http://hqfwdt.whu.edu.cn/repairredirect/website/index")

time.sleep(3)

driver.get("http://hqfwdt.whu.edu.cn/pc/?typeName=repair&linkUrl=\
http://hqfwdt.whu.edu.cn/repair/redirect/publish/repairs&isShow=1")  #我要报修界面
#print("获取当前URL：", driver.current_url)  # 获取当前URL
#print("获取当前页面title：", driver.title)  # 获取当前页面title
'''