from selenium.webdriver import ActionChains
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
browser = webdriver.Firefox(firefox_profile=firefox_profile)
browser.get('https://www.linkedin.com/')
browser.implicitly_wait(5)
elem = browser.find_element_by_name('session_key')
elem.clear()
elem.send_keys("") # your email id 
elem = browser.find_element_by_name('session_password')
elem.clear()
elem.send_keys("") # your password
submit = browser.find_element_by_xpath("//*[@type='submit']")
actions = ActionChains(browser)
actions.click(submit)
actions.perform() 
df=pd.read_csv("salesdata.csv")
companies=df["Company"]
companies=companies.dropna()

names=[]
websites=[]
headquarterss=[]
yearfoundeds=[]
companytypes=[]
sizes=[]
specialitys=[]
information=[]


for company in list(companies):
    print(company)
    try:
            company_s = company.lower().replace(" ", "-")
            browser.get('https://in.linkedin.com/company/' + company_s + "/")
            print('https://in.linkedin.com/company/' + company_s + "/")
            time.sleep(15) 
            soup = BeautifulSoup(browser.page_source, 'lxml')
            text = soup.text.replace("\n", "$")
            
            text = text.replace("  ", "")
            text = text.replace("$$", "$")
            string = text[text.find("Company details") + len("Company details") + 1: text.find("See more details about")]
            string = string.split("$")
            for itr in range(0, len(string)):
                try:
                    string.remove(" ")
                except:
                      pass
                try:
                    string.remove(" ")
                except:
                      pass
                try:
                    string.remove("")
                except:
                      pass
            
            dictionary = {}
            for itr in range(0, len(string) - 1, 2):
                dictionary[string[itr]] = string[itr + 1]
            data = []
            data.append(company)
            main = {
              "Website": 0,
              "Headquarters": 0,
              "Year founded": 0,
              "Company type": 0,
              "Company size": 0,
              "Specialties": 0
            }
            for key in dictionary.keys():
                if key in main:
                      main[key] = dictionary[key]
            for value in main.values():
                data.append(value)
            
            information.append(data)
    except:
        pass
    

