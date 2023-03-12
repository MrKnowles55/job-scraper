from scrape.indeed_scraper import *
import re


def get_title(soup):
    # Find the HTML element containing the job title using a CSS selector
    job_title_element = soup.select_one('.jobsearch-JobInfoHeader-title')

    # Get the text content of the HTML element
    return job_title_element.text.strip()


def get_employer(soup):
    try:
        text = soup.select_one('.jobsearch-CompanyInfoWithReview').text.strip()
        company_regex = re.compile(r'^(.*?)(\d.*)')
        employer = company_regex.search(text).group(1).strip()
    except:
        text = soup.select_one('.jobsearch-CompanyInfoWithoutHeaderImage').text.strip()
        company_regex = re.search(r'\b[A-Z][a-z]*', text)
        employer = company_regex.group(0)
    print(text)
    return employer


def get_location(soup):
    try:
        text = soup.select_one('.jobsearch-CompanyInfoWithReview').text.strip()
        location_regex = re.compile(r'^(.*?)(\d.*)')
        location = location_regex.search(text).group(1).strip()
    except:
        text = soup.select_one('.jobsearch-CompanyInfoWithoutHeaderImage').text.strip()
        location_regex = re.findall(r'[A-Z][a-z]*', text)
        location = location_regex[1]
    print(text)
    return location



links = load_links()

for link in links:
    soup = get_job_content_soup(link, pretty=False)
    print("https://www.indeed.com/viewjob?jk="+link)
    print(get_title(soup))
    print(get_employer(soup))
    print(get_location(soup))
    print("-"*10)




