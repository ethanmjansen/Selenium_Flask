import bs4
import requests
import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class IndeedBot():

    def __init__(self, job_title=None, city=None, state_province=None):
        self.job_title = job_title
        self.city = city 
        self.state_province = state_province

        self.driver = webdriver.Chrome('./chromedriver.exe')


    def job_search(self):
    
        self.driver.get('https://indeed.com')
        self.driver.find_element_by_name('q').send_keys(self.job_title)
        for i in range(20):
            self.driver.find_element_by_name('l').send_keys(Keys.BACK_SPACE)
        # self.driver.find_element_by_name('l').send_keys(self.city)
        self.driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button').click()
        this_url = self.driver.current_url
        page = requests.get(this_url).text
        soup = BeautifulSoup(page, 'lxml')
        print(soup)
        return soup



if __name__ =='__main__':
    iBot = IndeedBot(job_title='Web Developer')
    iBot.job_search()
