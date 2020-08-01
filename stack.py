import requests
from bs4 import BeautifulSoup

def get_last_page(url):
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")

  try:
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    page_num = pages[-2].get_text(strip=True)
  except:
    page_num = 0
  return int(page_num)
  # when there's no second page, this returns 1

def extract_job(html):
  title_link = html.find("h2").find("a")
  title = title_link["title"]
  link = title_link["href"]
  link = f"https://stackoverflow.com/{link}"
  company = html.find("h3", {"class":"fs-body1"}).find("span").get_text(strip=True)
  return {
    "title": title,
    "company": company,
    "link": link
  }

def extract_jobs(last_page, url):
  jobs = []
  if last_page != 0:
    for page in range(last_page):
      result = requests.get(f"{url}&pg=page+1")
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find_all("div", {"class": "-job"})
      for result in results:
        job = extract_job(result)
        jobs.append(job)
  return jobs

def get_jobs(word):
  stack_url = f"https://stackoverflow.com/jobs?r=true&q={word}"
  last_page = get_last_page(stack_url)
  jobs = extract_jobs(last_page, stack_url)
  return jobs