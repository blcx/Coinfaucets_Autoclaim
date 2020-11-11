from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import json
import undetected_chromedriver as uc
import telegram


with open('TelegramBot.json', 'r') as file:
    botinfo = json.load(file)
    file.close()

token = botinfo['TOKEN']
id = botinfo['CHATID']
bot = telegram.Bot(token=token)

counter = 0
global claim

def visit_site_xrp():
    print("Visiting site xrp")
    bot.send_message(chat_id=id, text="Visiting XRP site")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userXRP']
    password = login['passXRP']

    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)

    try:
        driver.get("https://coinfaucet.io/free")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")
        time.sleep(5)

        #send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(2)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)
        time.sleep(10)
        driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        time.sleep(5)
        try:
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
            print("roll success clicked after login")
            time.sleep(5)
            # send msg to telegram bot
            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            bot.send_message(chat_id=id, text=element.text)

            claim += 1
            time.sleep(2)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            bot.send_message(chat_id=id, text="Already Claimed")
            time.sleep(2)
            driver.quit()
    print("Visited site XRP successfully")


def visit_site_cardano():
    print("Visiting site cardano")
    bot.send_message(chat_id=id, text="Visiting site Cardano")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userADA']
    password = login['passADA']
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://freecardano.com/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")

        time.sleep(2)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)
        time.sleep(10)
        driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        time.sleep(5)
        try:
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
            print("roll success clicked after login")

            claim += 1
            time.sleep(2)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            bot.send_message(chat_id=id, text="Already Claimed")
            time.sleep(2)
            driver.quit()
    print("Visited site Cardano successfully")


def visit_site_tron():
    print("Visiting site Tron")
    bot.send_message(chat_id=id, text="Visiting site Tron")

    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userTRON']
    password = login['passTRON']
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://free-tron.com/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")
        time.sleep(5)

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(5)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)
        time.sleep(10)
        driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        time.sleep(5)
        try:
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
            print("roll success clicked after login")

            time.sleep(5)

            # send msg to telegram bot
            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            bot.send_message(chat_id=id, text=element.text)

            claim += 1
            time.sleep(5)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            bot.send_message(chat_id=id, text="Already Claimed")
            time.sleep(5)
            driver.quit()
    print("Visited site Tron successfully")


def visit_site_dash():
    print("Visiting site Dash")
    bot.send_message(chat_id=id, text="Visiting site Dash")

    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userDASH']
    password = login['passDASH']
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://freedash.io/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")

        time.sleep(5)

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(5)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)
        time.sleep(10)
        driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        time.sleep(5)
        try:
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
            print("roll success clicked after login")

            time.sleep(5)

            # send msg to telegram bot
            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            bot.send_message(chat_id=id, text=element.text)

            claim += 1
            time.sleep(5)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            bot.send_message(chat_id=id, text="Already Claimed")
            time.sleep(5)
            driver.quit()
    print("Visited site Dash successfully")



def visit_site_eth():
    print("Visiting site ETH")
    bot.send_message(chat_id=id, text="Visiting site ETH")

    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userETH']
    password = login['passETH']
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://freeethereum.com/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")

        time.sleep(5)

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(5)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)
        time.sleep(10)
        driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        time.sleep(5)
        try:
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
            print("roll success clicked after login")

            time.sleep(5)

            # send msg to telegram bot
            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            bot.send_message(chat_id=id, text=element.text)

            claim += 1
            time.sleep(5)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            bot.send_message(chat_id=id, text="Already Claimed")
            time.sleep(5)
            driver.quit()
    print("Visited site ETH successfully")



def visit_site_nem():
    print("Visiting site nem")
    bot.send_message(chat_id=id, text="Visiting site NEM")

    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userNEM']
    password = login['passNEM']
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://freenem.com/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")

        time.sleep(5)

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(5)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)
        time.sleep(10)
        driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        time.sleep(5)
        try:
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
            print("roll success clicked after login")

            time.sleep(5)

            # send msg to telegram bot
            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            bot.send_message(chat_id=id, text=element.text)

            claim += 1
            time.sleep(5)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            bot.send_message(chat_id=id, text="Already Claimed")
            time.sleep(5)
            driver.quit()
    print("Visited site NEM successfully")



def visit_site_neo():
    print("Visiting site neo")
    bot.send_message(chat_id=id, text="Visiting site NEO")
    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userNEO']
    password = login['passNEO']
    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://freeneo.io/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")

        time.sleep(5)

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(5)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)
        time.sleep(10)
        driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        time.sleep(5)
        try:
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
            print("roll success clicked after login")

            time.sleep(5)

            # send msg to telegram bot
            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            bot.send_message(chat_id=id, text=element.text)

            claim += 1
            time.sleep(5)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            bot.send_message(chat_id=id, text="Already Claimed")
            time.sleep(5)
            driver.quit()
    print("Visited site NEO successfully")



def visit_site_link():
    print("Visiting site link")
    bot.send_message(chat_id=id, text="Visiting site LINK")

    with open('Login.json', 'r') as file:
        login = json.load(file)
        file.close()

    username = login['userLINK']
    password = login['passLINK']

    #driver = webdriver.Chrome(PATH)
    driver = uc.Chrome()
    driver.set_page_load_timeout(120)
    try:
        driver.get("https://freechain.link/")
    except TimeoutException as e:
        print(e.msg)
        print("Page load Timeout Occured. Quiting !!!")
        driver.quit()

    try:
        time.sleep(10)
        # click roll button if it is present
        driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
        print("roll was successful on page load")

        time.sleep(5)

        # send msg to telegram bot
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
        bot.send_message(chat_id=id, text=element.text)

        time.sleep(5)
        driver.quit()

    except:
        # if roll button not present try to login
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        element.send_keys(username)
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "password")))
        element.send_keys(password)
        time.sleep(10)
        driver.find_element_by_xpath("//button[contains(text(),'LOGIN!')]").click()
        time.sleep(5)
        try:
            time.sleep(5)
            driver.find_element_by_xpath("/html/body/main/div/div/div/div/div/div[5]/button").click()
            print("roll success clicked after login")

            time.sleep(5)

            # send msg to telegram bot
            element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "result")))
            bot.send_message(chat_id=id, text=element.text)

            claim += 1
            time.sleep(5)
            driver.quit()

        except:
            print("already clicked wait more minutes")
            bot.send_message(chat_id=id, text="Already Claimed")
            time.sleep(5)
            driver.quit()
    print("Visited site LINK successfully")



while True:
   visit_site_xrp()
   time.sleep(5)
   visit_site_cardano()
   time.sleep(5)
   visit_site_tron()
   time.sleep(5)
   visit_site_dash()
   time.sleep(5)
   visit_site_eth()
   time.sleep(5)
   visit_site_nem()
   time.sleep(5)
   visit_site_neo()
   time.sleep(5)
   visit_site_link()
   time.sleep(5)

   bot.send_message(chat_id=id, text="Waiting About an Hour...")
   print("waiting about an hour")
   time.sleep(3600) #seconds to hour
   counter += 1
   bot.send_message(chat_id=id, text="wait finished " + "Run Times: " + str(counter))
   print("Wait Finished " + "Run Times: " + str(counter))





