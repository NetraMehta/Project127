from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from selenium.webdriver.common.by import By

StartURL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
Browser = webdriver.Chrome("D:/Users/User/WebScraping/chromedriver.exe")
Browser.get(StartURL)
time.sleep(2)

def Scrape():
    headers = ["Name", "Distance", "Mass", "Radius"]
    StarData = []
    soup = BeautifulSoup(Browser.page_source, "html.parser")
    for tr_tag in soup.find_all("tr"):
        tdtags = tr_tag.find_all("td")
        temp_list = []
        for index, litag in enumerate(tdtags):
            if index==0:
                temp_list.append(tdtags.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(tdtags.contents[0])
                except:
                    temp_list.append("")
        StarData.append(temp_list)
        
    with open("Scraper2.csv", "w") as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(StarData)

Scrape()