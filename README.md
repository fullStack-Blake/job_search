# Job Search Scrapper

## Prerequisites
**flask, BeautifulSoup4, requests** has to be installed
I used **repl** since this is a small project

## How does this app works
This is a **Job scrapper** with user selected keyword.
It scraps job information from 3 different websites.

Each *python* files scrapping jobs on

  **https://remoteok.io**
  
  **https://stackoverflow.com**
  
  **https://weworkremotely.com**
 
 and presents in *detail.html*
 
 This will not store the information on the 3rd party database since we only need the recent info.
 However, to not waste our bandwidth, we will store the information while the program runs.
 
 For example, let's assume that the user searched python, react and python.
 When the user searches python for the second time, the scrapper will not send the get request
 since it is stored temporarily in the local database.
 
 There is a hyperlink for user to download the output in .csv file
 
 *Happy Coding!*
