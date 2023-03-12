from scrape.indeed_scraper import *

if __name__ == '__main__':
    links = load_links()
    content = get_job_content_soup(links[0])
    print("https://www.indeed.com/viewjob?jk="+links[0])
    print(content)
