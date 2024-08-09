from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from UI_formatting import format

def get_rating(user_input):
    model_name=format(user_input)
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.get('https://www.pcmag.com/reviews/{model_name}')

    try:
        # Wait for the rating element to be present
        rating_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/main/div/header/div/div[1]/div[2]'))
        )
        rating = rating_element.text.strip()
        return rating
    
    except Exception as e:
        return None
    
    finally:
        driver.quit()

if __name__ == "__main__":
    get_rating()
