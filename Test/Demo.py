from selenium import webdriver

driver = webdriver.Chrome(executable_path='D:\chromedriver.exe')
driver.maximize_window()
driver.get("http://denasps19bs:8080/webapp/")