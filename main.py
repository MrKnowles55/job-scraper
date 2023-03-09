from scrape.indeed_scraper import *

if __name__ == '__main__':
    soup = extract_soup('https://www.indeed.com/jobs?q=python+developer&l=New+York+City%2C+NY')
    links = extract_job_links(soup)
    content = get_job_content(links[0])
    print(content)
