import requests
from bs4 import BeautifulSoup
import csv

url = 'https://realpython.github.io/fake-jobs/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')

# print(soup.prettify())

csv_file = open('E:/Code/Python-Automation-60Days/day07/demo_jobs.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Job name', 'Company name', 'Location', 'More info'])

for job in soup.find_all('div', class_='card-content'):

    try:
        job_title = job.find('h2', class_ = 'title is-5').text
        company = job.find('h3', class_ = 'subtitle is-6 company').text
        location = job.find('p', class_='location').text.strip()
        info = job.find('a', class_='card-footer-item')['href']

    except Exception:
        job_title = None
        company = None
        location = None
        info = None

    csv_writer.writerow([job_title, company, location, info])

    print(f'Job name: {job_title}')
    print(f'Company name: {company}')
    print(f'Location: {location}')
    print(f'More info: {info}')
    print()

csv_file.close()
