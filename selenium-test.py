# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,datetime

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/home.html"
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
                pass
        else: self.fail("time out")
        driver.find_element_by_id("footer-logo2").click()
        while 1:
            # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | tab=0 | ]]
            for i in range(60):
                try:
                    if self.is_element_present(By.ID, "btn1"):
                        print("btn1-present")
                        click1=driver.find_element_by_id("btn1").click()
                        if click1 != None:
                            print("click1=%s" % click1)
                            return
                        else:
                            print("b-click1=%s" % click1)
                            print("b-click1 time=%s" % datetime.datetime.now())
                            break
                    else:
                        print("btn1-not_element_present")
                        driver.find_element_by_xpath("//html").send_keys(Keys.F5)
                        print("btn1f5")
                        time.sleep(1)
                except:
                    print("not_btn1 time=%s" % datetime.datetime.now())
                    pass
                time.sleep(1)
            else: self.fail("time out")
            
            for i in range(60):
                try:
                    if self.is_element_present(By.XPATH, "/html/body/div/div[4]"):
                        print("div[4]_element_present")
                        click2=driver.find_element_by_xpath("/html/body/div/div[4]").click()
                        if click2 != None:
                            print("click2=%s" % click2)
                            return
                        else:
                            print("b-click2=%s" % click2)
                            print("b-click2 time=%s" % datetime.datetime.now())
                            break          
                except:
                    print("not_div[4] time=%s" % datetime.datetime.now())
                    pass
                time.sleep(1)
         
            else: self.fail("time out")
        return
        #driver.find_element_by_id("btn1").click()
        #driver.find_element_by_xpath("/html/body/div/div[4]").click()
    
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
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
