import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

def scrape(website):
    print("Launching Chrome")
    
    chrome_driver_path = "./chromedriver.exe"
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()

def extract_content(html):
    soup = BeautifulSoup(html, "html.parser")
    body = soup.body
    if body:
        return str(body)
    return None

def clean_body(body):
    soup = BeautifulSoup(body, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()
    
    cleaned_body = soup.get_text(separator="\n")

    cleaned_body = "\n".join(line.strip() for line in cleaned_body.splitlines() if line.strip())

    return cleaned_body

def split_dom_content(content, max_lenght=6000):
    return[
        content[i:i+max_lenght] for i in range(0, len(content), max_lenght)
    ]

