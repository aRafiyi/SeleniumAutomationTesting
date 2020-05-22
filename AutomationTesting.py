"""
Automation Testing - Selenium IDE
Created on April 16 2020
@author: ALIREZA RAFIYI
"""
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_PROG8440_AutomationTesting_ASSIGN04(unittest.TestCase):        
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\elbab\Downloads\chromedriver.exe")    
        self.driver.implicitly_wait(10) 
        self.verificationErrors = []     
        self.accept_next_alert = True  
  
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_checkTitle(self):
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748)
        assert self.driver.title == "PROG8440 - Software Quality"
        driver.quit()

    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_checkHeading1(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748)      
        self.driver.find_element(By.CSS_SELECTOR, "h1").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h1").text == "PROG8440 - Software Quality"
        driver.quit()
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_checkHeading2(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "h2").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h2").text == "Assignment #4"
        driver.quit()

    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04__checkHeading3(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "h3").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "h3").text == "Due: April 16th, 2020"
        driver.quit()        

    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04__checkTextParagraph(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(4)").text == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc tristique sapien dolor, eu placerat felis pellentesque vel. Nam in commodo ligula. In hac habitasse platea dictumst. Sed pulvinar risus eu elit auctor, et elementum urna eleifend. Nulla id quam ullamcorper, laoreet leo eu, tempor metus. Maecenas scelerisque ligula erat, sed pulvinar justo mattis sed. Proin vitae tortor vitae ex finibus iaculis. Duis nec quam eros. Curabitur ornare ligula eu augue ultricies, sit amet pellentesque elit ullamcorper."
        driver.quit()        

    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_checkImagePresentPart1(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        elements = self.driver.find_elements(By.CSS_SELECTOR, "img")
        assert len(elements) > 0
        driver.quit()        
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN0_checkImagePresentPart2(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        elements = self.driver.find_elements(By.CSS_SELECTOR, "img")
        assert len(elements) > 0
        driver.quit()        
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_checkRadioButtonSelectionMenu(self):      
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(17)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(17)").text == "Select a radio button and click on Submit."
        driver.quit()        

    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_checkFavouriteColourMenuRedBlueYellow(self):
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(18)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(18)").text == "What is your favourite colour?: Red Blue Yellow"
        driver.quit()               

    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_ckeckSelectedColorRed(self):       
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        self.driver.find_element(By.NAME, "colour").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(20)").click()
        self.driver.find_element(By.ID, "result").click()
        assert self.driver.find_element(By.ID, "result").text == "The colour you selected was: Red"
        driver.quit()
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04__ckeckSelectedColorBlue(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(20)").click()
        self.driver.find_element(By.ID, "result").click()
        assert self.driver.find_element(By.ID, "result").text == "The colour you selected was: Blue"
        driver.quit()
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_ckeckSelectedColorYellow(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(20)").click()
        self.driver.find_element(By.ID, "result").click()
        assert self.driver.find_element(By.ID, "result").text == "The colour you selected was: Yellow"
        driver.quit()        

    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_ckeckFavouriteCarMenu(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(17)").click()
        self.driver.find_element(By.ID, "strUser").click()
        assert self.driver.find_element(By.ID, "strUser").text == "Select your favourite car"
        driver.quit()        
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_ckeckFavouriteCarMenuVolvo(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(16)").click()
        self.driver.find_element(By.ID, "strUser").click()
        assert self.driver.find_element(By.ID, "strUser").text == "The car you selected was: Volvo"
        driver.quit()        
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_ckeckFavouriteCarMenuSaab(self):
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.ID, "cars").click()
        dropdown = self.driver.find_element(By.ID, "cars")
        dropdown.find_element(By.XPATH, "//option[. = 'Saab']").click()
        self.driver.find_element(By.ID, "cars").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(16)").click()
        self.driver.find_element(By.ID, "strUser").click()
        assert self.driver.find_element(By.ID, "strUser").text == "The car you selected was: Saab"
        driver.quit()        
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_ckeckFavouriteCarMenuFiat(self):             
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.ID, "cars").click()
        dropdown = self.driver.find_element(By.ID, "cars")
        dropdown.find_element(By.XPATH, "//option[. = 'Fiat']").click()
        self.driver.find_element(By.ID, "cars").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(16)").click()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        assert self.driver.find_element(By.ID, "strUser").text == "The car you selected was: Fiat"
        driver.quit()        
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_ckeckFavouriteCarMenuAudi(self):
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.ID, "cars").click()
        dropdown = self.driver.find_element(By.ID, "cars")
        dropdown.find_element(By.XPATH, "//option[. = 'Audi']").click()
        self.driver.find_element(By.ID, "cars").click()
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(16)").click()
        self.driver.find_element(By.ID, "strUser").click()
        assert self.driver.find_element(By.ID, "strUser").text == "The car you selected was: Audi"
        driver.quit()        
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_ckeckListElementsCantaloupes(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(3)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(3)").text == "Cantaloupes"
        driver.quit()        

    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_ckeckListElementsBananas(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(2)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(2)").text == "Bananas"
        driver.quit()        
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_ckeckListElementsApples(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(1)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "ol > li:nth-child(1)").text == "Apples"
        driver.quit()        
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_ckeckListElementsMilk(self):
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(3)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(3)").text == "Milk"
        driver.quit()        

    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_ckeckListElementsTea(self): 
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(2)").text == "Tea"
        driver.quit()        

    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04ckeckListElementsCoffee(self):
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(1)").click()
        assert self.driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(1)").text == "Coffee"
        driver.quit()
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04_checkHyperlinkToConestogaCollege(self):        
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        self.driver.find_element(By.CSS_SELECTOR, "body").click()
        assert self.driver.find_element(By.LINK_TEXT, "This is a link to Conestoga College").text == "This is a link to Conestoga College"
        driver.quit()
        
    def test_PROG8440_AUTOMATIONTESTING_ASSIGN04(self):       
        driver = self.driver      
        self.driver.get("http://localhost/PROG8440Assignment4.html")
        self.driver.set_window_size(1050, 748) 
        self.driver.find_element(By.CSS_SELECTOR, "ul > li:nth-child(3)").click()
        self.driver.find_element(By.LINK_TEXT, "This is a link to Conestoga College").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, "#logoblock img")
        assert len(elements) > 0
        self.driver.close()
        driver.quit()  


if __name__ == '__main__':    
   unittest.main()
