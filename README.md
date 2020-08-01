# Job Search Scrapper

## Prerequisites
flask, BeautifulSoup4, requests has to be installed
I used repl since this is small project and getting to know with flask

## How does this app works
Basically this is a Job scrapper on 3 websites.
Each python files scrapping jobs on

  **https://remoteok.io**
  
  **https://stackoverflow.com**
  
  **https://weworkremotely.com**
 
 and presents in detail.html
 
 This is a small project using local database (fake db)
 However, if the user searched certain keyword, the fake db will store the information and re-use it.
 
 For example, let's assume that the user searched python, react and python.
 When the user searches python for the second time, the scrapper will not send get request
 since it is stored temporarily in the database.
 
 User can download .csv file using hyperlink.
