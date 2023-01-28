#requires beautifulsoup4 and requests to be run properly

import requests
from bs4 import BeautifulSoup

#Url can be changed based on search

url = 'https://www.indeed.com/jobs?q=threat+analyst&l=&vjk=07e923112007ec7a'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#finds the job posting by class (may vary based on search)

job_titles = soup.find_all('a', {'class': 'jobtitle turnstileLink'})
for job in job_titles:
    print(job.text)

#saves the output to text file

with open('job_titles.txt', 'w') as file:
    file.writelines(job.text + '\n' for job in job_titles)




