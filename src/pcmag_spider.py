from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

service = Service(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service)
driver.get('https://www.pcmag.com/reviews/fitbit-sense-2')

rating_element = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div/header/div/div[1]/div[2]')
rating = rating_element.text
print(f'Review Rating: {rating}')

driver.quit()


