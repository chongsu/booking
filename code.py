# -- coding utf-8 --
from splinter.browser import Browser
from splinter.exceptions import ElementDoesNotExist
from selenium.webdriver.support.ui import Select
from time import sleep
import time
import multiprocessing as mp
from multiprocessing import Process


USR='@link.cuhk.edu.hk'
PASSWD=''
DATE= '7/11/2021'


TARGET = ['/html/body/div[2]/div/div[3]/div/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[6]/div/div[2]/a[111]',
          '/html/body/div[2]/div/div[3]/div/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[6]/div/div[2]/a[1]',
          '/html/body/div[2]/div/div[3]/div/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[6]/div/div[2]/a[1]',
          '/html/body/div[2]/div/div[3]/div/div/div/div[2]/div[2]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[6]/div/div[2]/a[1]'
          ]

class Dog:
    # this method open browser and login
    def __init__(self, username, passwd, date):
        self.webbrowser = 'firefox'
        self.ticket_url = "https://booking.peu.cuhk.edu.hk/peu_booking/Home/SelectRole/"
        
        # username and password
        self.username = username
        self.passwd = passwd
        
        # date
        self. date = date
        
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

        

    # wait until 00:00 Monday and then try designated time slot
    def start(self, timeslot):
        # wait until monday
        # while time.localtime().tm_wday > 0:
        #    sleep(0.5)
        success = False
        counter = 1
        while success == False:
            try:
                # preview
                if counter > 5:
                    success = True
                    print ('this time slot is full: ', timeslot)
                counter = counter + 1
                self.browser.find_by_xpath('/html/body/div[2]/div/div[3]/div/div/div/div[2]/form/div[3]/div[2]/button').click()
                # choose a time slot
                self.browser.find_by_xpath(timeslot).click()
                # confirm booking
                self.browser.find_by_xpath('/html/body/div[2]/div/div[3]/div/div/div/div[2]/form/div[18]/div/button[2]').click()
                success = True
                print("Congratulations! Your booking is confirmed.")
            except ElementDoesNotExist:
                print ('this time slot is full')

def function(i):
    dog = Dog(USR, PASSWD, DATE)
    dog.start(TARGET[i-1])

if __name__ == '__main__':
    print("Use multiprocessing.")
    pool = []
    size = len(TARGET)
    for pid in range(size):
        pool.append(Process(target=function, args=(pid+1,)))
        
    for pid in range(size):
        pool[pid].start()
        print("Process ", pid+1, ": Started!")
    
    for pid in range(size):
        pool[pid].join()
    print("Process: Done!")
