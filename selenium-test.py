# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,datetime,os,sys

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://baidu.com/home.html"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get(self.base_url + "")
        driver.find_element_by_id("tel").click()
        driver.find_element_by_id("tel").clear()
        driver.find_element_by_id("tel").send_keys("123")
        driver.find_element_by_id("pwd").click()
        driver.find_element_by_id("pwd").clear()
        driver.find_element_by_id("pwd").send_keys("456")
        driver.find_element_by_xpath("//*[@id=\"login\"]/button").click()

        for i in range(60):
            try:
                if self.is_element_present(By.XPATH, "//*[@id=\"myModal\"]/div/img[2]"):
                    print("is_element_present")
                    driver.find_element_by_xpath("//*[@id=\"myModal\"]/div/img[2]").click()
                    print("myModalclick")
                    driver.find_element_by_xpath("//html").click()
                    print("htmlclick")
                    break
                else:
                    print("not_element_present")
                    driver.find_element_by_xpath("//html").send_keys(Keys.F5)
                    print("f5")
                    time.sleep(1)
            except:
                print("except1")
                time.sleep(1)
                #driver.refresh()
                driver.find_element_by_xpath("//html").send_keys(Keys.F5)
                print("f51")
                continue
        else: self.fail("time out")
        driver.find_element_by_id("footer-logo2").click()
        tag=True
        while True:
            try:
                if self.is_element_present(By.ID, "btn1"):
                    print("btn1-present")
                    try:
                        a = driver.find_element_by_xpath("/html/body/div/div[3]/ul/li/a/h3").text
                        print("a4=%s" % a)
                        if a=='60':
                            print("a60=%s" % a)
                            print("a60-time=%s" % datetime.datetime.now())
                            os.system('TASKKILL /F /IM geckodriver.exe')
                            #exit(1)
                            tag=False
                            return
                        else:
                            print("a1=%s" % a)
                            click1=driver.find_element_by_id("btn1").click()
                            if self.is_element_present(By.XPATH, "/html/body/div/div[4]"):
                                print("div[4]_element_present")
                                click2=driver.find_element_by_xpath("/html/body/div/div[4]").click()
                                print("b-click2 time=%s" % datetime.datetime.now())                           
                                continue
                            else:
                                print("div[4] no time=%s" % datetime.datetime.now())
                                continue
                        
                    except BaseException as e:
                        print("h3 except time=%s" % datetime.datetime.now())
                        print(e)
                else:
                    print("btn1-not_element_present")
                    driver.find_element_by_xpath("//html").send_keys(Keys.F5)
                    print("btn1f5 %s" % datetime.datetime.now())
                    time.sleep(1)
                    continue
            except:
                print("except time=%s" % datetime.datetime.now())
                time.sleep(1)
                continue
            
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
