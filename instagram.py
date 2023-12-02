#Task -22-https://www.instagram.com/guviofficial/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class Insta:

    #Constructor parameter
    def __init__(self, url):
        self.url = url
        #Install latest webdriver manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        try: 
            self.driver.get(self.url)
            sleep(5)
            #Number of followers        
            followers = self.driver.find_element(By.XPATH, '//span[text()="114K"]').text
            print("Followers:", followers)
            #Number of follows
            follows = self.driver.find_element(By.XPATH, '//span[text()="4"]').text
            print("Follows:", follows)             
        except NoSuchElementException as error:
            print(error)


url = "https://www.instagram.com/guviofficial/"
i = Insta(url)
i.login()

