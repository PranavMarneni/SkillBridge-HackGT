import requests
from bs4 import BeautifulSoup
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, WebDriverException
import time

print("TestETstTTETEUTYEUTYE")

logging.basicConfig(level=logging.INFO)

def validate_job_url(url):
    valid_domains = [
        'ziprecruiter.com', 'craigslist.org', 'simplyhired.com',
        'reed.co.uk', 'dice.com', 'facebook.com/jobs', 'indeed.com',
        'greenhouse.io', 'lever.co', 'workday.com', 'smartrecruiters.com',
        'myworkdayjobs.com', 'jobs.lever.co', 'boards.greenhouse.io'
    ]
    return any(domain in url for domain in valid_domains)

def get_selenium_page(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        
        logging.info(f"Navigating to URL: {url}")
        driver.get(url)
        
        time.sleep(5)  # Wait for page to load
        
        page_source = driver.page_source
        driver.quit()
        return page_source
    except Exception as e:
        logging.error(f"Error fetching page with Selenium: {e}")
        return None

def extract_job_details(soup, url):
    # Build a long string containing the job details
    job_details_str = f"Job URL: {url}\n"
    
    if 'indeed.com' in url:
        
        title = soup.select_one('h1.jobsearch-JobInfoHeader-title')
        if title:
            job_details_str += f"Title: {title.text.strip()}\n"
        else:
            #logging.warning("Could not find job title")
            job_details_str += "Title: Not found\n"
        
        company = soup.select_one('div[data-company-name="true"]')
        if company:
            job_details_str += f"Company: {company.text.strip()}\n"
        else:
            #logging.warning("Could not find company name")
            job_details_str += "Company: Not found\n"
        
        location = soup.select_one('div[data-testid="job-location"]')
        if location:
            job_details_str += f"Location: {location.text.strip()}\n"
        else:
            #logging.warning("Could not find job location")
            job_details_str += "Location: Not found\n"
        
        description = soup.select_one('div#jobDescriptionText')
        if description:
            job_details_str += f"Description: {description.text.strip()}\n"
        else:
            #logging.warning("Could not find job description")
            job_details_str += "Description: Not found\n"
    
    return job_details_str

def get_job_details(url):
    page_source = get_selenium_page(url)
    if page_source:
        soup = BeautifulSoup(page_source, 'html.parser')
        return extract_job_details(soup, url)
    return None

def main_royce():
    # List of URLs to scrape
    jobUrlList = [
        'https://www.indeed.com/q-software-engineer-l-atlanta,-ga-jobs.html?vjk=5e9e805838d10141&advn=6984854090123921',
        'https://www.indeed.com/q-software-engineer-l-atlanta,-ga-jobs.html?vjk=1c5767a93c89b736&advn=1082936424650003'
    ]
    
    jobScrapeList = []
    
    for url in jobUrlList:
        if validate_job_url(url):
            #logging.info(f"Scraping job details from: {url}")
            job_data = get_job_details(url)
            if job_data:
                jobScrapeList.append(job_data)  # Add long string to list
                #logging.info(f"Scraped Job Data: {job_data}")
            #else:
                #logging.warning(f"Failed to extract job details from: {url}")
        #else:
            #logging.warning(f"Invalid URL skipped: {url}")
    
    # Output all scraped data in list format
    if jobScrapeList:
        return jobScrapeList  # Return the list of long strings
    else:
        return []

if __name__ == "__main__":
    scraped_jobs_list = main()
    if scraped_jobs_list:
        print("\nFinal Scraped Jobs List (Strings):")
        for job_str in scraped_jobs_list:
            print(job_str)  # Print each long string
            print("-" * 80)  # Separator for readability
