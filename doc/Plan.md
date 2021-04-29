*Replace the bold text with your own content*

*Adapted from https://htdp.org/2020-5-6/Book/part_preface.html*

# 0.  From Problem Analysis to Data Definitions
**<center>need to make a web crawler that visits websites and keeps track of each url that is visited**</center>  

##<center>The Crawler should</center>
*  start at a given url  
* Given the ammount of times to recurse the program will follow links up to the amount its given.
*   it will also keep following links until it reaches a link its already visited before.   
*  in which case it will stop.   
*  indentation used to determine the level of recursion that you are on.
*  once you hit the max recursion limit you have set it will keep running  
*  if there are more links but it wont click on any of them  

it will instead just print the links under the same indentation until it has found all links fo that page.
   
afterward it will comeback a level and start printing for that level, then back a level and so on....   

If the program has an error maybe it hits a bad link or something   
instead of crashing it will continue to run using exception handling to keep moving.

`depth:` will show the current depth of recursion you are currently on, this will be used in order to set the indentation of the program.  

`max depth: `is the maximum depth that the user sets (set to 3 by default) and this is where the program will stop recursing and start only printing links on the pages its been too.   

`Visited:` Visited: will display the links we've visited and will keep track of these links so that the crawler doesnt revisit them
 - If there is a "bad link" hard code these in to the Visited variable to that you dont visit these links after testing.  

`Crawl:` should be set at a default value of 0, meaning the starting point is 0.  
  - each time crawl is called `if (depth < maxDepth){ return crawl; }`   
  - `else{ print url; }`  
set indentation factor for each level of recursion.  
    - indent from each indentation. i.e 
  ```
  link0
    link1
      link2
        link3 -- stop 
        link
        link
        link
        link
      link
      link
      link
      link
    link
    link
    link
    link
    etc...    
```
use requests library to fetch webpages by url.   
look at anchor tags,   
if a href value is embedded in the anchor tag throw out the url indecated  
(these are just used to bring you to a different part of the page).  

- Remove the fragment section of the url if there is one.  
  
(fragments are indecated by their hash symbol usually followed by some phrase `#verryCoolKanye`)
# 1.  System Analysis
* give default values to `crawl`
```
crawl(url, depth, maxDepth, visited) 
```

* make sure the address provided is an absolute  
`if http / https is not in the adress then it is not an absolute adress `  
  

* need a way to indent each iteration  
`depth * "    " + url` will get a recursive indentation 
  

* need a recursive way to visit the websites  
`call crawl on absoluteURL and increase depth while calling visited and max depth in order to do recursive checks`
  
* add visited link to a set data type so they wont be revisited.   


* what to do once we hit our recursion limit  
`print links from each page starting from end call backward.`  
  if we hit a bad link, throw an exception add it to visited then keep crawling   
  
  




# 2.  Functional Examples
**<center>Get max recursion</center>**
```
if depth > (maxDepth)
    return
```

**<center>Setting indentation for recursion</center>**
```
print(depth * "    " + url
```
**<center>getting responses</center>**
```
response = reqests.get(url)
call crawl on the absolute url to join the page. 
```
**<center>Parsing urls</center>**
```
getting rid of the fragments ->  urldefrag(url) 
urljoin(url, link) link =  path,  url = scheme & location
```
**<center> Exception Handeling </center>**
```
get error if page does not exist  - error 404 
get error if do not have permissions to join page  - error 401
```




# 3.  Function Template

```python
try: 
    visited.add(url)
if dpeth > int(maxDepth):
    return
else: 
    print(depth * "    " + str(url))
response = reqeusts.get(url)


if absoluteURL.startswith('http'):
    if '#' in absoluteURL:
        absoluteURL, frag = urldefrag(url)
    r = response.status_code == 404
    k = response.status_code == 401
    if r:
        print("Bad link unable to join, ERROR 404")
        visited.add(absoluteURL)
    if k:
        print("Do not have correct permissions to join page, ERROR 401")
    
    if absoluteURL in visited:
        print(depth * "    " + absoluteURL)
        visited.add(absoluteURL)
    else:
        crawl(absoluteURL, depth + 1, maxDepth, visited)

except ConnectionError as r:
    print(f"{r}")
except PermissionError as k:
    print(f"{k}")
```


# 4.  Implementation

**This is the only part of the process focused on writing code in your chosen
programming language.**

**One by one translate passages of pseudocode into valid code.  Fill in the gaps
in the function template.  Exploit the purpose statement and the examples.**

**If you were thorough in the previous steps and are familiar with your
programming system this part will go by very quickly and the code will write
itself.**

**When you are learning a new programming language or an unfamiliar library this
phase can be slow and difficult.  As you gain experience with the relevant
technologies you will spend less and less time in this phase of the process.**


# 5.  Testing

**Articulate the examples given in step #2 as tests and ensure that each
function passes all of its tests.  Doing so discovers mistakes.  Tests also
supplement examples in that they help others read and understand the definition
when the need arises—and it will arise for any serious program.**

**As bugs are discovered and fixed, devise new test cases that will detect these
problems should they return.**

**If you didn't come across any bugs (lucky you!) think of a possible flaw and a
test that can be employed to screen for it.**

**At a minimum you should create a document explaining step-by-step how a
non-technical user may manually test your program to satisfy themselves that it
operates correctly.  Explain the entire process starting how to launch the
program, what inputs they should give and what results they should see at every
step.  Provide test cases of good and bad inputs to catch both false positives
and false negatives.  Any deviation from the expected outputs are errors.**

**The ideal is to write an automated test to avoid all manual labor beyond
launching the test.**
