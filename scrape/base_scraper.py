from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def extract_soup(url):
    """

    :param url:
    :return:
    """
    # Runs chrome in a manner to allow for web-scraping to not be stopped by cloudflare
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # disable GPU acceleration to improve performance
    chrome_options.add_argument("--no-sandbox")  # disable sandbox to avoid Chrome hangs
    chrome_options.add_argument("--disable-dev-shm-usage")  # disable shared memory to avoid Chrome crashes
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")

    driver = webdriver.Chrome(options=chrome_options)

    # enable JavaScript and cookies
    # driver.execute_script("document.cookie='cookies_enabled=true';")
    driver.execute_script("navigator.webdriver = false;")
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")

    # load the page with Selenium
    url = url
    driver.get(url)

    # extract the HTML content with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    content = soup.get_text()

    # close the browser
    driver.quit()

    return soup


def get_job_content_soup(link, base_url, pretty=False):
    base_url = base_url

    url = base_url + link

    # Runs chrome in a manner to allow for web-scraping to not be stopped by cloudflare
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # disable GPU acceleration to improve performance
    chrome_options.add_argument("--no-sandbox")  # disable sandbox to avoid Chrome hangs
    chrome_options.add_argument("--disable-dev-shm-usage")  # disable shared memory to avoid Chrome crashes
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_script("navigator.webdriver = false;")
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    if pretty:
        return soup.prettify()
    return soup


def get_job_content_text(link, base_url):
    base_url = base_url

    url = base_url + link

    # Runs chrome in a manner to allow for web-scraping to not be stopped by cloudflare
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # disable GPU acceleration to improve performance
    chrome_options.add_argument("--no-sandbox")  # disable sandbox to avoid Chrome hangs
    chrome_options.add_argument("--disable-dev-shm-usage")  # disable shared memory to avoid Chrome crashes
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_script("navigator.webdriver = false;")
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    content = soup.get_text()

    return content