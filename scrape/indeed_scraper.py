from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import base_scraper
import urllib.parse


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


def get_job_content_text(link, base_url="https://www.indeed.com/viewjob?jk="):
    return base_scraper.get_job_content_text(link, base_url=base_url)


def get_job_content_soup(link, base_url="https://www.indeed.com/viewjob?jk=", pretty=False):
    return base_scraper.get_job_content_soup(link, base_url="https://www.indeed.com/viewjob", pretty=pretty)


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
        soup = base_scraper.extract_soup(url)
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
    soup = base_scraper.extract_soup(url)
    links = extract_job_links(soup)

    content = get_job_content_text(links[0])
    print(content)



