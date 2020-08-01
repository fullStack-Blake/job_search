import csv

def save_to_file(jobs, keyword):
  file = open(f"{keyword}.csv", encoding='utf-8-sig', mode="w")
  writer = csv.writer(file)
  writer.writerow(["title", "company", "link"])
  for job in jobs:
    writer.writerow(list(job.values()))
  return
