import requests
from bs4 import BeautifulSoup

def get_jobs(word):
  try:
    jobs = []
    url = f"https://remoteok.io/remote-dev+{word}-jobs"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    trs = soup.find("table", {"id":"jobsboard"}).find_all("tr", {"class":"job"})
    for tr in trs:
      time = tr.find("time").text
      # I only saved jobs posted within a month since this
      # website has many invalid pages
      if 'd' in time:
        title = tr.find("h2", {"itemprop":"title"}).text
        company = tr.find("h3", {"itemprop":"name"}).text
        link = tr["data-id"]
        link = f"https://remoteok.io/l/{link}"
        job = {"title": title, "company": company, "link": link,}
        jobs.append(job)

    return jobs
  except:
    return []
      
  

