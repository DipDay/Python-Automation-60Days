import requests

url = 'https://bdjobs.com/h/jobs?qOT=&txtsearch=python&lang=en'
# url = "https://www.timesjobs.com/job-search?keywords=%22python%22%2C&location=&experience=&refreshed=true"

r = requests.get(url)

with open('E:/Code/Python-Automation-60Days/day07/collected_html_code.html', 'w', encoding='utf-8') as f:
    f.write(r.text)

