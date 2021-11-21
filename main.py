from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import sys
from time import sleep
from art import *
from getpass import getpass
from selenium.webdriver.firefox.options import Options

def clear():
    os.system('cls')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def error():
    print(bcolors.OKBLUE + '[' + bcolors.FAIL+ 'X' + bcolors.OKBLUE + '] ERROR! - Trying again')

def pause():
    os.system('pause')

def banner():
    print(bcolors.OKCYAN + ' ')
    tprint('InstaSpammer')
    tprint('Pro')
    print(' To Spam DM someone that you follow')
    print(' ')
    print(bcolors.ENDC + 'by - ' + bcolors.OKGREEN + 'Kolhax' + bcolors.ENDC + ' ')
    print(' ')

clear()
os.system('title InstaSpammer Pro')

print('You need to be following / accepted to send dm\'s with this tool')
pause()
clear()

banner()



print(' ')

name = input('Your Instagram name/email: ')
passw = getpass('Your Instagram Password: ')
victim = input('Your Victim Instagram name (Without \'@\') : ')
message = input('Message to spam: ')
ammount = int(input('ammount of messages: '))
cooldown1 = int(input('cooldowns between each messages in secconds: '))

clear()

os.system('title InstaSpammer Pro - Sent: 0')

banner()

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

#driver.minimize_window()

driver.get('https://www.instagram.com/')

while True:
    try:
        driver.find_element(By.NAME, 'username').send_keys(name)
        break
    except:
        error()
        sleep(1)
        continue

while True:
    try:
        driver.find_element(By.NAME, 'password').send_keys(passw)
        break
    except:
        error()
        sleep(1)
        continue

while True:
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()
        break
    except:
        error()
        sleep(1)
        continue

sleep(7)

driver.get('https://www.instagram.com/' + victim + '/')

while True:
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button').click()
        break
    except:
        error()
        sleep(1)
        continue

count1 = 0

sleep(5)

try:
    driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]').click()
except:
    pass

while ammount > count1:
    sleep(cooldown1)
    while True:
        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message)
            break
        except:
            error()
            sleep(1)
            continue

    while True:
        try:
            driver.find_element(By.XPATH, '/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
            break
        except:
            error()
            sleep(1)
            continue    
    count1 = count1 + 1
    print(bcolors.OKCYAN + '[' + bcolors.OKGREEN + '+' + bcolors.OKCYAN + '] Message Sent Succefully')
    os.system('title InstaSpammer Pro - Sent: ' + str(count1))

driver.quit()
pause()