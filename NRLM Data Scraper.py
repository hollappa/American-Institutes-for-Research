from selenium import webdriver
import time
import os
from pathlib import Path
import glob
 
path = os.path.join(r"C:\MIS Downloads\DisbursalofCIF") #set local path here
#path_to_chromedriver = 'G:\Gates SHG\Social Audit'
options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : path}
options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=options ,executable_path=r"C:\Users\cholla\Desktop\chromedriver.exe")  # path to your chromedriver

#url = "https://nrlm.gov.in/EnrtyStatusMPRAction.do?methodName=showDetail"
#url = "https://nrlm.gov.in/SHGSavingAmtMobilizedAction.do?methodName=showDetail"
#url = "https://nrlm.gov.in/MobilizationHouseholdsAction.do?methodName=showDetail&reportVar=total"
#url = "https://nrlm.gov.in/DisbursalOfRFAction.do?methodName=showDetail&reportVar=total"
url = "https://nrlm.gov.in/DisbursalOfCIFAction.do?methodName=showDetail&reportVar=total"

browser.get(url)
browser.set_page_load_timeout(45)
browser.maximize_window()

browser.find_element_by_id("all").click()
browser.find_element_by_id("allIandNI").click()
browser.find_element_by_xpath('//*[@value="Submit"]').click()            

col = browser.find_elements_by_xpath("//tr/td[2]")
rData = []
for webElement in col :
	rData.append(webElement.text)

state=[]
for e in rData[0:]:
    state.append(e)
    print(e)
state[:] = (value for value in state if value != 'Sub Total')
state[:] = (value for value in state if value != 'GRAND TOTAL')
state[:] = (value for value in state if value != '4')
state[:] = (value for value in state if value != '0')

month=['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
year=['2018-2019', '2019-2020'] #whichever years you want
month_2020=['APRIL', 'MAY', 'JUNE','JULY']
year_2020=['2020-2021']
#browser.find_element_by_link_text("BIHAR").click()


#select_dist = browser.find_element_by_name("ctl00$ContentPlaceHolder1$ddldist")
#options = [x for x in select_dist.find_elements_by_tag_name("option")]


for s in state[:]:
    browser.get(url)
    browser.find_element_by_id("all").click()
    browser.find_element_by_id("allIandNI").click()
    browser.find_element_by_xpath('//*[@value="Submit"]').click()            

    path1 =os.path.join(path, s) #generates the path into which to be downloaded
    os.makedirs(path1, exist_ok=True) 
    browser.find_element_by_link_text(s).click()
    time.sleep(4)

    elemn = browser.find_element_by_name("example_length")
    elemn.send_keys(100)
    col = browser.find_elements_by_xpath("//tr/td[2]")
    rData = []
    for webElement in col :
    	rData.append(webElement.text)
    rData[:] = (value for value in rData if value != 'Total')
    dist=[]
    #for e in rData[0:len(rData)-1]:
    for e in rData[0:]:    
        dist.append(e)
        print(e)
    dist[:] = (value for value in dist if value != '0')
    for e in dist[:]:
        #select_dist = browser.find_element_by_name("ctl00$ContentPlaceHolder1$ddldist")
        #select_dist.send_keys(e)
        elemn = browser.find_element_by_name("example_length")
        elemn.send_keys(100)

        browser.find_element_by_link_text(e).click()
        #path1 =os.path.join(path, s, e) #generates the path into which to be downloaded
        #os.makedirs(path1, exist_ok=True) 
        #os.chdir(path1)

        for x in year: #iterate over years - Yulia this is from the year array - if you have only one element
            elemyear = browser.find_element_by_name("year")
            elemyear.send_keys(x)
    
            for y in month: #iterate over months - as and when it stops you can update this to restart from a particular point
                elem2 = browser.find_element_by_name("month")
                elem2.send_keys(y)
                time.sleep(4)
                browser.find_element_by_xpath('//*[@alt="EXCEL"]').click()
         
        ##2020 financial year
        for x in year_2020: #iterate over years - Yulia this is from the year array - if you have only one element
            elemyear = browser.find_element_by_name("year")
            elemyear.send_keys(x)
    
            for y in month_2020: #iterate over months - as and when it stops you can update this to restart from a particular point
                elem2 = browser.find_element_by_name("month")
                elem2.send_keys(y)
                time.sleep(4)
                browser.find_element_by_xpath('//*[@alt="EXCEL"]').click()
    #click submit
        browser.find_element_by_xpath('//*[@value="Submit"]').click()            
        browser.find_element_by_link_text(s).click()