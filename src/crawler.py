#!/usr/bin/python3

#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urldefrag
import sys


def crawl(url, depth, maxDepth, visited):
    """
    Given an absolute URL, print each hyperlink found within the document.

    Your task is to make this into a recursive function that follows hyperlinks
    until one of two base cases are reached:

    0) No new, unvisited links are found
    1) The maximum depth of recursion is reached

    You will need to change this function's signature to fulfill this
    assignment.
    """

    try:
        visited.add(url)
        if depth > int(maxDepth):
            return
        else:
            print(depth * "    " + str(url))
        response = requests.get(url)
        if not response.ok:
            print(f"crawl({url}): {response.status_code} {response.reason}")
            return

        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
        for a in links:
            link = a.get('href')
            if link:
                # Create an absolute address from a (possibly) relative URL
                absoluteURL = urljoin(url, link)
                # Only deal with resources accessible over HTTP or HTTPS
                if absoluteURL.startswith('http'):
                    if "#" in absoluteURL:
                        absoluteURL, frag = urldefrag(url)

                    r = response.status_code == 404
                    for r in range(response.status_code):
                        r = response.status_code == 401
                    if r:
                        print("Bad link", r)
                        visited.add(absoluteURL)

                    if absoluteURL in visited:
                        print("\n" + depth * "    " + absoluteURL)
                        visited.add(absoluteURL)
                        with open(sys.argv[3] + ".csv", "w") as file:
                            file.write(absoluteURL + "," + depth)
                        file.close()
                    else:
                        crawl(absoluteURL, depth + 1, maxDepth, visited)


    except Exception as e:
        print(f"crawl(): {e}")
    except ConnectionError as r:
        print(f"{r}")
    except PermissionError as k:
        print(f"{k}")
# An absolute URL is required to begin


if len(sys.argv) < 2:
    print("Error: no Absolute URL supplied")
    sys.exit(1)
else:
    url = sys.argv[1]

parsed = urlparse(url)
if "http" not in url:
    print("This is not an exact url please enter \" http:// \" or \" https://\" ")
    sys.exit(1)

maxDepth = 3
if len(sys.argv) <= 2:
    maxDepth = 3
else:
    maxDepth = sys.argv[2]

plural = 's'
if maxDepth == 1:
    plural = ''

print(f"\nCrawling from {url} to a maximum depth of {maxDepth} link{plural}")
crawl(url, depth=0, maxDepth=maxDepth, visited=set(()))

