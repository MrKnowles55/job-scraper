from scrape.indeed_scraper import *

if __name__ == '__main__':
    soup = extract_soup('https://www.indeed.com/jobs?q=%2450%2C000&l=Lafayette%2C+IN&vjk=9033c2d3fdeeaaf8')
    links = extract_job_links(soup)
    content = get_job_content(links[0])
    print(content)
