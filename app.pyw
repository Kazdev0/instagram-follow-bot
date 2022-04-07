from selenium import webdriver
import time

usernamef = open("username.txt", "r")
passwordf = open("password.txt", "r")
u = usernamef.read()
p = passwordf.read()
browser = webdriver.Chrome("D:\chromedriver")
browser.get("https://instagram.com")
time.sleep(7)

giris_yap = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
giris_yap.click()
username  = browser.find_element_by_name("username")
username.send_keys(u)

time.sleep(2)
# //*[@id="loginForm"]/div/div[2]/div/label/input

password_yap = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password = browser.find_element_by_name("password")
password.send_keys(p)

time.sleep(3)

buton = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
buton.click()

time.sleep(3)

button = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
button.click()

time.sleep(4)
bildirim = browser.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')

bildirim.click()

time.sleep(7)
arama_cubugu = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
arama_cubugu.send_keys("ibrahmofficial07")
time.sleep(2)
user = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a')
user.click()

time.sleep(10)

follow = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/button')
follow.click()