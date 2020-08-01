import requests
from bs4 import BeautifulSoup

def get_jobs(word):
  try:
    jobs = []
    url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    prog_jobs = soup.find("section", {"id":"category-2"})
    lists = prog_jobs.find_all("li")[:-1]  
    for list in lists:
      link = list.find("a")["href"]
      link = f"https://weworkremotely.com/{link}"
      company = list.find("span", {"class":"company"}).text
      title = list.find("span", {"class":"title"}).text
      job = {"title": title, "company": company, "link": link}
      jobs.append(job)
    return jobs
  except:
    return []
      
  

