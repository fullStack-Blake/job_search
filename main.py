from flask import Flask, render_template, request, redirect, send_file
from stack import get_jobs as get_stack
from remoteok import get_jobs as get_remoteok
from wework import get_jobs as get_wework
from save import save_to_file

db = {}

app = Flask("Job_Finder")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def search():
  term = request.args["term"]
  if term:
    term = term.lower()
    existing_jobs = db.get(term)
    if existing_jobs:
      jobs = existing_jobs
    else:
      jobs = []
      jobs += get_stack(term)
      jobs += get_remoteok(term)
      jobs += get_wework(term)

      db[term] = jobs

    return render_template("detail.html", term = term, terms=jobs, num_jobs=len(jobs))
  
  else:
    return redirect("/")

@app.route("/export/<keyword>")
def export(keyword):
  try:
    jobs = db.get(keyword)
    if jobs:
      print("HERE")
      save_to_file(jobs, keyword)
      filename = f"{keyword}.csv"
      print(filename)

      return send_file(filename, mimetype="text/csv")
    else:
      print("Nothing")
  except:
    return print("Wrong")

app.run(host="0.0.0.0")
