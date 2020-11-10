#This scraps emploitic jobs
#Voyons voir
import requests
import time
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By 
#from test cases
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

class emploi():
    def __init__(self, wdriver):
        self.browser = webdriver.Chrome(wdriver)
        self.browser

    def main(self, job):
        self.fetch_get(job)
        
        

    def fetch_get(self,job):
        jo = job
        if ' ' in job : jo = self.space_formatting(job)
        self.browser.get('https://www.emploitic.com/offres-d-emploi?t[0]=location-6&q='+ jo)
        a = self.browser.page_source

        if("désolés" in a): 
            print("No jobs")
        else:
            elem = self.browser.find_elements_by_tag_name("h2")
            if elem[1].text == "Dernières offres d'emploi":
                elem.pop(0)
                elem.pop(0)
            else:
                elem.pop(0)
                
            jobs = [] #To return
            with open('list.txt',"w",encoding="utf-8") as f:
                for l in elem:
                    jobs.append(l.text)
                    f.write(l.text+"\n")
                    print(l.text)
            return jobs
        
        ##p =  self.soup.find_all("a", attrs={"class":"UnderlineNav-item"})
        #elements = WebDriverWait(self.browser, 5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, ".spaced-bot alert-container ")))
        #elem = self.browser.find_element_by_class_name('sirius com_finder view-jobs no-layout no-task itemid-110')


    def space_formatting(self,job):
        jo = ""
        for i in range(0,len(job)):
            if (job[i] == " "):
                jo += "%20"
            else:
                jo += job[i] 
        return jo

webdri = 'C:\\Users\\pc1\\Downloads\\chromedriver_win32\\chromedriver'
a = emploi(webdri)
a.main("python")