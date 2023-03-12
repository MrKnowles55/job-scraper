from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.parse


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


def extract_job_links(soup):
    """

    :param soup:
    :return:
    """
    # Extract the job links from the page
    job_links = []

    # Selects each Job button and collects the job ids
    for job in soup.find_all('a', {'role': 'button'}):
        if 'id' in job.find('span').attrs:
            link = job.find('span')['id']
            job_links.append(link[9:])
        else:
            raise KeyError("'id' not found in job:", job)
    return job_links


def get_job_content_text(link):
    """

    :param link:
    :return:
    """
    url_base = "https://www.indeed.com/viewjob?jk="

    url = url_base + link

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


def get_job_content_soup(link, pretty=True):
    """

    :param link:
    :return:
    """
    url_base = "https://www.indeed.com/viewjob?jk="

    url = url_base + link

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


def build_indeed_url(base_url, query, location, experience_level=None, is_remote=None, education=None, start=None):
    url_params = {
        'q': query,
        'l': location,
    }
    if experience_level:
        url_params['explvl'] = experience_level
    if is_remote:
        url_params['remote'] = 'true' if is_remote else 'false'
    if education:
        url_params['edu'] = education
    if start:
        url_params['start'] = start

    query_string = urllib.parse.urlencode(url_params)
    return f"{base_url}?{query_string}"


def extract_multiple_pages_from_url(pages, base_url, query, location, experience_level=None, is_remote=None, education=None):
    link_list = []
    for page in range(pages):
        url = build_indeed_url(base_url, query, location, experience_level, is_remote, education, page*10)
        soup = extract_soup(url)
        links = extract_job_links(soup)
        link_list += links

    return list(set(link_list))


def save_links(links: list, filename="data/job_links.txt"):
    with open(filename, 'w') as f:
        for link in links:
            f.write(link + '\n')


def load_links(filename="data/job_links.txt"):
    with open(filename, 'r') as f:
        return f.read().splitlines()


# Example usage:
if __name__ == "__main__":
    base_url = 'https://www.indeed.com/jobs'
    query = '$50,000'
    location = 'Lafayette, IN'
    experience_level = 'entry_level'
    is_remote = False
    education = 'Bachelor'

    # links = extract_multiple_pages_from_url(1, base_url, query, location, experience_level, is_remote, education)
    # content = get_job_content(links[0])

    url = build_indeed_url(base_url,query,location,experience_level,is_remote,education)
    soup = extract_soup(url)
    links = extract_job_links(soup)

    content = get_job_content_text(links[0])
    print(content)



