from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text
soup = BeautifulSoup(html_text, "lxml" )
jobs = soup.find("li", class_="clearfix job-bx wht-shd-bx")
company_name = soup.find("h3", class_= "joblist-comp-name").text.replace(" ", "")
print(company_name)