# -- coding utf-8 --
from selenium import webdriver
from selenium.webdriver import ActionChains
from splinter.browser import Browser
from splinter.exceptions import ElementDoesNotExist
from selenium.webdriver.support.ui import Select
from time import sleep
import time, sys


class Dog:
    def __init__(self, username, passwd, date):
        self.webbrowser = 'firefox'
        self.ticket_url = "https://booking.peu.cuhk.edu.hk/peu_booking/Home/SelectRole/"
        
        # username and password
        self.username = username
        self.passwd = passwd
        
        # date
        self. date = '7/11/2021'
        
        # open webbrowser
        self.browser = Browser(self.webbrowser)
        self.browser.visit(self.ticket_url)

        # log in
        self.browser.fill("UserName", self.username)
        self.browser.fill("Password", self.passwd)
        self.browser.click_link_by_id('submitButton')

        # click facility booking
        self.browser.links.find_by_href('/peu_booking/Client/ClientBooking/FacilityBooking').click()

        # choose date
        self.browser.fill('PreviewDate', self.date)

        # choose BAD Badminton
        self.browser.execute_script("document.getElementsByClassName('form-control select2-hidden-accessible')[1].value = 'j2eQwFClj6jr1lYGf4sneA==';")

        

    # this method open browser and login
    def start(self, timeslot):

        # wait until monday
        while time.localtime().tm_wday > 0:
            sleep(0.1)
       
        # preview
        self.browser.find_by_xpath('/html/body/div[2]/div/div[3]/div/div/div/div[2]/form/div[3]/div[2]/button').click()
        # choose a time slot
        
        
        try:
        # print (self.browser.find_by_xpath(timeslot))
            self.browser.find_by_xpath(timeslot).click()
        except ElementDoesNotExist:
            print ('this time slot is full')

        # confirm booking
        #self.browser.find_by_xpath('/html/body/div[2]/div/div[3]/div/div/div/div[2]/form/div[18]/div/button[2]').click()

        
dog = []
dog.append(Dog('7/11/2021'))
dog.append(Dog('7/11/2021'))
dog.append(Dog('7/11/2021'))

dog[0].start('/html/body/div[2]/div/div[3]/div/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[6]/div/div[2]/a[111]')
#dog[1].start('/html/body/div[2]/div/div[3]/div/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[6]/div/div[2]/a[1]')
dog[2].start('/html/body/div[2]/div/div[3]/div/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[6]/div/div[2]/a[1]')