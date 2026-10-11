from bs4 import BeautifulSoup

with open('E:/Code/Python-Automation-60Days/day07/collected_html_code.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'lxml')

# with open('E:/Code/Python-Automation-60Days/day07/output_html.html', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())

job_titles = soup.find_all('p', attrs={'data-testid': 'job-title'})
for index, job in enumerate(job_titles, start=1):
    print(f"{index}. {job.text.strip()}")

with open('E:/Code/Python-Automation-60Days/day07/collected_html_code.html', 'r', encoding='utf-8') as f:
    content = f.read()
    print("File length:", len(content))