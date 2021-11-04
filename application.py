from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


chrome = webdriver.Chrome()
time.sleep(1)
chrome.get("https://www.invertexto.com/gerador-email-temporario")
time.sleep(1)
tentativas = 1000000
tentativa = 0

while tentativa < tentativas:
    tentativa = tentativa + 1
    print("Voto de número: ", tentativa, " realizado")
    chrome.get("https://www.invertexto.com/gerador-email-temporario")
    getEmail = chrome.find_element_by_xpath("//*[@id='email-input']").get_attribute("value")
    print(getEmail)


'''while tentativa < tentativas:
    tentativa = tentativa + 1
    print("Voto de número: ", tentativa, " realizado")
    selectTaina = chrome.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div/div/div/div[2]/div/div/span/div/div[9]/label/div/div[1]").click()
    time.sleep(0.5)
    btnEnviar = chrome.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[3]/div/div[1]/div").click()
    time.sleep(0.5)
    btnVotarNovamente = chrome.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div[4]/a").click()
    time.sleep(0.5)'''