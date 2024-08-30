from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os

base_url = "https://web.whatsapp.com/"

my_numbers = [
    "+9647727341795",
    "+9647727341795",
    "+9647727341795",
    "+9647727341795",
    "+9647727341795",
    "+9647727341795",
    "+9647727341795",
]

op = Options()
op.add_argument(argument=r'user-data-dir=login/')

def send_my_text(driver, phone, msg):
    wassup_url = rf'{base_url}send?phone={phone}&text&app_absent=0'
    driver.get(wassup_url)
    time.sleep(5)
    chatbox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    chatbox.send_keys(msg)
    chatbox.send_keys(Keys.RETURN)
    time.sleep(2)


def send_my_image(driver, phone, path):
    wassup_url = rf'{base_url}send?phone={phone}&text&app_absent=0'
    driver.get(wassup_url)
    print(f'sending to {phone} .....')
    time.sleep(5)
    driver.find_element(By.XPATH,
                        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/div/div/span').click()
    file = driver.find_element(By.XPATH,
                               '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[1]/div[2]/div/span/div/ul/div/div[2]/li/div/input')
    filename = os.path.realpath(path)
    file.send_keys(filename)
    time.sleep(0.1)
    driver.find_element(By.XPATH,
                        '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div').click()
    time.sleep(2)


# send_my_text(driver=driver,phone=phone,msg="hi 😋")

def friday():
    driver = webdriver.Chrome(options=op)
    for i in my_numbers:
        send_my_image(driver=driver, phone=i, path='Images/friday.jpg')


ch = "-1"
while ch != "0":

    ch = input("Please Choose:\n1) login:\n2) send image:\n0) exit:\nChoose:")

    if ch == "1":

        driver = webdriver.Chrome(options=op)
        driver.get(base_url)
        time.sleep(25)

    elif ch == "2":

        friday()

    elif ch == "0":
        break
