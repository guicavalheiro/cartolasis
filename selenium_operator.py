#WebDriver
from selenium import webdriver

#Selenium Tools
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec

#Selenium Exceptions
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException

#System
import os
import shutil
from pathlib import Path
import time

class SeleniumOperator:
    
    def __init__(self, driver):
        
        self.driver = driver
        #self.antiBan = False
    
    def search_element_by_xpath(self, xpath, lock):
        
        try:
            wait = WebDriverWait(self.driver, lock)
            element = wait.until(ec.element_to_be_clickable((By.XPATH, xpath)))
            
            if element is False:
                print("Element is false, it wasn't found on the page")
                return False
                
            else:
                return element
        
        except Exception as e:
            print(f"Search Element By Xpath - Exception: {e}\nXpath: {xpath}")
    
    def get_attribute(self, xpath, name, lock):
        
        try:
            element = self.search_element_by_xpath(xpath, lock) 
            attribute = element.get_attribute(name)
            
            return str(attribute)
        
        except Exception as e:
            print(f"Get Attribute - Exception: {e}\nXpath: {xpath}\nName: {name}")
            
    def get_text(self, xpath, lock):
        
        try:
            element = self.search_element_by_xpath(xpath, lock)
            return str(element.text)
        
        except Exception as e:
            print(f"Get Text - Exception: {e}\nXpath: {xpath}")
            
    def is_on_screen(self, xpath, lock):
        
        try:
            wait = WebDriverWait(self.driver, lock)
            element = wait.until(ec.element_to_be_clickable((By.XPATH, xpath)))
            
            if element is False:
                return False
            
            else:
                return True
        
        except Exception as e:
            print(f"Is On Screen - Exception: {e}")
            return False
                
    def my_send_keys(self, element, key, lock):                
        
        try:
            time.sleep(lock)
            element.send_keys(str(key))    
        
        except Exception as e:
            print(f"My Send Keys - Exception: {e}\nElement: {element}\nKey: {key}")
                
    def clicking_a_button(self, button, lock):
                   
        try:
            button.click()
            time.sleep(lock)
            return True
    
        except Exception as e:
            print(f"Clicking a Button - Exception: {e}\nButton: {button}")           
            
    def find_and_click(self, xpath, lock):
        
        c = 0
        while c < 5:
            
            try:
                element = self.search_element_by_xpath(xpath, lock)
                time.sleep(lock)
                click = self.clicking_a_button(element, lock)
                #time.sleep(1.5)
                
                if click:
                    c = 5
                    return True
                
                else:
                    c += 1    
            
            except Exception as e:
                print(f"Find And Click - Exception: {e}\nXpath: {xpath}")       

    def sendkeys_click_insert(self, xpath, key, lock):
        
        try:
            element = self.search_element_by_xpath(xpath, lock)
            self.clicking_a_button(element, lock)
            self.my_send_keys(element, key, lock)
            
        except Exception as e:
            print(f"SendKeys Click Insert - Exception: {e}\nXpath: {xpath}\nKey: {key}")
            
    def type_of(self, variable):    
        
        tipo = type(variable)
        print(f"Tipo da váriavel: {tipo}.")
    