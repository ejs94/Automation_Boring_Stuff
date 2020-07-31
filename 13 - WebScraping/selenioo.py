from selenium import webdriver
browser = webdriver.Firefox(
    executable_path=r'D:\Program Files (x86)\Mozilla Firefox\geckodriver.exe')
browser.get('https://duckduckgo.com/')
searchElem = browser.find_element_by_css_selector(
    '#search_form_input_homepage')
searchElem.send_keys('UNIFEI')
searchElem.submit()
