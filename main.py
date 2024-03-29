from bs4 import BeautifulSoup
import requests
import sys
def get_jobs(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    return jobs



def main():
    def print_job_details(job, index):
        company_name = job.find("h3", class_="joblist-comp-name").text.strip()
        skills = job.find("span", class_="srp-skills").text.strip()
        more_info = job.find("h2").a["href"]

        with open(f'post/{index}.txt', 'w') as f:
            f.write(f"Company Name: {company_name}\n")
            f.write(f"Skills Required: {skills}\n")
            f.write(f"More Info: {more_info}\n")
        print(f"file saved: {index}")


    base_url = "https://www.timesjobs.com/candidate/job-search.html"
    url_params = "?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation="
    url = base_url + url_params
    jobs = get_jobs(url)

    for index, job in enumerate(jobs):
        job_published_date = job.find("span", class_="sim-posted").text
        skills = job.find("span", class_="srp-skills").text.strip()

        if 'few' in job_published_date and (
                operating_choice == '1' and unfamiliar_skills not in skills) or operating_choice == '2':
            print_job_details(job, index)


if __name__ == "__main__":
    print("If you want to filter skills, press 1; otherwise, press 2")
    operating_choice = input(" > ")
    if operating_choice not in ('1', '2'):
        print("Invalid choice. Please enter 1 or 2.")
        sys.exit()

    if operating_choice == '1':
        print("Enter skills that you are unfamiliar with:")
        unfamiliar_skills = input("> ")

    main()
