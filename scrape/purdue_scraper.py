import base_scraper


def extract_job_links(soup):
    """

    :param soup:
    :return:
    """
    # Extract the job links from the page
    job_links = []

    # Selects each Job button and collects the job ids
    for job in soup.find_all('a', {'class': "jobTitle-link"}):
        job_links.append(job['href'])

    job_links = list(set(job_links))
    return job_links


def get_job_content_text(link, base_url="https://careers.purdue.edu"):
    return base_scraper.get_job_content_text(link, base_url=base_url)


def get_job_content_soup(link, base_url="https://careers.purdue.edu", pretty=False):
    return base_scraper.get_job_content_soup(link, base_url=base_url, pretty=pretty)


def get_title(soup):
    return soup.find('title').text


def get_content(soup):
    content = soup.find('div', {'class': 'jobDisplay'}).find('div', {'class': 'job'}).text
    content = content.split("Job Summary")[1].strip()
    content = content.split("Nearest Major Market:")[0].strip()
    return content


url = "https://careers.purdue.edu/search/?q=&locationsearch=west+lafayette"

soup = base_scraper.extract_soup(url)

links = extract_job_links(soup)

print(links[0])
soup = get_job_content_soup(links[0])

print(get_content(soup))
