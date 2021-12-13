#<center>Manual</center>
The web crawler is a simple program,   
Using recursion the user can enter a url in the command line and recursively visit sites  

---
#How to use: 
The user will enter a command as such ` python src/crawler.py https://geeksforgeeks.org/ 3
`  
This will go to the site geeks for geeks, then crawl to a depth of 3. 
If the user add one more argument to the command line ` python src/crawler.py https://geeksforgeeks.org/ 3
 links` the crawler will save the urls to a `.csv` file called links   
if no extra argument is given the crawler will decide what to call the file   